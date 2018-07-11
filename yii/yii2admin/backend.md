## 后台目录

#### 定义超级管理员
    backend/config/params.ph
    <!-- 指定admin属性的uid值,即为超级管理员,不需要rbac权限检查 -->

#### 后台系统设置>>网站设置
    对应db表:yii2_config
    通常在BaseController控制器的init构造函数中转化,并存入Yii::$app->params['web']中
    use backend\models\Config;
    Yii::$app->params['web'] = Config::lists();

#### 后台控制器
    backend/controllers/*
    控制器继承BaseController再继承common\core\Controller再继承\yii\web\Controller

#### 后台控制器(BaseController)的通用方法
    - function saveRow($model, $data)
    - function delRow($model, $pk = 'id')
    - function error($message = '', $jumpUrl = '', $ajax = false)
    - function success($message = '', $jumpUrl = '', $ajax = false)
    - function setForward()
    - function getForward($default = '')

#### 后台图片上传
    使用backend/controllers/PublicController控制器
    结合Yii::$app->params['upload']生成图片路径
    也可以使用common/helpers/Html::src()方法生成图片路径

#### 后台(首页)入口代码跟踪记录
~~~
- require()       /data/www/yii/backend/views/layouts/main.php:12
- require()       /data/www/yii/backend/views/index/index.php:5
- yii\web\View->renderPhpFile() /data/www/yii/vendor/yiisoft/yii2/base/View.php:348
- yii\web\View->renderFile() /data/www/yii/vendor/yiisoft/yii2/base/View.php:257
- yii\web\View->render() /data/www/yii/vendor/yiisoft/yii2/base/View.php:156
- backend\controllers\IndexController->renderContent() /data/www/yii/vendor/yiisoft/yii2/base/Controll
- backend\controllers\IndexController->render() /data/www/yii/vendor/yiisoft/yii2/base/Controller.
- backend\controllers\IndexController->actionIndex() /data/www/yii/backend/controllers/IndexContro
- call_user_func_array:{/data/www/yii/vendor/yiisoft/yii2/base/InlineAction.php:57}() /data/www/yi
- yii\base\InlineAction->runWithParams() /data/www/yii/vendor/yiisoft/yii2/base/InlineAction.php:5
- backend\controllers\IndexController->runAction() /data/www/yii/vendor/yiisoft/yii2/base/Controll
- yii\web\Application->runAction() /data/www/yii/vendor/yiisoft/yii2/base/Module.php:528
- yii\web\Application->handleRequest() /data/www/yii/vendor/yiisoft/yii2/web/Application.php:103
- yii\web\Application->run() /data/www/yii/vendor/yiisoft/yii2/base/Application.php:386
- {main}          /data/www/yii/backend/web/index.php:24
~~~

#### 修改后台模版(框架)页面
    <!-- 整体框架 -->
    backend\views\layouts\main.php
    <!-- 导航菜单 -->
    backend\views\layouts\public\menu.php
    <!-- 侧边导航 -->
    backend\views\layouts\public\menu-sub.php
    <!-- 消息通知 -->
    backend\views\layouts\public\notice.php
    <!-- 框架颜色搭配 -->
    backend\views\layouts\public\setting.php