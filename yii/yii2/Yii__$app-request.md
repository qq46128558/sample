
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

#### 读取Cookie(当前请求的cookie信息)
	$cookies = Yii::$app->request->cookies;
	<!-- 获取名为 "language" cookie 的值，如果不存在，返回默认值 "en" -->
	$language = $cookies->getValue('language', 'en');

#### 判断某Cookie名是否存在
	if ($cookies->has('language')) ...
	if (isset($cookies['language'])) ...


#### 获取登录用户的IP
	Yii::$app->request->getUserIP()