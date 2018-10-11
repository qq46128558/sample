#### 生成一个auth_key
    #随机字符串
    \Yii::$app->security->generateRandomString();

	#加密密码
	Yii::$app->security->generatePasswordHash($password);
	
    #校验密码
    Yii::$app->getSecurity()->validatePassword($password, $result['password']))