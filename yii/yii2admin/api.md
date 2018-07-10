## RESTful Web 服务(API)

### 如何新建一个API接口
1. 修改api/config/main.php>>modules属性
2. 增加一个模块(若不存在),tp表示太平项目
~~~php
'tp'=>[
            'class'=>'api\modules\tp\Module',
            'defaultRoute'=>'index',
        ],
~~~
3. 新建api\modules\tp目录(若不存在)
4. 新建api\modules\tp\Module.php文件
~~~php
<?php
namespace api\modules\tp;
class Module extends \yii\base\Module
{
    public $controllerNamespace = 'api\modules\tp\controllers';
    public function init()
    {
        parent::init();
    }
}
~~~
5. 新建api\modules\tp\controllers目录(若不存在)
6. 新建一个控制器api\modules\tp\controllers\TestController.php (前缀Test首字母大写,后缀Controller是固定的)
~~~php
<?php
// 命名空间
namespace api\modules\tp\controllers;
// 继承 yii\rest\ActiveController 可以默认实现index/update/view等方法
use yii\rest\ActiveController;
use yii\filters\auth\QueryParamAuth;
class TestController extends ActiveController{
    // 一般是用对应model的, 这样查数据方便, 可以无对应Model,但不能为null
    public $modelClass = 1; // 'common\modelsgii\User';

    // 重写行为方法
    public function behaviors(){
        $behaviors=parent::behaviors();
        // 设置认证方式. 不设置则无需access-token,可以随便调用
        $behaviors['authenticator']=['class'=>QueryParamAuth::className(),];
        // 响应格式,默认已支持xml/json,由request的accept决定,可以不设置
        // $behaviors['contentNegotiator']['formats']['text/html'] = \yii\web\Response::FORMAT_HTML;
        return $behaviors;
    }
    // 覆盖actions方法,禁用原来的动作
    public function actions(){
        $actions=parent::actions();
        unset($actions['index'],$actions['view'],$actions['create'],$actions['update'],$actions['delete'],$actions['options']);
        return $actions;
    }
    // 默认入口方法
    public function actionIndex(){
        $value=\Yii::$app->request->get();
        return $value;
    }
    // 其他方法
    public function actionFormat(){
        return Array(
            'status'=>200,
            'msg'=>null,
            'data'=>Array('key'=>101,'value'=>'测试值'),
        );
    }
}
~~~
7. 修改nginx配置:vim /usr/local/nginx/conf/vhost/default.conf
~~~
# API重写
location ~ /api/(tp|v) {
~~~
8. 重启nginx服务: /etc/init.d/nginx restart
9. 测试接口:
~~~
http://47.106.160.48/api/tp/test?access-token=e282486518
http://47.106.160.48/api/tp/test/format?access-token=e282486518
~~~



### 授权验证的控制
~~~
由api/config/main.php中的components>>user>>identityClass控制
'components' => [
        'user' => [
            'class' => 'yii\web\User',
            'identityClass' => 'api\models\User',

api\models\User.php(可参考源码)
需实现IdentityInterface接口的findIdentityByAccessToken()方法
public static function findIdentityByAccessToken($token, $type = null)
以判断token是否有效
~~~


### 速率限制
~~~
也由由api/config/main.php中的components>>user>>identityClass控制

api\models\User.php(可参考源码)
需实现RateLimitInterface接口的三个方法:
// 每10秒5次API调用
public  function getRateLimit($request, $action){
    return [5, 10];
}
// 返回剩余的允许的请求和最后一次速率限制检查时相应的 UNIX 时间戳数
public  function loadAllowance($request, $action){
    return [$this->allowance, $this->allowance_updated_at];
}
// 保存剩余的允许请求数和当前的 UNIX 时间戳
public  function saveAllowance($request, $action, $allowance, $timestamp){
    $this->allowance = $allowance;
    $this->allowance_updated_at = $timestamp;
    $this->save();
}
~~~