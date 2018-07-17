
#### 是否有Post数据
	Yii::$app->request->isPost

#### 读取Post数据
	<!-- 返回数组 -->
	$data = Yii::$app->request->post('Menu');

#### 读取Url参数
	<!-- 返回数组 -->
	Yii::$app->request->queryParams
	<!-- 返回字符串 -->
	$ids = Yii::$app->request->param('id', 0);

#### 读取Get参数
	$pid = Yii::$app->request->get('pid', 0);

#### 是否Ajax方式提交
	Yii::$app->request->isAjax