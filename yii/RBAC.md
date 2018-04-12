## 基于角色的存取控制
使用 RBAC 涉及到两部分工作。第一部分是建立授权数据， 而第二部分是使用这些授权数据在需要的地方执行检查

基于角色的存取控制 （RBAC） 提供了一个简单而强大的集中式存取控制机制

#### 配置RBAC (使用 PhpManager)
~~~
// yii\rbac\PhpManager 默认将 RBAC 数据保存在 @app/rbac 目录下的文件中
return [
    // ...
    'components' => [
        'authManager' => [
            'class' => 'yii\rbac\PhpManager',
        ],
        // ...
    ],
];
~~~


#### 配置RBAC (使用 DbManager)
~~~
return [
    // ...
    'components' => [
        'authManager' => [
            'class' => 'yii\rbac\DbManager',
        ],
        // ...
    ],
];

// 继续之前，你需要在数据库中创建表存放授权数据
// 你可以使用存放在 @yii/rbac/migrations 目录中的数据库迁移文件来做这件事
// yii migrate --migrationPath=@yii/rbac/migrations
// 可以通过 \Yii::$app->authManager 访问 authManager
~~~


#### 建立授权数据
~~~
// 最好是将授权数据初始化命令写到 RBAC 数据库迁移文件中
<?php
namespace app\commands;

use Yii;
use yii\console\Controller;

class RbacController extends Controller
{
    public function actionInit()
    {
        $auth = Yii::$app->authManager;

        // 添加 "createPost" 权限
        $createPost = $auth->createPermission('createPost');
        $createPost->description = 'Create a post';
        $auth->add($createPost);

        // 添加 "updatePost" 权限
        $updatePost = $auth->createPermission('updatePost');
        $updatePost->description = 'Update post';
        $auth->add($updatePost);

        // 添加 "author" 角色并赋予 "createPost" 权限
        $author = $auth->createRole('author');
        $auth->add($author);
        $auth->addChild($author, $createPost);

        // 添加 "admin" 角色并赋予 "updatePost" 
		// 和 "author" 权限
        $admin = $auth->createRole('admin');
        $auth->add($admin);
        $auth->addChild($admin, $updatePost);
        $auth->addChild($admin, $author);

        // 为用户指派角色。其中 1 和 2 是由 IdentityInterface::getId() 返回的id （译者注：user表的id）
        // 通常在你的 User 模型中实现这个函数。
        $auth->assign($author, 2);
        $auth->assign($admin, 1);
    }
}

// 执行授权数据初始化
php yii rbac/init
~~~


#### 注册用户授权
~~~
// 如果你的应用允许用户注册，你需要在注册时给新用户指派一次角色。例如， 在高级项目模板中，要让所有注册用户成为作者，你需要如下例所示修改 frontend\models\SignupForm::signup() 方法
public function signup()
{
    if ($this->validate()) {
        ......
        // 要添加以下三行代码：
        $auth = Yii::$app->authManager;
        $authorRole = $auth->getRole('author');
        $auth->assign($authorRole, $user->getId());

        return $user;
    }

    return null;
}
~~~

#### 使用规则
~~~
// 规则是 yii\rbac\Rule 的派生类。 它需要实现 execute() 方法
namespace app\rbac;

use yii\rbac\Rule;

/**
 * 检查 authorID 是否和通过参数传进来的 user 参数相符
 */
class AuthorRule extends Rule
{
    public $name = 'isAuthor';

    /**
     * @param string|integer $user 用户 ID.
     * @param Item $item 该规则相关的角色或者权限
     * @param array $params 传给 ManagerInterface::checkAccess() 的参数
     * @return boolean 代表该规则相关的角色或者权限是否被允许
     */
    public function execute($user, $item, $params)
    {
        return isset($params['post']) ? $params['post']->createdBy == $user : false;
    }
}
~~~

上述规则检查 post 是否是 $user 创建的。我们还要在之前的命令中 创建一个特别的权限 updateOwnPost

~~~
$auth = Yii::$app->authManager;

// 添加规则
$rule = new \app\rbac\AuthorRule;
$auth->add($rule);

// 添加 "updateOwnPost" 权限并与规则关联
$updateOwnPost = $auth->createPermission('updateOwnPost');
$updateOwnPost->description = 'Update own post';
$updateOwnPost->ruleName = $rule->name;
$auth->add($updateOwnPost);

// "updateOwnPost" 权限将由 "updatePost" 权限使用
$auth->addChild($updateOwnPost, $updatePost);

// 允许 "author" 更新自己的帖子
$auth->addChild($author, $updateOwnPost);
~~~


#### 存取检查
~~~
// 存取检查简单到只需要一个方法调用 yii\rbac\ManagerInterface::checkAccess()
// 为方便起见， Yii 提供了一个快捷方法 yii\web\User::can()
if (\Yii::$app->user->can('createPost')) {
    // 建贴
}

// 为了检查某用户是否能更新帖子，我们需要传递一个额外的参数，该参数是 AuthorRule 要用的
if (\Yii::$app->user->can('updatePost', ['post' => $post])) {
    // 更新帖子
}
~~~


#### 使用默认角色

所谓默认角色就是 隐式 地指派给 所有 用户的角色。不需要调用 yii\rbac\ManagerInterface::assign() 方法做显示指派，并且授权数据中不包含指派信息

默认角色通常与一个规则关联，用以检查该角色是否符合被检查的用户

~~~
// 建立规则-检查是否匹配用户的组
namespace app\rbac;

use Yii;
use yii\rbac\Rule;

/**
 * 检查是否匹配用户的组
 */
class UserGroupRule extends Rule
{
    public $name = 'userGroup';

    public function execute($user, $item, $params)
    {
        if (!Yii::$app->user->isGuest) {
            $group = Yii::$app->user->identity->group;
            if ($item->name === 'admin') {
                return $group == 1;
            } elseif ($item->name === 'author') {
                return $group == 1 || $group == 2;
            }
        }
        return false;
    }
}
// 注意，在上述代码中，因为 "author" 作为 "admin" 的子角色，当你实现这个规则的 execute() 方法时， 你也需要遵从这个层次结构。
// 这就是为何当角色名为 "author" 的情况下（译者注：$item->name就是角色名）， execute() 方法在组为 1 或者 2 时均要返回 true （意思是用户属于 "admin" 或者 "author" 组 ）。
~~~

~~~
// 初始化数据指令
$auth = Yii::$app->authManager;

$rule = new \app\rbac\UserGroupRule;
$auth->add($rule);

$author = $auth->createRole('author');
$author->ruleName = $rule->name;
$auth->add($author);
// ... 添加$author角色的子项部分代码 ... （译者注：省略部分参照之前的控制台命令）

$admin = $auth->createRole('admin');
$admin->ruleName = $rule->name;
$auth->add($admin);
$auth->addChild($admin, $author);
// ... 添加$admin角色的子项部分代码 ... （译者注：省略部分参照之前的控制台命令）
~~~

配置 defaultRoles
~~~
return [
    // ...
    'components' => [
        'authManager' => [
            'class' => 'yii\rbac\PhpManager',
            'defaultRoles' => ['admin', 'author'],
        ],
        // ...
    ],
];
~~~

现在如果你执行一个存取权限检查， 判定该规则时， admin 和 author 两个角色都将会检查

如果规则返回 true ，意思是角色符合当前用户

`基于上述规则 的实现，意味着如果某用户的 group 值为 1 ， admin 角色将赋予该用户， 如果 group 值是 2 则将赋予 author 角色。`

(未完全理解)