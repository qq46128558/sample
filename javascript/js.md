##### js调用php代码(文件为php扩展名)
~~~
#文件头可引入Yii框架类
<script type="text/javascript">
    var csrftoken="<?php echo Yii::$app->request->csrfToken;?>";
    console.log(csrftoken);
</script>
~~~