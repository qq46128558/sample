#### 当前用户的身份实例。未认证用户则为 Null
    $identity = Yii::$app->user->identity;

#### 当前用户的ID。 未认证用户则为 Null 。
    $id = Yii::$app->user->id;

#### 判断当前用户是否是游客（未认证的）
    $isGuest = Yii::$app->user->isGuest;

