
## RBAC权限控制(未完全理解)


### 后台
#### 权限检查的入口
	backend/behaviors/RbacBehavior.php
	public function rbacAction($event){


#### 配置RBAC权限数据保存控制类?
	backend\config\main.php
	/* 数据库RBAC权限控制 */
    'authManager' => [
        'class' => 'common\core\rbac\DbManager',
    ],
