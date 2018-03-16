

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

##### 写日志
	#2018-03-16 05:41:16 [::1][-][-][error][application] XXX
	Yii::error('XXX');
	Yii::info('XXX');



##模型/控制器/视图方法
---------------------------
##### 模型加载Post数据
    $model->load(Yii::$app->request->post());

##### 模型必填值校验
    $model->validate();


##对象/应用组件
---------------------------
##### 全局应用实例/单例/服务定位器
	#应用主体是管理 Yii 应用系统整体结构和生命周期的对象。 每个Yii应用系统只能包含一个应用主体，应用主体在 入口脚本 中创建并能通过表达式 \Yii::$app 全局范围内访问。
	#网页应用主体
    Yii::$app   
	#在应用中可以任意注册组件，并可以通过表达式 \Yii::$app->ComponentID 全局访问

##### 数据库操作对象
	#yii\db\Connection
	#vendor/yiisoft/yii2/db/Connection.php
	Yii::$app->db

##### 请求对象
	Yii::$app->request

##### Redis对象
	Yii::$app->redis

##### 获取模块
	#vendor/yiisoft/yii2/base/Module.php
	Yii::$app->getModule('gii');

##### 访问params参数
	Yii::$app->params['adminEmail'];

##### 返回应用的版本
	Yii::$app->getVersion();
	Yii::$app->version;

##### primary cache
	\Yii::$app->cache


##位置
---------------------------

##### 基类模块
	use yii\bsae\Module
	vendor/yiisoft/yii2/base/Module.php
	#继承ServiceLocator

#### 基类组件
	use yii\base\Component
	vendor/yiisoft/yii2/base/Component.php
	#继承BaseObject

##### 基类控制器引用及位置
	use yii\web\Controller;
	vendor/yiisoft/yii2/web/Controller.php
	#继承yii\base\Controller继承组件

##### 基类模型引用及位置
	use yii\base\Model;
	vendor/yiisoft/yii2/base/Model.php
	#继承组件

#### 基类小部件
	use yii\base\Widget
	vendor/yiisoft/yii2/base/Widget.php
	#继承组件

##### 小部件引用及位置
	use yii\widgets\......
	vendor/yiisoft/yii2/widgets/
	#一类继承基类小部件

##### Data引用及位置
	#如分页器
	use yii\data\Pagination;
	vendor/yiisoft/yii2/data/Pagination.php
	#继承BaseObject

##### Helper引用及位置
	#如Html助手
	use yii\helpers\Html;
	vendor/yiisoft/yii2/helpers/Html.php
	#继承BaseHtml

##### Gii
	http://XXXX/index.php?r=gii
	vendor/yiisoft/yii2/base/Module.php
	gii模块类是 yii\gii\Module
	vendor\yiisoft\yii2-gii\

##### 入口文件
	#web应用
	web/index.php
	#控制台应用
	yii

