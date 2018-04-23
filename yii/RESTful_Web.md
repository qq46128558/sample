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

**设置 enableSession 属性为 false.**

设置 loginUrl 属性为null 显示一个HTTP 403 错误而不是跳转到登录界面.

RESTful APIs应为无状态的， 当enableSession为false， 请求中的用户认证状态就不能通过session来保持

如果你将RESTful APIs作为应用开发，可以设置应用配置中 user 组件的 enableSession， 如果将RESTful APIs作为模块开发，可以在模块的 init() 方法中增加如下代码，如下所示
~~~
public function init()
{
    parent::init();
    \Yii::$app->user->enableSession = false;
}
~~~

为使用HTTP Basic Auth，**可配置authenticator 行为**，如下所示：

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

**在你的user identity class 类中实现 yii\web\IdentityInterface::findIdentityByAccessToken() 方法.**

findIdentityByAccessToken()方法的实现是系统定义的， 例如，一个简单的场景，当每个用户只有一个access token, 可存储access token 到user表的access_token列中， 方法可在User类中简单实现，如下所示：

~~~
use yii\db\ActiveRecord;
use yii\web\IdentityInterface;

class User extends ActiveRecord implements IdentityInterface
{
    public static function findIdentityByAccessToken($token, $type = null)
    {
        return static::findOne(['access_token' => $token]);
    }
}
~~~

在上述认证启用后，对于每个API请求， 请求控制器都会在它的beforeAction()步骤中对用户进行认证。

如果认证成功，控制器再执行其他检查(如频率限制，操作权限)，然后再执行动作， 授权用户信息可使用Yii::$app->user->identity获取.

如果认证失败，会发送一个HTTP状态码为401的响应， 并带有其他相关信息头(如HTTP 基本认证会有WWW-Authenticate 头信息).


## 限流
为防止滥用，你应该考虑对您的 API 限流。 例如，您可以限制每个用户 10 分钟内最多调用 API 100 次。 如果在规定的时间内接收了一个用户大量的请求，将返回响应状态代码 429 (这意味着过多的请求)。

要启用限流, user identity class 应该实现 yii\filters\RateLimitInterface.

这个接口需要实现以下三个方法：

- getRateLimit(): 返回允许的请求的最大数目及时间，例如，[100, 600] 表示在 600 秒内最多 100 次的 API 调用。
- loadAllowance(): 返回剩余的允许的请求和最后一次速率限制检查时 相应的 UNIX 时间戳数。
- saveAllowance(): 保存剩余的允许请求数和当前的 UNIX 时间戳。

为了提高性能，你也可以考虑使用缓存或 NoSQL 存储这些信息。

~~~
public function getRateLimit($request, $action)
{
    return [$this->rateLimit, 1]; // $rateLimit requests per second
}

public function loadAllowance($request, $action)
{
    return [$this->allowance, $this->allowance_updated_at];
}

public function saveAllowance($request, $action, $allowance, $timestamp)
{
    $this->allowance = $allowance;
    $this->allowance_updated_at = $timestamp;
    $this->save();
}
~~~

**一旦 identity 实现所需的接口， Yii 会自动使用 yii\filters\RateLimiter 为 yii\rest\Controller 配置一个行为过滤器来执行速率限制检查**。如果速度超出限制， 该速率限制器将抛出一个 yii\web\TooManyRequestsHttpException。

当速率限制被激活，默认情况下每个响应将包含以下 HTTP 头发送目前的速率限制信息：

- X-Rate-Limit-Limit: 同一个时间段所允许的请求的最大数目;
- X-Rate-Limit-Remaining: 在当前时间段内剩余的请求的数量;
- X-Rate-Limit-Reset: 为了得到最大请求数所等待的秒数。

你可以参考以下代码在你的 REST 控制器类里配置速率限制：
你可以禁用这些头信息通过配置 yii\filters\RateLimiter::$enableRateLimitHeaders 为 false, 就像代码示例所示。
~~~
public function behaviors()
{
    $behaviors = parent::behaviors();
    $behaviors['rateLimiter']['enableRateLimitHeaders'] = false;
    return $behaviors;
}
~~~


