## 事件


#### 事件应用(测试)示例
~~~php
基类模型文件 vendor/yiisoft/yii2/db/BaseActiveRecord.php 中有许多数据库操作事件
如 const EVENT_AFTER_UPDATE = 'afterUpdate';

在控制器 backend/controllers/BaseController.php 的 saveRow()方法中增加代码如:
\yii\base\Event::on(yii\db\ActiveRecord::className(),yii\db\ActiveRecord::EVENT_AFTER_UPDATE,['\common\core\PubFunction','modelAdminLog']);   

则当模型有更新时,会执行 \common\core\PubFunction::modelAdminLog()方法

public static function modelAdminLog($event){
	file_put_contents('sample.txt',var_export($event,1),FILE_APPEND);
}
~~~

#### 回调函数应用
~~~php
public static function modelAdminLog($event){
// 取得事件名
$event->name

// 触发事件的模型
$event->sender
// 新属性值
$event->sender->attributes
// 旧属性值
$event->sender->oldAttributes

// 未知
$event->changedAttributes
~~~