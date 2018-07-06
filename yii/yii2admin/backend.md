## 后台目录

#### 定义超级管理员
    backend/config/params.ph
    <!-- 指定admin属性的uid值,即为超级管理员,不需要rbac权限检查 -->

#### 后台系统设置>>网站设置
    对应db表:yii2_config
    通常在BaseController控制器的init构造函数中转化,并存入Yii::$app->params['web']中
    use backend\models\Config;
    Yii::$app->params['web'] = Config::lists();