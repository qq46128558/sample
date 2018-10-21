# table 数据表格

## 快速使用

- 绑定容器
- 设置数据接口
	- {"code":0,"msg":"",count:1000,"data":[{"id":1,"username":"user-0"},{"id":2,"username":"user-1"}]}
- 在表头设定对应的字段

~~~html
<table id="demo" lay-filter="test"></table>
<script>
layui.use('table',function(){
	var table=layui.table;
	table.render({
		elem:'#demo'
		,height:312
		,url:'/demo/table/user/' //数据接口
		,page:true //开启分页
		,cols:[[ //表头(两个数组是为了可实现跨行跨列的表格)
			{field:'id',title:'ID',width:80,sort:true,fixed:'left'}
			,{field:'username',title:'用户名',width:80}
			,...
		]]
	});
});
</script>
~~~

> table.render()方法返回一个对象,可用于表格重载

## 方法渲染(推荐)

快速使用的示例即为方法渲染的方式(无需写过多的html)

## 自动渲染

无需写过多js,可专注于html表头部份

~~~html
<!-- lay-data内对象的值要用单引号 -->
<table class="layui-table" lay-data="{height:315,url:'/demo/table/user/',page:true,id:'test'}" lay-filter="test">
	<thead>
		<tr>
			<th lay-data="{field:'id',width:80,sort:true}">ID</th>
			<th lay-data="{field:'username',width:80}">用户名</th>
			...
		</tr>
	</thead>
</table>

<script>
layui.use('table',function(){
	var table=layui.table;
});
</script>
~~~

## 转换静态表格

已有一段有内容的表格,无需配置数据接口,在js中指定表格元素,并给表头加上自定义属性(利于SEO)

## 基础参数

|参数|类型|说明
|-|-|-
|elem|string/dom|指定原始table容器的选择器或dom
|cols|array|设置表头
|url(等)|-|异步数据接口相关参数
|toolbar|string/dom/boolean|开启表格头部工具栏区域
|defaultToolbar|array|自由配置头部工具栏右侧的图标,['filter','print','exports']
|width|number|设定容器宽度
|height|number/string|设定容器高度
|cellMinWidth|number|全局定义常规单元格的最小宽度,60
|done|function|数据渲染完的回调
|data|array|直接赋值数据
|totalRow|boolean|是否开启合计行区域
|page|boolean/object|开启分页,false/laypage支持的参数
|limit|number|每页显示的条数,10
|limits|array|每页条数的选择项
|loading|boolean|是否显示加载条,true
|title|string|定义table的大标题,如导出时
|text|object|自定义文本
|initSort|object|初始排序状态
|id|string|设定容器唯一id
|skin(等)|-|设定表格各种外观,尺寸

## cols 表头参数一览表

|参数|类型|说明
|-|-|-
|field|string|设定字段名
|title|string|设定标题名
|width|number/string|设定列宽
|minWidth|number|当前常规单元格的最小宽度,60
|type|string|设定列类型,normal/checkbox/radio/numbers/space,normal
|LAY_CHECKED|boolean|是否全选状态,false
|fixed|string|固定列,left/right
|hide|boolean|是否初始隐藏列,false
|totalRow|boolean|是否开启该列的自动合计功能,false
|totalRowText|string|自定义的合计文本
|sort|boolean|是否允许排序,false
|unresize|boolean|是否禁用拖拽列宽,false
|edit|string|单元格编辑类型,text,默认不开启
|event|string|自定义单元格点击事件名
|style|string|自定义单元格样式
|align|string|单元格排序方式,left/center/right
|colspan|number|单元格所占列数,1
|rowspan|number|单元格所占行数,1
|templet|string|自定义列模板,如时间戳转化为日期字符
|toolbar|string|绑定工具条,自定义操作性按钮

## templet 自定义列模板(laytpl语法)

- 绑定模板选择器
	- cols:[[{field:'title',title:'文章标题',width:200,templet:'#titleTpl'}]]
	- <script type="text/html" id="titleTpl"><a href="/detail/{{d.id}}" class="layui-table-link">{{d.title}}</a></script>
- 函数转义
	- ,templet:function(d){return 'ID:'+d.id+',标题:<span style="color:#c00;">'+d.title+'</span>'}
- 直接赋值模板字符
	- 需要一层<div></div>包裹
	- ,templet:'<div><a href="/detail/{{d.id}}" class="layui-table-link">{{d.title}}</a></div>'

## toolbar 绑定列工具条
	
行上的查看,编辑,删除,与templet参数的使用方式完全类似

借助table模块的工具条事件,完成不同的操作功能

~~~javascript
// 监听工具条
table.on('tool(test)',function(obj){ // tool是工具条事件名,test是table原始容器的lay-filter
	var data=obj.data; //获得当前行数据
	var layEvent=obj.event; //获得lay-event对应的值
	var tr=obj.tr; //获得当前行tr的dom对象
	if (layEvent===='detail'){
		//...
	}
});
~~~

## 异步数据接口

|参数|功能
|-|-
|url|接口地址,默认自动传递两个参数:?page=1&limit=30
|method|接口http请求类型
|where|接口的其他参数
|contentType|发送到服务端的内容编码类型,contentType:'application/json'
|headers|接口的请求头
|parseData|数据预解析回调函数,function(res),res为原始返回数据
|request|用于对分页请求的参数重新设定名称,{pageName:'curr',limitName:'nums'}
|response|重新规定返回的数据格式

## done 数据渲染完的回调

	done:function(res,curr,count)

- res: 接口返回的信息
- curr: 当前页码
- count: 数据总量

## text 自定义文本

内置的一些默认文本信息
	
	text:{none:"暂无相关数据"} //默认是无数据

## initSort 初始排序

	initSort:{field:'id',type:'desc'}

## height 设定容器高度(不填写不出现纵向滚动条)

	height:'full-20' //高度最大化减去差值

## 设定表格外观
	
- skin,line/row/nob
- even,true/false
- size,sm/lg

## 基础方法

- table.set(options)
- table.on('event(filter)',callback)
- table.init(filter,options)
- table.checkStatus(id)
- table.render(options)
- table.exportFile(id,data,type)

### 获取选中行
	
	var checkStatus=table.checkStatus('test');
	checkStatus.data; //选中的行数据
	checkStatus.data.length; //选中的行数
	checkStatus.isAll; //是否全选

### 导出数据

	table.exportFile(tableIns.config.id,data) //data为该实例中任意数量的数据,默认csv,也可以为cls

## 事件临听

- 监听头部工具栏: table.on('toolbar(test)',function(obj){}) //obj.config.id/obj.event
- 监听复选框: table.on('checkbox(test)',function(obj){}) //obj.checked/.data/.type
- 监听单元格编辑: table.on('edit(test)',function(obj){}) //obj.value/.field/.data
- 监听行单击事件: table.on('row(test)',function(obj){}) //obj.tr/.data[obj.del(),obj.update(fields)]
- 监听行双击事件: table.on('rowDouble(test)',function(obj){})
- 监听行中工具条点击事件: table.on('tool(test)',function(obj){})
- 监听排序切换: table.on('sort(test)',function(obj){}) //obj.field/.type
	- 服务端排序需要用到table.reload和initSort参数

## 表格重载
	
比如数据全局搜索

	table.relaod(ID,options)
	tableIns.reload(options)

