## 存取控制过滤器
存取控制过滤器（ACF）是一种通过 yii\filters\AccessControl 类来实现的简单授权方法， 非常适用于仅需要简单的存取控制的应用

#### site 控制器中使用 ACF
~~~
use yii\web\Controller;
use yii\filters\AccessControl;

class SiteController extends Controller
{
    public function behaviors()
    {
        return [
            'access' => [
                'class' => AccessControl::className(),
                'only' => ['login', 'logout', 'signup'],
                'rules' => [
                    [
                        'allow' => true,
                        'actions' => ['login', 'signup'],
                        'roles' => ['?'],
                    ],
                    [
                        'allow' => true,
                        'actions' => ['logout'],
                        'roles' => ['@'],
                    ],
                ],
            ],
        ];
    }
    // ...
}
~~~

#### 用户没有获得执行当前动作的授权时

- 如果该用户是访客，将调用 yii\web\User::loginRequired() 将用户的浏览器重定向到登录页面。
- 如果该用户是已认证用户，将抛出一个 yii\web\ForbiddenHttpException 异常。

通过配置 yii\filters\AccessControl::$denyCallback 属性定制该行为

~~~
[
    'class' => AccessControl::className(),
    ...
    'denyCallback' => function ($rule, $action) {
        throw new \Exception('You are not allowed to access this page');
    }
]
~~~


#### Access rules 支持很多的选项
- allow： 指定该规则是 "允许" 还是 "拒绝" 
- actions：指定该规则用于匹配哪些动作
- controllers：指定该规则用于匹配哪些控制器
- roles：指定该规则用于匹配哪些用户角色
    - ?： 用于匹配访客用户 （未经认证）
    - @： 用于匹配已认证用户
- ips：指定该规则用于匹配哪些 yii\web\Request::userIP 
- verbs：指定该规则用于匹配哪种请求方法
- matchCallback：指定一个PHP回调函数用于 判定该规则是否满足条件,当这个规则不满足条件时该函数会被调用

~~~
use yii\filters\AccessControl;

class SiteController extends Controller
{
    public function behaviors()
    {
        return [
            'access' => [
                'class' => AccessControl::className(),
                'only' => ['special-callback'],
                'rules' => [
                    [
                        'actions' => ['special-callback'],
                        'allow' => true,
                        'matchCallback' => function ($rule, $action) {
                            return date('d-m') === '31-10';
                        }
                    ],
                ],
            ],
        ];
    }

    // 匹配的回调函数被调用了！这个页面只有每年的10月31号能访问（译者注：原文在这里说该方法是回调函数不确切，读者不要和 `matchCallback` 的值即匿名的回调函数混淆理解）。
    public function actionSpecialCallback()
    {
        return $this->render('happy-halloween');
    }
}
~~~

