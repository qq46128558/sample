## Url 助手类
yii\helpers\Url

### 获得通用 URL
~~~
$relativeHomeUrl = Url::home();
$absoluteHomeUrl = Url::home(true);
$httpsAbsoluteHomeUrl = Url::home('https');
~~~

~~~
$relativeBaseUrl = Url::base();
$absoluteBaseUrl = Url::base(true);
$httpsAbsoluteBaseUrl = Url::base('https');
~~~

### 创建 URLs
~~~
$url = Url::toRoute(['product/view', 'id' => 42]);

// generates: /index.php?r=site/index&param1=value1&param2=value2
['site/index', 'param1' => 'value1', 'param2' => 'value2']

// generates: /index.php?r=site/index&param1=value1#name
['site/index', 'param1' => 'value1', '#' => 'name']
~~~

~~~
// /index.php?r=site/index
echo Url::toRoute('site/index');

// /index.php?r=site/index&src=ref1#name
echo Url::toRoute(['site/index', 'src' => 'ref1', '#' => 'name']);

// /index.php?r=post/edit&id=100     假设别名 "@postEdit" 被定义为 "post/edit"
echo Url::toRoute(['@postEdit', 'id' => 100]);

// http://www.example.com/index.php?r=site/index
echo Url::toRoute('site/index', true);

// https://www.example.com/index.php?r=site/index
echo Url::toRoute('site/index', 'https');
~~~

还有另外一个方法 **Url::to() 和 toRoute() 非常类似**。这两个方法的唯一区别在于，前者要求一个路由必须用数组来指定。 如果传的参数为字符串，它将会被直接当做 URL 。

~~~
// /index.php?r=site/index
echo Url::to(['site/index']);

// /index.php?r=site/index&src=ref1#name
echo Url::to(['site/index', 'src' => 'ref1', '#' => 'name']);

// /index.php?r=post/edit&id=100     假设别名 "@postEdit" 被定义为 "post/edit"
echo Url::to(['@postEdit', 'id' => 100]);

// 当前请求的 URL
echo Url::to();

// /images/logo.gif
echo Url::to('@web/images/logo.gif');

// images/logo.gif
echo Url::to('images/logo.gif');

// http://www.example.com/images/logo.gif
echo Url::to('@web/images/logo.gif', true);

// https://www.example.com/images/logo.gif
echo Url::to('@web/images/logo.gif', 'https');
~~~

使用 yii\helpers\Url::current() 来创建一个基于当前请求路由和 GET 参数的 URL。 **你可以通过传递一个 $params 给这个方法来添加或者删除 GET 参数**

~~~
// 假设 $_GET = ['id' => 123, 'src' => 'google']，当前路由为 "post/view"

// /index.php?r=post/view&id=123&src=google
echo Url::current();

// /index.php?r=post/view&id=123
echo Url::current(['src' => null]);
// /index.php?r=post/view&id=100&src=google
echo Url::current(['id' => 100]);
~~~

### 记住 URLs
~~~
// 记住当前 URL 
Url::remember();

// 记住指定的 URL。参数格式请参阅 Url::to()。
Url::remember(['product/view', 'id' => 42]);

// 记住用给定名称指定的 URL
Url::remember(['product/view', 'id' => 42], 'product');
~~~

在后续的请求处理中，可以用如下方式获得记住的 URL：

~~~
$url = Url::previous();
$productUrl = Url::previous('product');
~~~

### 检查相对 URLs
    $isRelative = Url::isRelative('test/it');




