## 防止 CSRF 攻击
CSRF 是跨站请求伪造的缩写

比如说：an.example.com 站点有一个 /logout URL，当以 GET 请求访问时， 登出用户。如果它是由用户自己操作的，那么一切都没有问题。但是， 有一天坏人在一个用户经常访问的论坛发了一个 `<img src="http://an.example.com/logout">` 内容的帖子。 浏览器无法辨别请求一个图片还是一个页面，所以，当用户打开含有上述标签的页面时，他将会从 an.example.com 登出

为了避免 CSRF 攻击，你总是需要：
- 遵循 HTTP 准则，比如 GET 不应该改变应用的状态。
- 保证 Yii CSRF 保护开启。

#### 控制器关闭CSRF
~~~
namespace app\controllers;

use yii\web\Controller;

class SiteController extends Controller
{
    public $enableCsrfValidation = false;

    public function actionIndex()
    {
        // CSRF validation will not be applied to this and other actions
    }

}
~~~

#### 动作关闭CSRF
~~~
namespace app\controllers;

use yii\web\Controller;

class SiteController extends Controller
{
    public function beforeAction($action)
    {
        // ...set `$this->enableCsrfValidation` here based on some conditions...
        $this->enableCsrfValidation = false;
        // call parent method that will check CSRF if such property is true.
        return parent::beforeAction($action);
    }
}
~~~