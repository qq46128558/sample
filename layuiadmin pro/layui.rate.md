# rate 评分组件

## 使用

	<div id="test1"></div>
	<script>
	  layui.use('rate', function(){
	    var rate = layui.rate;
	   
	    //渲染
	    var ins1 = rate.render({
	      elem: '#test1'  //绑定元素
	    });
	  });
	</script>

## 基础参数

~~~html
elem	指向容器选择器	string/object	-

length	评分组件中具体星星的个数。个数当然是整数啦，残缺的星星很可怜的，所以设置了小数点的组件我们会默认向下取整	number	5

value	评分的初始值	number	0

theme	主题颜色。我们默认的组件颜色是#FFB800，你可以根据自身喜好来更改组件的颜色，以适用不同场景	string	#FFB800

half	设定组件是否可以选择半星	boolean	false

text	是否显示评分对应的内容	boolean	false

readonly	是否只读，即只用于展示而不可点	boolean	false
~~~

## 自定义文本的回调

通过 setText 函数，在组件初次渲染和点击后时产生回调

	rate.render({
	  elem: '#test1'
	  ,setText: function(value){
	    var arrs = {
	      '1': '极差'
	      ,'2': '差'
	      ,'3': '中等'
	      ,'4': '好'
	    };
	    this.span.text(arrs[value] || ( value + "星"));
	  }
	});

当你点击 3 星时，文本内容是中等，点击 5 星时，由于没有设定对应文字，所以文本会显示 5 星

## 点击产生的回调

通过 choose 实现函数，在组件被点击后触发，回调分数，用户可根据分数来设置效果，比如出现弹出层

	rate.render({
	  elem: '#test1'
	  ,choose: function(value){
	    if(value > 4) alert( '么么哒' )
	  }
	});

