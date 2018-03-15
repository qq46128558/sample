

##### 模型加载Post数据
    $model->load(Yii::$app->request->post());

##### 模型必填值校验
    $model->validate();

##### XSS过滤
    use yii\helpers\Html;
    $value=Html::encode('<script>alert("abc");</script>');

##### 获取CSRF Token
    Yii::$app->request->getCsrfToken();
    Yii::$app->request->csrfToken;

##### 获取版本
    Yii::getVersion();

##### 全局应用实例/单例/服务定位器
    Yii::$app   