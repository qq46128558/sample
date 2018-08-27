## render

#### 渲染php视图文件(带布局)
    // 渲染:端(backend)/views/控制器(index)/index.php
    return $this->render('index');

#### 渲染指定扩展名(html)的视图文件(带布局)
    // 渲染:端(backend)/views/控制器(index)/index.html
    return $this->render('index.html');

#### 后台入口渲染文件顺序
    Rendering view file: /data/www/yii/backend/views/index/index.php
    Rendering view file: /data/www/yii/backend/views/layouts/main.php
    Rendering view file: /data/www/yii/backend/views/layouts/public/menu.php
    Rendering view file: /data/www/yii/backend/views/layouts/public/notice.php
    Rendering view file: /data/www/yii/backend/views/layouts/public/menu-sub.php
    Rendering view file: /data/www/yii/backend/views/layouts/public/menu-mobile.php
    Rendering view file: /data/www/yii/backend/views/layouts/public/setting.php

#### 渲染指定文件(无布局)
    return $this->renderFile('@backend/views/index/index.php');


#### 后台渲染文件的流程
1. 控制器中调用render(基类的)方法: backend\controllers\IndexController->render() 
    - vendor/yiisoft/yii2/base/Controller.php
    - public function render($view, $params = [])

2. 跳入view的render方法,并渲染出$content: yii\web\View->render()
    - 先查找(传入的)视图文件: findViewFile() (protected)
    - 然后对文件渲染: yii\web\View->renderFile() 
    - 得到$content
    - vendor/yiisoft/yii2/base/View.php
    - public function render($view, $params = [], $context = null)
    - protected function findViewFile($view, $context = null)
    - public function renderFile($viewFile, $params = [], $context = null

3. 返回控制器,调用renderContent方法: backend\controllers\IndexController->renderContent()
    - 查找布局文件: findLayoutFile()
    - 对布局文件进行渲染,同时传入上一步得到的$content: yii\web\View->renderFile()
    - vendor/yiisoft/yii2/base/Controller.php
    - public function renderContent($content)
    - public function findLayoutFile($view)
        - 此处由$this->layout(即控制器中的public $layout)控制是否渲染布局文件

4. 跳入view的renderFile方法,得到$content: yii\web\View->renderFile()
5. 完成渲染,得到结果
    - 此处的$content就是: 布局文件+传入的文件
6. 总结:
    - render()渲染: 传入文件+布局文件(其中布局文件中将合并传入的$content)
    - renderFile渲染: 传入文件

#### 页面不使用默认的布局(不使用模版)
    在控制器中增加
    public $layout = false;

