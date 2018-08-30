## a标签

#### 点击事件
~~~
<!-- 常用 W3C标准不推荐在href里面执行javascript语句 -->
a href="javascript:js_method();"
<!-- 常用且周全 -->
a href="javascript:void(0);" onclick="js_method()"
<!-- 常用 区别只是执行了一条空的js代码 -->
a href="javascript:;" onclick="js_method()"
<!-- 用这种方法点击后网页返回到页面的最顶端 -->
a href="#" onclick="js_method()"
<!-- 页面不发生跳转 -->
a href="#" onclick="js_method();return false;"
~~~