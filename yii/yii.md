

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

##### 错误处理
	#使用错误处理器
	use yii\base\ErrorException;
	try{}
	catch(ErrorException $e){}

	#自定义错误显示
	#error handler 错误处理器默认使用两个视图显示错误
	#PRD
	@yii/views/errorHandler/error.php
	#DEV
	@yii/views/errorHandler/exception.php
	#可以配置错误处理器的 errorView 和 exceptionView 属性 使用自定义的错误显示视图

	#使用错误动作
	#使用指定的错误操作 来自定义错误显示更方便
	#配置errorHandler组件
	'errorAction' => 'site/error',
		controllers/SiteController.php
			actions()
				'error'
					yii\web\ErrorAction
	vendor\yiisoft\yii2\web\ErrorAction.php
	#上述代码定义error 操作使用yii\web\ErrorAction 类， 该类渲染名为error视图来显示错误

	#除了使用yii\web\ErrorAction, 可定义error 动作使用类似如下的操作方法：
	$exception = Yii::$app->errorHandler->exception;


##方法
---------------------------
##### 获取版本
    Yii::getVersion();

##### 日志
	vendor\yiisoft\yii2\base\log\
	Yii::trace("Action '{$action->uniqueId}' spent $time second.");
	Yii::info();
	Yii::warning();
	#2018-03-16 05:41:16 [::1][-][-][error][application] XXX
	#Timestamp [IP address][User ID][Session ID][Severity Level][Category] Message Text
	Yii::error('XXX');
	#假如一条日志消息不是一个字符串，它将被导出为一个字符串，通过调用 yii\helpers\VarDumper::export()

	#它们共享相同的函数签名 function ($message, $category = 'application')
	#建议使用PHP魔术常量 __METHOD__ 作为分类名称
	Yii::trace('start calculating average revenue', __METHOD__);

	#日志目标
	#通过配置在应用配置里的 log application component ，你可以注册多个日志目标
	#保存日志消息到文件中
		'class'=>'yii\log\FileTarget',
		'levels' => ['error', 'warning'],

	#日志文件
		runtime/log/app.log

	#消息格式化
	#通过配置 yii\log\Target::$prefix 的属性来自定义格式

	#性能分析
	#levels profile：相应的消息通过 Yii::beginProfile() 和 Yii::endProfile() 被记录。
		\Yii::beginProfile('myBenchmark');
			...code block being profiled...
		\Yii::endProfile('myBenchmark');


##### 将驼峰式大小写变量名转换为多个首字母大写的单词
	use yii\helpers\Inflector;
	echo Inflector::camel2words("helloWorld", true);

##### 从config.php加载配置来初始化模块
	\Yii::configure($this, require(__DIR__ . '/config.php'));




##模型/控制器/视图/模块方法
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

##### 使用视图布局文件
	#配置yii\base\Application::$layout 或 yii\base\Controller::$layout 
	#前者管理所有控制器的布局，后者覆盖前者来控制单个控制器布局
	public $layout = 'post';

##### 其他地方渲染视图
	#在任何地方都可以通过表达式 Yii::$app->view 访问 view 应用组件
	echo \Yii::$app->view->renderFile('@app/views/site/about.php');

##### 视图中访问数据
	#推送
	echo $this->render('report', [
		'foo' => 1,
		'bar' => 2,
	]);
	#拉取 $this->context
	<?= $this->context->id ?>

##### 嵌套布局
	<?php $this->beginContent('@app/views/layouts/base.php'); ?>
		...child layout content here...
	<?php $this->endContent(); ?>

##### 使用数据块
	#内容视图
	<?php $this->beginBlock('block1'); ?>
		...content of block1...
	<?php $this->endBlock(); ?>
	#布局视图
	<?php if (isset($this->blocks['block1'])): ?>
		<?= $this->blocks['block1'] ?>
	<?php else: ?>
		... default content for block1 ...
	<?php endif; ?>

