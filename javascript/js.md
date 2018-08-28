#### js调用php代码(文件为php扩展名)
~~~
#文件头可引入Yii框架类
<script type="text/javascript">
    var csrftoken="<?php echo Yii::$app->request->csrfToken;?>";
    console.log(csrftoken);
</script>
~~~


#### 判断页面是否有滚动条
[阅读原文](https://www.cnblogs.com/nzbin/p/8117535.html "https://www.cnblogs.com/nzbin/p/8117535.html")
~~~javascript
function hasScrollbar() {
    return document.body.scrollHeight > (window.innerHeight || document.documentElement.clientHeight);
}
~~~

#### 计算滚动条宽度的方法(未验证)
~~~javascript
function getScrollbarWidth() {

    var scrollDiv = document.createElement("div");
    scrollDiv.style.cssText = 'width: 99px; height: 99px; overflow: scroll; position: absolute; top: -9999px;';
    document.body.appendChild(scrollDiv);
    var scrollbarWidth = scrollDiv.offsetWidth - scrollDiv.clientWidth;
    document.body.removeChild(scrollDiv);

    return scrollbarWidth;

}
~~~