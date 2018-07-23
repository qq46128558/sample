## 表关系说明

|表名|描述|备注
|-|-|-
|yii2_auth_assignment|角色关联后台用户表|user_id关联yii2_admin的uid
|yii2_auth_item|角色表及权限表|type=1角色,type=2权限,varchar(64)为主键
|yii2_auth_item_child|角色对应权限表|-
|yii2_auth_rule|权限对应的类功能控制器?|未确定
|yii2_picture|图片地址|-
