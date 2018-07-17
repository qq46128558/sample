## Model中的方法

#### 根据ID查找一个Model
	<!-- backend\models\Menu -->
	$model = Menu::findOne($id)

#### 加载数据库设置的默认值到model
	<!-- vendor/yiisoft/yii2/db/ActiveRecord.php -->
	$model->loadDefaultValues();


#### 修改model中record的字段值
	$model->pid = $pid;


#### 根据ID查找一行记录
	$result=Menu::findOne(123);
	// 或
	$result=$this::findOne(123);
	if ($result)
		return $result->title

#### 添加非表字段属性
~~~php
// 在model中增加方法
public function getPidname(){
    $name=Menu::findOne($this->pid);
    if ($name && $this->pid!=0)
        return $name->title;
    else
        return Yii::t('backend','一級菜單');
}
// 则可以通过$model->pidname取得值,也可以应用于view页面
~~~