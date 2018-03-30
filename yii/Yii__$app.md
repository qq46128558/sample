## Yii::$app 功能

#### 调用指定控制器的方法
    #注意区分当前控制器是web or console,只能调用自身类型对应的控制器
    \Yii::$app->runAction('timinglottery/v1/main/calc',$this->activityId);