# upload 图片/文件上传

## 快速使用

~~~html
<button type="button" class="layui-btn" id="test1">
  <i class="layui-icon">&#xe67c;</i>上传图片
</button>
~~~~

~~~javascript
layui.use('upload', function(){
  var upload = layui.upload;
   
  //执行实例
  var uploadInst = upload.render({
    elem: '#test1' //绑定元素
    ,url: '/upload/' //上传接口
    ,done: function(res){
      //上传完毕回调
    }
    ,error: function(){
      //请求异常回调
    }
  });
});
~~~

## 核心方法与基础参数选项

	upload.render(options)

也可直接在元素上设定基础参数

	<button class="layui-btn test" lay-data="{url: '/a/'}">上传图片</button>
	<button class="layui-btn test" lay-data="{url: '/b/', accept: 'file'}">上传文件</button>
	upload.render({
	  elem: '.test'
	  ,done: function(res, index, upload){
	    //获取当前触发上传的元素，一般用于 elem 绑定 class 的情况，注意：此乃 layui 2.1.0 新增
	    var item = this.item;
	  }
	})

|参数选项|说明|类型
|-|-|-
|elem|指向容器选择器|string/object
|url|服务端上传接口|string
|data|请求上传接口的额外参数|data: {id: function(){return $('#id').val();}}|object
|headers|接口的请求头 headers: {token: 'sasasas'}|object
|accept|指定允许上传时校验的文件类型:images/file/video/audio|string,images
|acceptMime|规定打开文件选择框时，筛选出的文件类型，值为用逗号隔开的 MIME 类型列表,acceptMime: 'image/jpg, image/png'|string,images
|exts|允许上传的文件后缀,exts: 'zip丨rar丨7z'|string
|auto|是否选完文件后自动上传,如果设定 false，那么需要设置 bindAction 参数来指向一个其它按钮提交上传|boolean,true
|bindAction|指向一个按钮触发上传，一般配合 auto: false 来使用。值为选择器或DOM对象，如：bindAction: '#btn'|string/object
|field|设定文件域的字段名|string,file
|size|设置文件最大可允许上传的大小，单位 KB。不支持ie8/9|number,0
|multiple|是否允许多文件上传。设置 true即可开启。不支持ie8/9|boolean,false
|number|设置同时可上传的文件数量，一般配合 multiple 参数出现。|number,0
|drag|是否接受拖拽的文件上传，设置 false 可禁用。不支持ie8/9|boolean,true

### 回调

- choose: 选择文件后的回调函数
- before: 文件提交上传前的回调
- done: 执行上传请求后的回调
- error: 执行上传请求出现异常的回调

## 上传接口

设定一个 URL 地址给 url 参数，用来告诉 upload 模块的服务端上传接口。像你平时使用Ajax一样

~~~javascript
upload.render({
  elem: '#id'
  ,url: '/api/upload/' //必填项
  ,method: ''  //可选项。HTTP类型，默认post
  ,data: {} //可选项。额外的参数，如：{id: 123, abc: 'xxx'}
});  
~~~

该接口返回的相应信息（response）必须是一个标准的 JSON 格式

## 选择文件的回调choose

在文件被选择后触发，该回调会在 before 回调之前。一般用于非自动上传（即 auto: false ）的场景，比如预览图片等。

~~~javascript
upload.render({
  elem: '#id'
  ,url: '/api/upload/'
  ,auto: false //选择文件后不自动上传
  ,bindAction: '#testListAction' //指向一个按钮触发上传
  ,choose: function(obj){
    //将每次选择的文件追加到文件队列
    var files = obj.pushFile();
    
    //预读本地文件，如果是多文件，则会遍历。(不支持ie8/9)
    obj.preview(function(index, file, result){
      console.log(index); //得到文件索引
      console.log(file); //得到文件对象
      console.log(result); //得到文件base64编码，比如图片
      
      //obj.resetFile(index, file, '123.jpg'); //重命名文件名，layui 2.3.0 开始新增
      
      //这里还可以做一些 append 文件列表 DOM 的操作
      
      //obj.upload(index, file); //对上传失败的单个文件重新上传，一般在某个事件中使用
      //delete files[index]; //删除列表中对应的文件，一般在某个事件中使用
    });
  }
});      
~~~

## 文件上传前的回调before

~~~javascript
upload.render({
  elem: '#id'
  ,url: '/api/upload/'
  ,before: function(obj){ //obj参数包含的信息，跟 choose回调完全一致，可参见上文。
    layer.load(); //上传loading
  }
  ,done: function(res, index, upload){
    layer.closeAll('loading'); //关闭loading
  }
  ,error: function(index, upload){
    layer.closeAll('loading'); //关闭loading
  }
});
~~~

## 上传接口请求成功的回调done

在上传接口请求完毕后触发，但文件不一定是上传成功的，只是接口的响应状态正常（200）。回调返回三个参数，分别为：服务端响应信息、当前文件的索引、重新上传的方法

~~~javascript
upload.render({
  elem: '#id'
  ,url: '/api/upload/'
  ,done: function(res, index, upload){
    //假设code=0代表上传成功
    if(res.code == 0){
      //do something （比如将res返回的图片链接保存到表单的隐藏域）
    }
    
    //获取当前触发上传的元素，一般用于 elem 绑定 class 的情况，注意：此乃 layui 2.1.0 新增
    var item = this.item;
    
    //文件保存失败
    //do something
  }
});      
~~~

## 上传请求失败的回调error

当请求上传时出现异常时触发（如网络异常、404/500等）。回调返回三个参数，分别为：当前文件的索引、重新上传的方法

~~~javascript
upload.render({
  elem: '#id'
  ,url: '/api/upload/'
  ,error: function(index, upload){
    //当上传失败时，你可以生成一个“重新上传”的按钮，点击该按钮时，执行 upload() 方法即可实现重新上传
  }
});   
~~~

## 多文件上传完毕后的状态回调

只有当开启多文件时（即 multiple: true），该回调才会被触发。回调返回一个 object 类型的参数，包含一些状态数据：

~~~javascript
upload.render({
  elem: '#id'
  ,url: '/api/upload/'
  ,multiple: true
  ,allDone: function(obj){ //当文件全部被提交后，才触发
    console.log(obj.total); //得到总文件数
    console.log(obj.successful); //请求成功的文件数
    console.log(obj.aborted); //请求失败的文件数
  }
  ,done: function(res, index, upload){ //每个文件提交一次触发一次。详见“请求成功的回调”
  
  }
});      
~~~

## 重新上传

在执行 upload.render(options) 方法时，其实有返回一个实例对象，以便对完成重新上传等操作。注意：这是对当前上传队列的全局重新上传，而 choose 回调返回的 obj.upload(index, file) 方法则是对单个文件进行重新上传。如：

~~~javascript
var uploadInst = upload.render({
  elem: '#id'
  ,url: '/api/upload/'
  ,choose: function(obj){
    obj.preview(function(index, file, result){
      //对上传失败的单个文件重新上传，一般在某个事件中使用
      //obj.upload(index, file);
    });
  }
});
 
//重新上传的方法，一般在某个事件中使用
//uploadInst.upload(); 
~~~