## 版本
一个常见的做法是在 API 的 URL 中嵌入版本号。例如， http://example.com/v1/users 代表 /users 版本 1 的 API。

另一种 API 版本化的方法， 最近用的非常多的是把版本号放入 HTTP 请求头，通常是通过 Accept 头，如下
~~~
// 通过参数
Accept: application/json; version=v1
// 通过vendor的内容类型
Accept: application/vnd.company.myapp-v1+json
~~~

下面我们描述在一种 API 版本混合了这两种方法的一个实用的策略：

- 把每个主要版本的 API 实现在一个单独的模块 ID 的主版本号 (例如 v1, v2)。 自然，API 的 url 将包含主要的版本号。
- 在每一个主要版本 (在相应的模块)，使用 Accept HTTP 请求头 确定小版本号编写条件代码来响应相应的次要版本。

为每个模块提供一个主要版本， 它应该包括资源类和控制器类 为特定服务版本。 更好的分离代码， 你可以保存一组通用的 基础资源和控制器类， 并用在每个子类版本模块。 在子类中， 实现具体的代码例如 Model::fields()。

你的代码可以类似于如下的方法组织起来：
~~~
api/
    common/
        controllers/
            UserController.php
            PostController.php
        models/
            User.php
            Post.php
    modules/
        v1/
            controllers/
                UserController.php
                PostController.php
            models/
                User.php
                Post.php
            Module.php
        v2/
            controllers/
                UserController.php
                PostController.php
            models/
                User.php
                Post.php
            Module.php
~~~

你的应用程序配置应该这样：

~~~
return [
    'modules' => [
        'v1' => [
            'class' => 'app\modules\v1\Module',
        ],
        'v2' => [
           'class' => 'app\modules\v2\Module',
        ],
    ],
    'components' => [
        'urlManager' => [
            'enablePrettyUrl' => true,
            'enableStrictParsing' => true,
            'showScriptName' => false,
            'rules' => [
                ['class' => 'yii\rest\UrlRule', 'controller' => ['v1/user', 'v1/post']],
                ['class' => 'yii\rest\UrlRule', 'controller' => ['v2/user', 'v2/post']],
            ],
        ],
    ],
];
~~~

**使用模块， 将不同版本的代码隔离。 通过共用基类和其他类 跨模块重用代码也是有可能的。**

为了处理次要版本号， 可以利用内容协商 功能通过 contentNegotiator 提供的行为。 contentNegotiator 行为可设置 yii\web\Response::$acceptParams 属性当它确定支持哪些内容类型时。

例如， 如果一个请求通过 Accept: application/json; version=v1 被发送， **内容交涉后，yii\web\Response::$acceptParams将包含值['version' => 'v1']**。

基于 acceptParams 的版本信息，你可以写条件代码 如 actions，resource classes，serializers 等等。

由于次要版本需要保持向后兼容性，希望你的代码不会有 太多的版本检查。否则，有机会你可能需要创建一个新的主要版本。


#### 错误处理
自定义错误响应

有时你可能想自定义默认的错误响应格式。例如，你想一直使用HTTP状态码200， 而不是依赖于使用不同的HTTP状态来表示不同的错误， 并附上实际的HTTP状态代码为JSON结构的一部分的响应

为了实现这一目的，你可以响应该应用程序配置的 response 组件的 beforeSend 事件：

~~~
return [
    // ...
    'components' => [
        'response' => [
            'class' => 'yii\web\Response',
            'on beforeSend' => function ($event) {
                $response = $event->sender;
                if ($response->data !== null && !empty(Yii::$app->request->get('suppress_response_code'))) {
                    $response->data = [
                        'success' => $response->isSuccessful,
                        'data' => $response->data,
                    ];
                    $response->statusCode = 200;
                }
            },
        ],
    ],
];
~~~

当 suppress_response_code 作为 GET 参数传递时，上面的代码 将重新按照自己定义的格式响应（无论失败还是成功）。
