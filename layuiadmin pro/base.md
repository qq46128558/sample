# layui

[layui文档][layui]
[layuiAdmin pro v1.x 【单页版】开发者文档][admin]
[layuiAdmin pro 在线演示][adminpro]
[layui 实用干货和常见问题的处理][faq]
[layui 示例][demo]

[layui]: https://www.layui.com/doc/ "https://www.layui.com/doc/"
[admin]: https://fly.layui.com/docs/5/ "https://fly.layui.com/docs/5/"
[adminpro]: https://www.layui.com/admin/pro/ "https://www.layui.com/admin/pro/"
[faq]: https://fly.layui.com/jie/5366/ "https://fly.layui.com/jie/5366/"
[demo]: https://www.layui.com/demo/ "https://www.layui.com/demo/"

## 模块定义

~~~javascript
//layui模块的定义
layui.define([mods], function(exports){
  
  //……
  
  exports('mod', api);
});  

// layui.define([mods], callback)
// 参数mods是可选的，用于声明该模块所依赖的模块
// callback即为模块加载完毕的回调函数，它返回一个exports参数，用于输出该模块的接口
// exports是一个函数，它接受两个参数，第一个参数为模块名，第二个参数为模块接口
// 当你声明了上述的一个模块后，你就可以在外部使用了，mod就会注册到layui对象下，即可通过 layui.mod() 去执行该模块的接口。
~~~

## 模块使用

方法：layui.use([mods], callback)

~~~javascript
//layui模块的使用
layui.use(['mod1', 'mod2'], function(args){
  var mod = layui.mod1;
  
  //……
  
});  

// 它的参数跟上述的 define方法完全一样
// mods里面必须是一个合法的模块名，不能包含目录
// 如果需要加载目录，建议采用extend建立别名

// 该方法的函数其实返回了所加载的模块接口，所以你其实也可以不通过layui对象赋值获得接口
layui.use(['laypage', 'layedit'], function(laypage, layedit){
  //使用分页
  laypage();
  //建立编辑器
  layedit.build();
});
~~~

## 模块化的用法

~~~javascript
layui.config({
  base: '/res/js/modules/' //你存放新模块的目录，注意，不是layui的模块目录
}).use('index'); //加载入口

/**
  项目JS主入口
  以依赖layui的layer和form模块为例
**/    
layui.define(['layer', 'form'], function(exports){
  var layer = layui.layer
  ,form = layui.form;
  
  layer.msg('Hello World');
  
  exports('index', {}); //注意，这里是模块输出的核心，模块名必须和use时的模块名一致
});    
~~~

## 全局配置

~~~javascript
layui.config({
  dir: '/res/layui/' //layui.js 所在路径（注意，如果是script单独引入layui.js，无需设定该参数。），一般情况下可以无视
  ,version: false //一般用于更新模块缓存，默认不开启。设为true即让浏览器不缓存。也可以设为一个固定的值，如：201610
  ,debug: false //用于开启调试模式，默认false，如果设为true，则JS模块的节点会保留在页面
  ,base: '' //设定扩展的Layui模块的所在目录，一般用于外部模块扩展
});
~~~

## 动态加载CSS

方法：layui.link(href)

href即为css路径

## 本地存储

其中参数 table 为表名，settings是一个对象，用于设置key、value。

- localStorage 持久化存储：layui.data(table, settings)，数据会永久存在，除非物理删除。
- sessionStorage 会话性存储：layui.sessionData(table, settings)，页面关闭后即失效。注：layui 2.2.5 新增

~~~javascript
//【增】：向test表插入一个nickname字段，如果该表不存在，则自动建立。
layui.data('test', {
  key: 'nickname'
  ,value: '贤心'
});
 
//【删】：删除test表的nickname字段
layui.data('test', {
  key: 'nickname'
  ,remove: true
});
layui.data('test', null); //删除test表
  
//【改】：同【增】，会覆盖已经存储的数据
  
//【查】：向test表读取全部的数据
var localTest = layui.data('test');
console.log(localTest.nickname); //获得“贤心”
~~~

