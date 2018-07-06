## Yii::$app 功能

#### 调用指定控制器的方法
    #注意区分当前控制器是web or console,只能调用自身类型对应的控制器
    \Yii::$app->runAction('timinglottery/v1/main/calc',$this->activityId);

#### 处理密码
    // bcrypt哈希
    // 哈希化密码
    $hash = Yii::$app->getSecurity()->generatePasswordHash($password);
    // 哈希串验证
    Yii::$app->getSecurity()->validatePassword($password, $hash)

#### 生成伪随机数据
    $key = Yii::$app->getSecurity()->generateRandomString();

#### 加密和解密
也可以通过 yii\base\Security::encryptByKey() 和 yii\base\Security::decryptByKey() 使用密钥而不是密码。

~~~
// $data 和 $secretKey 从表单中获得
$encryptedData = Yii::$app->getSecurity()->encryptByPassword($data, $secretKey);
// 将 $encryptedData 存储到数据库

// $secretKey 从用户输入获得，$encryptedData 来自数据库
$data = Yii::$app->getSecurity()->decryptByPassword($encryptedData, $secretKey);
~~~
    
#### 确认数据完整性
~~~
// 用密钥和数据生成的哈希前缀数据
// $secretKey 是我们的应用程序或用户密钥，$genuineData 是从可靠来源获得的
$data = Yii::$app->getSecurity()->hashData($genuineData, $secretKey);

// 检查数据完整性是否受到损害
// $secretKey 我们的应用程序或用户密钥，$data 从不可靠的来源获得
$data = Yii::$app->getSecurity()->validateData($data, $secretKey);
~~~
