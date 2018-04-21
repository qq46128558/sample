## RESTful Web 服务
Yii 提供了一整套用来简化实现 RESTful 风格的 Web Service 服务的 API

#### 资源
RESTful 的 API 都是关于访问和操作 资源，可将资源看成MVC模式中的 模型

**字段**

当RESTful API响应中包含一个资源时，该资源需要序列化成一个字符串。 Yii将这个过程分成两步，首先，资源会被yii\rest\Serializer转换成数组， 然后，该数组会通过response formatters 根据请求格式(如JSON, XML)被序列化成字符串。 当开发一个资源类时应重点关注第一步。

通过覆盖 fields() 和/或 yii\base\Model::extraFields() 方法, 可指定资源中称为 字段 的数据放入展现数组中， 两个方法的差别为前者指定默认包含到展现数组的字段集合， 后者指定由于终端用户的请求包含 expand 参数哪些额外的字段应被包含到展现数组

~~~
// 返回fields()方法中申明的所有字段
http://localhost/users

// 只返回fields()方法中申明的id和email字段
http://localhost/users?fields=id,email

// 返回fields()方法申明的所有字段，以及extraFields()方法中的profile字段
http://localhost/users?expand=profile

// 返回回fields()和extraFields()方法中提供的id, email 和 profile字段
http://localhost/users?fields=id,email&expand=profile
~~~

覆盖 fields() 方法
~~~
// 明确列出每个字段，适用于你希望数据表或
// 模型属性修改时不导致你的字段修改（保持后端API兼容性）
public function fields()
{
    return [
        // 字段名和属性名相同
        'id',
        // 字段名为"email", 对应的属性名为"email_address"
        'email' => 'email_address',
        // 字段名为"name", 值由一个PHP回调函数定义
        'name' => function ($model) {
            return $model->first_name . ' ' . $model->last_name;
        },
    ];
}

// 过滤掉一些字段，适用于你希望继承
// 父类实现同时你想屏蔽掉一些敏感字段
public function fields()
{
    $fields = parent::fields();

    // 删除一些包含敏感信息的字段
    unset($fields['auth_key'], $fields['password_hash'], $fields['password_reset_token']);

    return $fields;
}
~~~

覆盖 extraFields() 方法

~~~
public function fields()
{
    return ['id', 'email'];
}

public function extraFields()
{
    return ['profile'];
}
~~~


#### 控制器
Yii 提供两个控制器基类来简化创建RESTful 操作的工作:**yii\rest\Controller** 和 **yii\rest\ActiveController**， 两个类的差别是后者提供一系列将资源处理成Active Record的操作。

~~~
namespace app\controllers;

use yii\rest\ActiveController;

class UserController extends ActiveController
{
    // 通过指定 modelClass 作为 app\models\User， 控制器就能知道使用哪个模型去获取和处理数据
    public $modelClass = 'app\models\User';
}
~~~

创建新的操作和Web应用中创建操作类似， 唯一的差别是Web应用中调用render()方法渲染一个视图作为返回值， 对于RESTful操作直接返回数据， serializer 和response object 会处理原始数据到请求格式的转换，例如

~~~
public function actionView($id)
{
    return User::findOne($id);
}
~~~

过滤器

如果你只想用HTTP 基础认证，可编写如下代码

~~~
use yii\filters\auth\HttpBasicAuth;

public function behaviors()
{
    $behaviors = parent::behaviors();
    $behaviors['authenticator'] = [
        'class' => HttpBasicAuth::className(),
    ];
    return $behaviors;
}
~~~

**自定义动作**

所有这些动作通过actions() 方法申明，可覆盖actions()方法配置或禁用这些动作

~~~
public function actions()
{
    $actions = parent::actions();

    // 禁用"delete" 和 "create" 动作
    unset($actions['delete'], $actions['create']);

    // 使用"prepareDataProvider()"方法自定义数据provider 
    $actions['index']['prepareDataProvider'] = [$this, 'prepareDataProvider'];

    return $actions;
}