## 获取设备信息

方法：layui.device(key)，参数key是可选的

~~~javascript
var device = layui.device();
//device即可根据不同的设备返回下述不同的信息
{
  os: "windows" //底层操作系统，windows、linux、mac等
  ,ie: false //ie6-11的版本，如果不是ie浏览器，则为false
  ,weixin: false //是否微信环境
  ,android: false //是否安卓系统
  ,ios: false //是否ios系统
}
~~~

有时你的App可能会对userAgent插入一段特定的标识，譬如： 
Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 **myapp/1.8.6** Safari/537.36

你要验证当前的WebView是否在你的App环境，即可通过上述的myapp（即为Native给Webview插入的标识，可以随意定义）来判断。

~~~javascript
var device = layui.device('myapp');
if(device.myapp){
  alert('在我的App环境');
}    
~~~

## 其他底层引擎

~~~html
方法/属性	描述
layui.cache	静态属性。获得一些配置及临时的缓存信息
layui.extend(options)	拓展一个模块别名，如：layui.extend({test: '/res/js/test'})
layui.each(obj, fn)	对象（Array、Object、DOM对象等）遍历，可用于取代for语句
layui.getStyle(node, name)	获得一个原始DOM节点的style属性值，如：layui.getStyle(document.body, 'font-size')
layui.img(url, callback, error)	图片预加载
layui.sort(obj, key, desc)	将数组中的对象按某个成员重新对该数组排序，如：layui.sort([{a: 3},{a: 1},{a: 5}], 'a')
layui.router()	获得location.hash路由，目前在Layui中没发挥作用。对做单页应用会派上用场。
layui.hint()	向控制台打印一些异常信息，目前只返回了error方法：layui.hint().error('出错啦')
layui.stope(e)	阻止事件冒泡
layui.onevent(modName, events, callback)	自定义模块事件，属于比较高级的应用。有兴趣的同学可以阅读layui.js源码以及form模块
layui.event(modName, events, params)	执行自定义模块事件，搭配onevent使用
layui.factory(modName)	用于获取模块对应的 define 回调函数
~~~

## 模块命名空间

我们推荐你将所有的业务代码都写在一个大的 use 回调中，而不是将模块接口暴露给全局，比如下面的方式我们是极不推荐的：

~~~javascript
//强烈不推荐下面的做法
var laypage, laydate;
layui.use(['laypage', 'laydate'], function(){
  laypage = layui.laypage;
  laydate = layui.laydate;
});
~~~

你之所以想使用上面的错误方式，是想其它地方使用不在执行一次 layui.use？但这种理解本身是存在问题的。因为如果一旦你的业务代码是在模块加载完毕之前执行，你的全局对象将获取不到模块接口，因此这样用不仅不符合规范，还存在报错风险。建议在你的 js 文件中，在最外层写一个 layui.use 来加载所依赖的模块，并将业务代码写在回调中

事实上，如果你不想采用 layui.use，你可以引入 layui.all.js 来替代 layui.js

## 如何使用内部jQuery？

由于Layui部分内置模块依赖jQuery，所以我们将jQuery1.11最稳定的一个版本作为一个内置的DOM模块（唯一的一个第三方模块）。只有你所使用的模块有依赖到它，它才会加载，并且如果你的页面已经script引入了jquery，它并不会重复加载。内置的jquery模块去除了全局的$和jQuery，是一个符合layui规范的标准模块。所以你必须通过以下方式得到：

~~~javascript
//主动加载jquery模块
layui.use(['jquery', 'layer'], function(){ 
  var $ = layui.$ //重点处
  ,layer = layui.layer;
  
  //后面就跟你平时使用jQuery一样
  $('body').append('hello jquery');
});
 
//如果内置的模块本身是依赖jquery，你无需去use jquery，所以上面的写法其实可以是：
layui.use('layer', function(){ 
  var $ = layui.$ //由于layer弹层依赖jQuery，所以可以直接得到
  ,layer = layui.layer;
 
  //……
});
~~~

