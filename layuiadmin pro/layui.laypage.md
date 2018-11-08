# laypage 分页模块

## 快速使用

~~~javascript
<div id="test1"></div>
<script>
layui.use('laypage', function(){
  var laypage = layui.laypage;
  //执行一个laypage实例
  laypage.render({
    elem: 'test1' //注意，这里的 test1 是 ID，不用加 # 号
    ,count: 50 //数据总数，从服务端得到
  });
});
</script>
~~~

## 基础参数

|参数|说明|类型|默认值
|-|-|-|-
|elem|指向存放分页的容器,id不能加#|string/object|-
|count|数据总数。一般通过服务端得到|number|-
|limit|每页显示的条数|number|10
|limits|每页条数的选择项(layout 参数开启了 limit)|array|[10,20,30]
|curr|起始页|number|1
|groups|连续出现的页码个数|number|5
|prev|自定义“上一页”的内容，支持传入普通文本和HTML|string|上一页
|next|同上|string|下一页
|first|同上|string|1
|last|同上|string|总页数值
|layout|自定义排版 可选值有：count（总条目输区域）、prev（上一页区域）、page（分页区域）、next（下一页区域）、limit（条目选项区域）、refresh（页面刷新区域。注意：layui 2.3.0 新增） 、skip（快捷跳页区域）|array|['prev', 'page', 'next']
|theme|自定义主题|string|-
|hash|开启location.hash，并自定义 hash 值,如果开启，在触发分页时，会自动对url追加：#!hash值={curr} 利用这个，可以在页面载入时就定位到指定页|string/boolean|false

## jump - 切换分页的回调

当分页被切换时触发，函数返回两个参数：obj（当前分页的所有选项值）、first（是否首次，一般用于初始加载的判断）

~~~javascript
laypage.render({
  elem: 'test1'
  ,count: 70 //数据总数，从服务端得到
  ,jump: function(obj, first){
    //obj包含了当前分页的所有参数，比如：
    console.log(obj.curr); //得到当前页，以便向服务端请求对应页的数据。
    console.log(obj.limit); //得到每页显示的条数
    
    //首次不执行
    if(!first){
      //do something
    }
  }
});
~~~

**laypage 只负责分页本身的逻辑，具体的数据请求与渲染需要另外去完成**

