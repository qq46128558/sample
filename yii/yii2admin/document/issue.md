## Yii2Admin 问题记录

### 后台

#### 翻页后点击行动作(如删除),无提示框,直接显示JSON
~~~
触发提示框显示的代码由JS控制: common/metronic/other/js/common.js
发现翻页后,无加载common.js
再次刷新后则加载common.js正常

解决:
view对应页面(index.php),body中删除对应代码即可
<?php \yii\widgets\Pjax::begin(['options'=>['id'=>'pjax-container']]); ?>
<?php \yii\widgets\Pjax::end(); ?>

原因:
pjax导致了js失效
~~~