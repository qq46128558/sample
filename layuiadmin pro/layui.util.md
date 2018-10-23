# util 工具集

其内部由多个小工具组件组成

## 固定块
	
	由两个可选的bar和一个默认必选的TopBar组成

	util.fixbar(options) 

options:

~~html
bar1	Boolean/String	默认false。如果值为true，则显示第一个bar，带有一个默认图标。
如果值为图标字符，则显示第一个bar，并覆盖默认图标

bar2	Boolean/String	默认false。如果值为true，则显示第二个bar，带有一个默认图标。
如果值为图标字符，则显示第二个bar，并覆盖默认图标

bgcolor	String	自定义区块背景色

showHeight	Number	用于控制出现TOP按钮的滚动条高度临界值。默认：200

css	Object	你可以通过重置bar的位置，比如 css: {right: 100, bottom: 100}

click	Function	点击bar的回调，函数返回一个type参数，用于区分bar类型。
支持的类型有：bar1、bar2、top
~~~

~~~javascript
layui.use('util', function(){
  var util = layui.util;
  
  //执行
  util.fixbar({
    bar1: true
    ,click: function(type){
      console.log(type);
      if(type === 'bar1'){
        alert('点击了bar1')
      }
    }
  });
});
~~~

## 倒计时

这是一个精致的封装，它并不负责 UI 元素的呈现，而仅仅只是返回倒计时的数据，这意味着你可以将它应用在任何倒计时相关的业务中。

	util.countdown(endTime, serverTime, callback)

- endTime	结束时间戳或Date对象，如：4073558400000，或：new Date(2099,1,1).
- serverTime	当前服务器时间戳或Date对象
- callback	回调函数。如果倒计时尚在运行，则每一秒都会执行一次。并且返回三个参数： date（包含天/时/分/秒的对象）、 serverTime（当前服务器时间戳或Date对象）, timer（计时器返回的ID值，用于clearTimeout）

~~~hmtl
<div id="test"></div>
 
<script>
layui.use('util', function(){
  var util = layui.util;
  
  //示例
  var endTime = new Date(2099,1,1).getTime() //假设为结束日期
  ,serverTime = new Date().getTime(); //假设为当前服务器时间，这里采用的是本地时间，实际使用一般是取服务端的
   
  util.countdown(endTime, serverTime, function(date, serverTime, timer){
    var str = date[0] + '天' + date[1] + '时' +  date[2] + '分' + date[3] + '秒';
    layui.$('#test').html('距离2099年1月1日还有：'+ str);
  });
});
</script>
~~~

## 其它方法

~~html
util.timeAgo(time, onlyDate)	某个时间在当前时间的多久前。 
参数 time：即为某个时间的时间戳或日期对象 
参数 onlyDate：是否在超过30天后，只返回日期字符，而不返回时分秒 
如果在3分钟以内，返回：刚刚 
如果在30天以内，返回：若干分钟前、若干小时前、若干天前，如：5分钟前 
如果在30天以上，返回：日期字符，如：2017-01-01

util.toDateString(time, format)	转化时间戳或日期对象为日期格式字符 
参数 time：可以是日期对象，也可以是毫秒数 
参数 format：日期字符格式（默认：yyyy-MM-dd HH:mm:ss），可随意定义，如：yyyy年MM月dd日

util.digit(num, length)	数字前置补零 
参数 num：原始数字 
参数 length：数字长度，如果原始数字长度小于 length，则前面补零，如：util.digit(7, 3) //007

util.escape(str)	转义 xss 字符 
参数 str：任意字符
~~~

