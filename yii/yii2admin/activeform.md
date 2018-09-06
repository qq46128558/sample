## ActiveForm小部件应用


#### 类文件
	// 如view中调用方式,一般如:
	$form->field()->widget()->label();

	common\core\ActiveForm 
	class ActiveForm extends \yii\widgets\ActiveForm
	// 基类文件位置
	vendor/yiisoft/yii2/widgets/ActiveForm.php
	class ActiveForm extends Widget
	
	// field方法
	public function field($model, $attribute, $options = [])
	// 返回object
	Yii::createObject()

	common/core/ActiveField.php
	class ActiveField extends \yii\widgets\ActiveField
	public function widget($class, $config = [], $options = [])
	// 基类文件位置
	// vendor/yiisoft/yii2/widgets/ActiveField.php
	// widget()方法
	public function widget($class, $config = [])



