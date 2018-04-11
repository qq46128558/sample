#### 当前用户的身份实例。未认证用户则为 Null
    $identity = Yii::$app->user->identity;

#### 当前用户的ID。 未认证用户则为 Null 。
    $id = Yii::$app->user->id;

#### 判断当前用户是否是游客（未认证的）
    $isGuest = Yii::$app->user->isGuest;

#### 登录用户
~~~
// 使用指定用户名获取用户身份实例。
// 请注意，如果需要的话您可能要检验密码
$identity = User::findOne(['username' => $username]);

// 登录用户
Yii::$app->user->login($identity);

// 为了使用 cookie 登录，你需要在应用配置文件中将 yii\web\User::$enableAutoLogin 设为 true。你还需要在 yii\web\User::login() 方法中 传递有效期（记住登录状态的时长）参数。
~~~

#### 注销用户
	Yii::$app->user->logout();
	// 请注意，启用 session 时注销用户才有意义。该方法将从内存和 session 中 同时清理用户认证状态。默认情况下，它还会注销所有的 用户会话数据。
	// 如果你希望保留这些会话数据，可以换成 Yii::$app->user->logout(false) 。

