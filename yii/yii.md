

##其他
---------------------------
##### XSS过滤
    use yii\helpers\Html;
    $value=Html::encode('<script>alert("abc");</script>');

##### 获取CSRF Token
    Yii::$app->request->getCsrfToken();
    Yii::$app->request->csrfToken;


##方法
---------------------------
##### 获取版本
    Yii::getVersion();



##模型/控制器
---------------------------
##### 模型加载Post数据
    $model->load(Yii::$app->request->post());

##### 模型必填值校验
    $model->validate();


##对象
---------------------------
##### 全局应用实例/单例/服务定位器
    Yii::$app   

##### 数据库操作对象
	#yii\db\Connection
	#vendor/yiisoft/yii2/db/Connection.php
	Yii::$app->db

##### 请求对象
	Yii::$app->request

##### Redis对象
	Yii::$app->redis



##位置
---------------------------
##### 小部件引用及位置
	use yii\widgets\......
	vendor/yiisoft/yii2/widgets/

##### 基类控制器引用及位置
	use yii\web\Controller;
	vendor/yiisoft/yii2/web/Controller.php

##### 基类模型引用及位置
	use yii\base\Model;
	vendor/yiisoft/yii2/base/Model.php

##### Data引用及位置
	#如分页器
	use yii\data\Pagination;
	vendor/yiisoft/yii2/data/Pagination.php

##### Helper引用及位置
	#如Html助手
	use yii\helpers\Html;
	vendor/yiisoft/yii2/helpers/Html.php

