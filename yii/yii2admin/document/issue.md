## Yii2Admin 问题记录

### 后台

#### 翻页后点击行动作(如删除),无提示框,直接显示JSON
~~~
触发提示框显示的代码由JS控制: common/metronic/other/js/common.js
发现翻页后,无加载common.js
再次刷新后则加载common.js正常

解决:
view对应页面(index.php),body中删除对应代码即可
<?php \yii\widgets\Pjax::begin(['options'=>['id'=>'pjax-container']]); ?>
<?php \yii\widgets\Pjax::end(); ?>

原因:
pjax导致了js失效
~~~

#### Model保存失败无提示(是因为校验失败)
Model的校验代码
~~~
vendor/yiisoft/yii2/validators/Validator.php 288
	public function validateAttribute($model, $attribute)
~~~


#### var_export does not handle circular reference
~~~
将var_export
$data['remark']=var_export($event,1)
改为print_r即可
$data['remark']=print_r($event,1)
~~~


#### 文件上传获取$_FILES为空Array()
~~~
使用Yii的ActiveForm的fileInput(),后台使用\yii\web\UploadedFile
获取实例(getInstance())时返回为Null,跟踪发现$_FILES为空Array()

原因:
提交按钮class="ajax-post"
则会调用 common\metronic\other\js\common.js
以 $.ajax post方式提交数据,导致获取不到$_FILES数据

解决:
1. 不以$.post()方式传数据.
2. 使用自定义上传文件widget.
[其他原因参考资料](https://blog.csdn.net/dxk539687357/article/details/52460685 "https://blog.csdn.net/dxk539687357/article/details/52460685")
~~~





### API

#### 默认Index方法不支持POST的解决
~~~
POST方式调用接口: http://47.106.160.48/api/tp/test?access-token=M0eZFQzHhDwokrkCAdTMc2vyqayCxw3k
返回
{"name":"Method Not Allowed","message":"Method Not Allowed. This URL can only handle the following request methods: GET, HEAD.","code":0,"status":405,"type":"yii\\web\\MethodNotAllowedHttpException"}

抛错位置:
vendor/yiisoft/yii2/filters/VerbFilter.php
101         if (!in_array($verb, $allowed)) {
102             $event->isValid = false;
103             // https://tools.ietf.org/html/rfc2616#section-14.7
104             Yii::$app->getResponse()->getHeaders()->set('Allow', implode(', ', $allowed));
105             throw new MethodNotAllowedHttpException('Method Not Allowed. This URL can only handle t    he following request methods: ' . implode(', ', $allowed) . '.');
106         }


方法一:
修改框架代码: vendor/yiisoft/yii2/rest/ActiveController.php
对index增加POST
111     protected function verbs()
112     {
113         return [
114             'index' => ['POST',GET', 'HEAD'],
115             'view' => ['GET', 'HEAD'],
116             'create' => ['POST'],
117             'update' => ['PUT', 'PATCH'],
118             'delete' => ['DELETE'],
119         ];
120     }

方法二:
// 重写行为方法
public function behaviors(){
    $behaviors=parent::behaviors();
    // 设置认证方式. 不设置则无需access-token,可以随便调用
    $behaviors['authenticator']=['class'=>QueryParamAuth::className(),];
    // 使index方法支持POST
   	$behaviors['verbFilter']['actions']['index']=['GET','POST','HEAD'];
	return $behaviors;                                                                       
}
~~~


### JS

#### js文件中引入另外一个js
~~~
new_element=document.createElement("script");
new_element.setAttribute("type","text/javascript");
new_element.setAttribute("src","a.js"); // 在这里引入了a.js
document.body.appendChild(new_element);
~~~

#### common.js中使用layui.js
~~~
html中先加载了layui.js, 然后在common.js中可以直接使用(就像使用jquery一样), 如:
//dom加载完成后执行的js
;$(function(){
	layui.use('layer',function(){var layer = layui.layer;});
});
~~~