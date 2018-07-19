
#### 发送Cookie
	$cookies = Yii::$app->response->cookies;
	$cookies->add(new \yii\web\Cookie([
	    'name' => 'language',
	    'value' => 'zh-CN',
	]));

#### 删除Cookie
	$cookies->remove('language');
	unset($cookies['language']);