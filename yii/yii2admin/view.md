## 页面View(render的视图)

- $this 对应类: \yii\web\View
- $this->context 对应类: \yii\web\Controller
- 布局中的$content : 正文内容


#### 控制器向页面传递值的方法(多种)
~~~php
// 控制器中
//设置当前view的params参数，
$view = \Yii::$app->view;
$view->params['layoutData']='test';

// 页面中
<?php echo $this->params['layoutData']; ?>
// 或
<?=$this->params['layoutData'] ?>
~~~

~~~php
// 控制器中
return $this->render('index',['value1'=>$data,'value2'=>$info]);
// 只能在index的页面中获取到
<?php echo $value1; ?>
<?=$value2 ?>
~~~

~~~php
// 控制器中
public $myparams=[];
$this->myparams=array('item1','item2');
// 页面中
<?php var_dump($this->context->myparams);?>
~~~


#### 新增页面注意事项
	比如menu新加页面view(查看详情)
	需要增加对应的菜单动作(yii2_menu表),这样侧边的导航栏才能正常显示出来


#### 按钮中执行JS
	<?= Html::button('重置', ['class' => 'btn btn-default','onclick'=>"javascript:$('#menusearch-title').val('');"]) ?>