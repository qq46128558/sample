## 控制器中的方法

#### 保存一行数据
	传入model及data,自动根据model(new或findone)进行model->insert()或model->update()
	$this->saveRow($model, $data)

#### 标记当前位置到cookie供后续跳转调用
	$this->setForward();

#### 读取标记过的位置
	$this->getForward();


#### 显示动作执行信息
	<!-- 成功并跳转 -->
	$this->success(Yii::t('backend','動作執行成功'), $this->getForward());
	<!-- 失败不跳转 -->
	$this->error(Yii::t('backend','動作執行錯誤'));

#### 直接显示信息
	<!-- 刷新页面 -->
	$this->success('abc',null,true);
	<!-- 不刷新页面 -->
	$this->error('abc',null,true);
	<!-- 控制显示时间: BaseController.php>>dispatchJump()>>$waitSecond -->
	<!-- 控制器中显示信息 -->
	header('Content-Type:application/json; charset=utf-8');
 	echo json_encode(array('info'=>'abc','status'=>1,'url'=>null));exit;

#### 显示渲染的页面
~~~php
// 并传入参数$searchModel及$dataProvider到view页面
return $this->render('index', [
    'searchModel' => $searchModel,
    'dataProvider' => $dataProvider,
]);

return $this->render('edit', [
    'model' => $model,
]);
~~~