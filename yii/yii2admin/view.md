## 页面View(render的视图)

- $this 对应类: \yii\web\View
- $this->context 对应类: \yii\web\Controller



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
