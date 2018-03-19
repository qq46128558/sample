

##其他
---------------------------
##### XSS过滤
    use yii\helpers\Html;
    $value=Html::encode('<script>alert("abc");</script>');

##### 保证HTML内容数据输出安全
	use yii\helpers\HtmlPurifier;
	echo HtmlPurifier::process($post->text);

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

##### 将驼峰式大小写变量名转换为多个首字母大写的单词
	use yii\helpers\Inflector;
	echo Inflector::camel2words("helloWorld", true);


##模型/控制器/视图方法
---------------------------
##### 模型加载Post数据
    $model->load(Yii::$app->request->post());

##### 模型必填值校验
    $model->validate();

##### 设置模型使用场景
	$model->scenario = 'login';
	#或者
	$model = new User(['scenario' => 'login']);
	#覆盖yii\base\Model::scenarios()方法来自定义行为
	#!表示非安全属性,需单独赋值
	return [
        'login' => ['username', 'password','!secret'],
        'register' => ['username', 'email', 'password'],
    ];

##### 块赋值
	#用户输入数据赋值到模型属性
	$model->attributes = \Yii::$app->request->post('ContactForm');

##### 模型数据验证
	$model->validate();

##### 模型数据验证规则
	#覆盖 yii\base\Model::rules() 方法
	#on为应用场景
	#safe为安全属性
	return [
        [['name', 'email', 'subject', 'body'], 'required', 'on' => 'register'],
        ['email', 'email'],
		[['title', 'description'], 'safe'],
    ];

##### 模型转换为数组
	$post = \app\models\Post::findOne(100);
	$array = $post->attributes;

##### 模型转换为字段数组
	#返回fields()方法定义的所有字段和extraFields()方法定义的prettyName and fullAddress字段
	$array = $model->toArray([], ['prettyName', 'fullAddress']);
	#覆盖 fields() 来增加、删除、重命名和重定义字段
	return [
        // 字段名和属性名相同
        'id',

        // 字段名为 "email"，对应属性名为 "email_address"
        'email' => 'email_address',

        // 字段名为 "name", 值通过PHP代码返回
        'name' => function () {
            return $this->first_name . ' ' . $this->last_name;
        },
    ];
	#或者
	$fields = parent::fields();
    // 去掉一些包含敏感信息的字段
    unset($fields['auth_key'], $fields['password_hash'], $fields['password_reset_token']);
    return $fields;

##### 默认控制器
	#yii\base\Application::defaultRoute
	#yii\web\Application::defaultRoute
	echo \Yii::$app->defaultRoute;

##### 控制器独立动作
	#覆盖yii\base\Controller::actions()方法
	#创建一个独立操作类,继承yii\base\Action 或它的子类,并实现公有的名称为run()的方法

##### 控制器默认动作
	#由 yii\base\Controller::$defaultAction 属性指定的默认操作
	public $defaultAction = 'home';

##### 控制器生命周期
	- 在控制器创建和配置后，yii\base\Controller::init() 方法会被调用
	- 控制器根据请求操作ID创建一个操作对象(action)
	- 控制器按顺序调用应用主体、模块（如果控制器属于模块）、 控制器的 beforeAction() 方法
	- 控制器执行操作
	- 控制器按顺序调用控制器、模块（如果控制器属于模块）、应用主体的 afterAction() 方法
	- 应用主体获取操作结果并赋值给响应

##### 其他地方渲染视图
	#在任何地方都可以通过表达式 Yii::$app->view 访问 view 应用组件
	echo \Yii::$app->view->renderFile('@app/views/site/about.php');
	

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
	#一般继承基类小部件

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

