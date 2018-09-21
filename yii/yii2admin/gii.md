## Gii 应用

#### 开启Gii
1. 配置文件(经查找前后端及API端均有,选一个来用即可):frontend/config/main-local.php(backend/config/main-local.php)(api/config/main-local.php)
2. 配置class及allowedIPs(否则默认只能本机访问)
~~~php
$config['modules']['gii'] = [ 
        'class' => 'yii\gii\Module',
        'allowedIPs'=>['14.29.69.182'],
    ];
~~~
3. 原配置文件中有if条件限制,如(不是测试环境则加载): if (!YII_ENV_TEST) {
4. YII_ENV_TEST 在基类中的定义是这样的:
~~~
// vendor/yiisoft/yii2/BaseYii.php
defined('YII_ENV_PROD') or define('YII_ENV_PROD', YII_ENV === 'prod');
defined('YII_ENV_DEV') or define('YII_ENV_DEV', YII_ENV === 'dev');
defined('YII_ENV_TEST') or define('YII_ENV_TEST', YII_ENV === 'test');
~~~
5. 可以在.env文件中配置: YII_ENV     = dev 


#### 使用 Gii 去生成活动记录类
1. 需要先在后台建表
2. 使用Model Generator
3. 各值如下
~~~
Table Name: yii2_uploadfile
Model Class Name: Uploadfile
勾选: Standardize Capitals
Namespace: common\modelsgii
Base Class: \common\core\BaseActiveRecord
Database Connection ID: db
勾选Use Table Prefix
Generate Relations: All relations
勾选Generate Relations from Current Schema
勾选Generate Labels from DB Comments
不勾选Generate ActiveQuery
勾选Enable I18N
Message Category: common
勾选Use Schema Name
~~~
4. Preview/Generate


#### 使用 Gii 去生成数据表操作的增查改删（CRUD）代码
1. 在backend建一个空的model
~~~
<?php
namespace backend\models;
use Yii;
class Uploadfile extends \common\modelsgii\Uploadfile
{
}
~~~
2. 使用CRUD Generator
3. 各值如下
~~~
Model Class: backend\models\Uploadfile
Search Model Class: backend\models\search\UploadfileSearch
Controller Class: backend\controllers\UploadfileController
View Path: @backend/views/uploadfile
Base Controller Class: backend\controllers\BaseController
Widget Used in Index Page: GridView
勾选Enable I18N
不勾选Enable Pjax
Message Category: backend
~~~
4. Preview/Generate