public function prepareDataProvider()
{
    // 为"index"动作准备和返回数据provider
}
~~~

**执行访问检查**

在yii\rest\ActiveController中， 可覆盖checkAccess()方法来完成权限检查

~~~
public function checkAccess($action, $model = null, $params = [])
{
    // check if the user can access $action and $model
    // throw ForbiddenHttpException if access should be denied
    if ($action === 'update' || $action === 'delete') {
        if ($model->author_id !== \Yii::$app->user->id)
            throw new \yii\web\ForbiddenHttpException(sprintf('You can only %s articles that you\'ve created.', $action));
    }
}
~~~

#### 路由

在实践中，你通常要用美观的 URL 并采取有优势的 HTTP 动词。 例如，请求 POST /users 意味着访问 user/create 动作。 这可以很容易地通过配置 urlManager 应用程序组件来完成 如下所示：

~~~
'urlManager' => [
    'enablePrettyUrl' => true,
    'enableStrictParsing' => true,
    'showScriptName' => false,
    'rules' => [
        ['class' => 'yii\rest\UrlRule', 'controller' => 'user'],
    ],
]
~~~

通过配置 only 和 except 选项来明确列出哪些行为支持， 哪些行为禁用

~~~
[
    'class' => 'yii\rest\UrlRule',
    'controller' => 'user',
    'except' => ['delete', 'create', 'update'],
],
~~~

可以通过配置 patterns 或 extraPatterns 重新定义现有的模式或添加此规则支持的新模式。 例如，通过末端 GET /users/search 可以支持新行为 search， 按照如下配置 extraPatterns 选项

~~~
[
    'class' => 'yii\rest\UrlRule',
    'controller' => 'user',
    'extraPatterns' => [
        'GET search' => 'search',
    ],
]
~~~

**您可能已经注意到控制器 ID user 以复数形式出现在 users 末端。 这是因为 yii\rest\UrlRule 能够为他们使用的末端全自动复数化控制器 ID。 您可以通过设置 yii\rest\UrlRule::$pluralize 为 false 来禁用此行为。**

你也可以配置 yii\rest\UrlRule::$controller 属性来明确指定如何将端点URL中使用的名称映射到 控制器ID。例如，以下代码将名称 u 映射到控制器ID user

~~~
[
    'class' => 'yii\rest\UrlRule',
    'controller' => ['u' => 'user'],
]
~~~

在 yii\rest\UrlRule 中所包含的每个规则中，指定额外的配置可能很有用。 一个很好的例子就是指定 expand 参数的默认值(未理解)

~~~
[
    'class' => 'yii\rest\UrlRule',
    'controller' => ['user'],
    'ruleConfig' => [
        'class' => 'yii\web\UrlRule',
        'defaults' => [
            'expand' => 'profile',
        ]
    ],
],
~~~


## 认证
和Web应用不同，RESTful APIs 通常是无状态的， 也就意味着不应使用sessions 或 cookies， 因此每个请求应附带某种授权凭证，因为用户授权状态可能没通过sessions 或 cookies维护， 常用的做法是每个请求都发送一个秘密的access token来认证用户， 由于access token可以唯一识别和认证用户， API 请求应通过HTTPS来防止man-in-the-middle (MitM) 中间人攻击

- HTTP 基本认证:  access token 当作用户名发送，应用在access token可安全存在API使用端的场景， 例如，API使用端是运行在一台服务器上的程序
- 请求参数: access token 当作API URL请求参数发送，例如 https://example.com/users?access-token=xxxxxxxx， 由于大多数服务器都会保存请求参数到日志， 这种方式应主要用于JSONP 请求，因为它不能使用HTTP头来发送access token
- OAuth 2: 使用者从认证服务器上获取基于OAuth2协议的access token， 然后通过HTTP Bearer Tokens 发送到API 服务器

