# flow 流加载

该模块包含信息流加载和图片懒加载两大核心支持，无论是对服务端、还是前端体验，都有非常大的性能帮助。

## 使用

	layui.use('flow', function(){
	  var flow = layui.flow;
	  //信息流
	  flow.load(options);
	  
	  //图片懒加载
	  flow.lazyimg(options);
	});

## 信息流

信息流即异步逐页渲染列表元素，这是你页面已经存在的一段列表，你页面初始时只显示了6个

~~html
<ul id="demo">
  <li>1</li>
  <li>2</li>
  ……
  <li>6</li>
</ul>
~~~

你想通过加载更多来显示余下列表，那么你只需要执行方法：flow.load(options) 即可

~~~javascript
layui.use('flow', function(){
  var $ = layui.jquery; //不用额外加载jQuery，flow模块本身是有依赖jQuery的，直接用即可。
  var flow = layui.flow;
  flow.load({
    elem: '#demo' //指定列表容器
    ,done: function(page, next){ //到达临界点（默认滚动触发），触发下一页
      var lis = [];
      //以jQuery的Ajax请求为例，请求下一页数据（注意：page是从2开始返回）
      $.get('/api/list?page='+page, function(res){
        //假设你的列表返回在data集合中
        layui.each(res.data, function(index, item){
          lis.push('<li>'+ item.title +'</li>');
        }); 
        
        //执行下一页渲染，第二参数为：满足“加载更多”的条件，即后面仍有分页
        //pages为Ajax返回的总页数，只有当前页小于总页数的情况下，才会继续出现加载更多
        next(lis.join(''), page < res.pages);    
      });
    }
  });
});
~~~

## 基础参数

~~html
elem	string	指定列表容器的选择器

scrollElem	string	滚动条所在元素选择器，默认document。如果你不是通过窗口滚动来触发流加载，而是页面中的某一个容器的滚动条，那么通过该参数指定即可。

isAuto	boolean	是否自动加载。默认true。如果设为false，点会在列表底部生成一个“加载更多”的button，则只能点击它才会加载下一页数据。

end	string	用于显示末页内容，可传入任意HTML字符。默认为：没有更多了

isLazyimg	boolean	是否开启图片懒加载。默认false。如果设为true，则只会对在可视区域的图片进行按需加载。但与此同时，在拼接列表字符的时候，你不能给列表中的img元素赋值src，必须要用lay-src取代,如:
layui.each(res.data, function(index, item){
  lis.push('<li><img lay-src="'+ item.src +'"></li>');
});   
        

mb	number	与底部的临界距离，默认50。即当滚动条与底部产生该距离时，触发加载。注意：只有在isAuto为true时有效。
额，等等。。mb=margin-bottom，可不是骂人的呀。

done	function	到达临界点触发加载的回调。信息流最重要的一个存在。携带两个参数
done: function(page, next){
  //请注意：layui 1.0.5 之前的版本是从第2页开始返回，也就是说你的第一页数据并非done来触发加载
  （为之前这个愚蠢的设计表示抱歉）
  //从 layui 1.0.5 的版本开始，page是从1开始返回，初始时即会执行一次done回调。
  //console.log(page) //获得当前页
  
  //执行下一页渲染，第二参数为：满足“加载更多”的条件，即后面仍有分页
  //只有当前页小于总页数的情况下，才会继续出现加载更多
  next('列表HTML片段', page < res.pages); 
}
~~~

## 图片懒加载

应该说比当前市面上任何一个懒加载的实现都更为强劲和轻量，她用不足80行代码巧妙地提供了一个始终加载当前屏图片的高性能方案（无论上滑还是下滑）。对你的网站因为图片可能带来的压力，可做出很好的应对。

	flow.lazyimg(options)

	layui.use('flow', function(){
	  var flow = layui.flow;
	  //当你执行这样一个方法时，即对页面中的全部带有lay-src的img元素开启了懒加载（当然你也可以指定相关img）
	  flow.lazyimg(); 
	});

	<img lay-src="aaa.jpg"> 
	<img src="bbb.jpg" alt="該图不会懒加载">
	<img lay-src="ccc.jpg">    

图片懒加载的使用极其简单，其参数（options对象）可支持的key如下表所示：

elem	string	指定开启懒加载的img元素选择器，如 elem: '.demo img' 或 elem: 'img.load'

scrollElem	string	滚动条所在元素选择器，默认document。如果你不是通过窗口滚动来触发流加载，而是页面中的某一个容器的滚动条，那么通过该参数指定即可。
