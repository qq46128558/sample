## 权限存取控制
`$auth = Yii::$app->authManager;`

#### 关键概念
- 规则
- 权限
- 角色

#### 添加 "createPost" 权限
    $createPost = $auth->createPermission('createPost');
    $createPost->description = 'Create a post';
    $auth->add($createPost);

#### 添加 "updatePost" 权限
    $updatePost = $auth->createPermission('updatePost');
    $updatePost->description = 'Update post';
    $auth->add($updatePost);

#### 添加 "author" 角色
    $author = $auth->createRole('author');
    $auth->add($author);

#### 添加 "admin" 角色
    $admin = $auth->createRole('admin');
    $auth->add($admin);

#### 给"author" 角色赋予 "createPost" 权限
    $auth->addChild($author,$createPost);

#### 给"admin" 角色赋予 "updatePost" 权限
    $auth->addChild($admin,$updatePost);

#### 给"admin" 角色赋予 "author" 权限
    // 即$author为$admin的子角色
    // 也可以理解$admin拥有$author的权限
    $auth->addChild($admin,$author);

#### 为用户指派角色
    // 其中 1 和 2 是由 IdentityInterface::getId() 返回的id （译者注：user表的id）
    $auth->assign($author,2);
    $auth->assign($admin,1);

#### 获取author角色
    $authorRole = $auth->getRole('author');

#### 添加规则
    // 规则是 yii\rbac\Rule 的派生类。 它需要实现 execute() 方法
    $rule = new \app\rbac\AuthorRule;
    $auth->add($rule);

#### 添加 "updateOwnPost" 权限并与规则关联
    // 规则是上面的\app\rbac\AuthorRule
    $updateOwnPost = $auth->createPermission('updateOwnPost');
    $updateOwnPost->description = 'Update own post';
    $updateOwnPost->ruleName = $rule->name;
    $auth->add($updateOwnPost);

#### "updateOwnPost" 权限将由 "updatePost" 权限使用
    $auth->addChild($updateOwnPost,$updatePost);

#### 给"author" 角色赋予 "updateOwnPost" 权限
    // 允许 "author" 更新自己的帖子
    $auth->addChild($author,$updateOwnPost);

#### 存取检查(判断权限)
    // 判断user是否有createPost权限
    \Yii::$app->user->can('createPost')

#### 存取检查(带参数)
    // 是否有updatePost权限
    \Yii::$app->user->can('updatePost', ['post' => $post])

#### 角色与规则关联(用于使用默认角色)
    $rule = new \app\rbac\UserGroupRule;
    $auth->add($rule);

    $author = $auth->createRole('author');
    $author->ruleName = $rule->name;
    $auth->add($author);

