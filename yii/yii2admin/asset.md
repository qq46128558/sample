## 前端资源


#### 后台页面注册前端资源流程(记录)
~~~php
1. 入口: 
backend/views/layouts/main.php 视图文件

2. 注册资源文件: 
// Registers this asset bundle with a view
AppAsset::register($this); // vendor/yiisoft/yii2/web/AssetBundle.php
- 再调用:
// get_called_class() => backend\assets\AppAsset
$view->registerAssetBundle(get_called_class()); // vendor/yiisoft/yii2/web/View.php
- 过程中调用到:
// src: /data/www/yii/common/metronic
// 返回$dir: backend/web/assets/c68869b8
protected function publishFile($src) // vendor/yiisoft/yii2/web/AssetManager.php
    $dir = $this->hash($src);
- 上面就是资源目录backend/web/assets/c68869b8产生的源头,也可以页面上ctrl+u查看源码

3. 注册依赖的资源文件
依赖来源: backend\assets\AppAsset.php >> public $depends
'backend\assets\IeAsset',
'backend\assets\CoreAsset',

4. 使用哪些css与js
即资源文件中的 $css 与 $js
>> 此时尚未渲染到页面

5. view类的一些标记功能(未知作用)
$this->beginPage(); // vendor/yiisoft/yii2/base/View.php

6. 写上css资源标记
<?php $this->head() ?> // vendor/yiisoft/yii2/web/View.php
<![CDATA[YII-BLOCK-HEAD]]>

7. 写标记(未知作用)
<?php $this->beginBody() ?> // vendor/yiisoft/yii2/web/View.php
<![CDATA[YII-BLOCK-BODY-BEGIN]]>

8. 再注册一个资源文件
<?php \backend\assets\LayoutAsset::register($this); ?> // vendor/yiisoft/yii2/web/AssetBundle.php

9. 写上js资源标记同时注册资源文件中的$css与$js
<?php $this->endBody() ?> // vendor/yiisoft/yii2/web/View.php
<![CDATA[YII-BLOCK-BODY-END]]>
// Registers all files provided by an asset bundle including depending bundles files.
$this->registerAssetFiles($bundle);

10. 页面结束标记并替换资源标记为资源文件路径
<?php $this->endPage() ?> // vendor/yiisoft/yii2/web/View.php
echo strtr($content, [
    self::PH_HEAD => $this->renderHeadHtml(), // <![CDATA[YII-BLOCK-HEAD]]> $css
    self::PH_BODY_BEGIN => $this->renderBodyBeginHtml(), // <![CDATA[YII-BLOCK-BODY-BEGIN]]> 未知
    self::PH_BODY_END => $this->renderBodyEndHtml($ajaxMode), // <![CDATA[YII-BLOCK-BODY-END]]> $js
]);

11. 最终效果
asset: 'layouts/layout/css/layout.min.css',
css:
<link href="/admin/assets/c68869b8/layouts/layout/css/layout.min.css" rel="stylesheet">

asset: 'global/plugins/jquery.min.js',
js:
<script src="/admin/assets/c68869b8/global/plugins/jquery.min.js"></script>

/admin/assets/c68869b8
对应目录是:
backend/web/assets/c68869b8

12. 一些总结
- backend/web/assets/c68869b8/.... 内容不上传git
    (经验证c68869b8可以直接删除,然后清除缓存,刷新后会自动重新生成)
- asset文件中配置的资源文件前缀目录是: common/metronic/
- 修改资源应修改此目录内文件: common/metronic/
~~~