##### 模块目录结构
	forum/
		Module.php                   模块类文件
		controllers/                 包含控制器类文件
			DefaultController.php    default 控制器类文件
		models/                      包含模型类文件
		views/                       包含控制器视图文件和布局文件
			layouts/                 包含布局文件
			default/                 包含DefaultController控制器视图文件
				index.php            index视图文件

##### 访问模块
	#getInstance() 方法返回当前请求的模块类实例， 如果模块没有被请求，该方法会返回空
	$module = yii\gii\Module::getInstance();
	var_dump($module);

	#获取ID为 "forum" 的模块
	$module = \Yii::$app->getModule('forum');
	#获取处理当前请求控制器所属的模块
	$module = \Yii::$app->controller->module;

##### 模块嵌套
	$this->modules = [
            'admin' => [
                // 此处应考虑使用一个更短的命名空间
                'class' => 'app\modules\forum\modules\admin\Module',
            ],
        ];

##### 使用过滤器
	#覆盖 yii\base\Controller::behaviors() 方法声明过滤器
	#配置only属性明确指定控制器应用到哪些动作
	#除了控制器外，可在 模块或应用主体 中申明过滤器。 申明之后，过滤器会应用到所属该模块或应用主体的 所有 控制器动作
	#继承 yii\base\ActionFilter 类并覆盖 beforeAction() 或 afterAction() 方法来创建动作的过滤器，前者在动作执行之前执行，后者在动作执行之后执行。 beforeAction() 返回值决定动作是否应该执行， 如果为 false，之后的过滤器和动

##### 核心过滤器
	#Yii 提供了一组常用过滤器，在 yii\filters 命名空间下
	vendor/yiisoft/yii2/filters/


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
	#vendor\yiisoft\yii2\web\Request.php
	#继承\yii\base\Request再继承Component

##### 响应对象
	Yii::$app->response
	#vendor\yiisoft\yii2\web\Response.php
	#设置响应格式
	\Yii::$app->response->format = \yii\web\Response::FORMAT_JSON;
	#调用 yii\web\Response::send() 方法来确保没有其他内容追加到响应中
	\Yii::$app->response->redirect('http://example.com/new', 301)->send();
	#一旦yii\web\Response::send() 方法被执行后，其他地方调用该方法会被忽略， 这意味着一旦响应发出后，就不能再追加其他内容
	
##### Redis对象
	Yii::$app->redis

##### Sessions
	Yii::$app->session

##### Cookies
	Yii::$app->request->cookies
	Yii::$app->response->cookies
	#cookieValidationKey 对你的应用安全很重要， 应只被你信任的人知晓，请不要将它放入版本控制中。
	#当通过 request 和 response 组件读取和发送 cookie 时， 你会喜欢扩展的 cookie 验证的保障安全功能，它能 使 cookie 不被客户端修改。该功能通过给每个cookie签发一个哈希字符串来告知服务端 cookie 是否在客户端被修改， 如果被修改，通过 request 组件的 yii\web\Request::cookies cookie 集合访问不到该 cookie。
	
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

##### 视图路径
	#yii\base\Application::viewPath 
	Yii::$app->viewPath;
	#模块的视图路径
	#yii\base\Module::viewPath
	use app\modules\api\Api;
	$modules=new Api('xxx');
	echo $modules->viewPath;

##### 视图布局路径
	#yii\base\Application::layoutPath
	Yii::$app->layoutPath;
	#配置yii\base\Module::layoutPath来自定义应用或模块的布局默认路径

##### 视图布局文件
	Yii::$app->layout;

##### 获取ID为 "forum" 的模块
	$module = \Yii::$app->getModule('forum');

##### 获取处理当前请求控制器所属的模块
	$module = \Yii::$app->controller->module;



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

##### 基类小部件
	use yii\base\Widget
	vendor/yiisoft/yii2/base/Widget.php
	#继承组件

##### 基类过滤器
	use yii\base\ActionFilter
	vendor/yiisoft/yii2/base/ActionFilter.php
	#继承Behavior再继承BaseObject

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

##### 扩展清单文件
	vendor/yiisoft/extensions.php

##### 入口文件
	#web应用
	web/index.php
	#控制台应用
	yii

