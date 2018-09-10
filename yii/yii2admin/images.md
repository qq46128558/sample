## 上传图片
感觉需要学习Yii2的widget开发基础才会比较好理解

#### 配置
~~~php
// 存储位置.env
	STORAGE_URL      = /storage
// 存储位置别名 common/config/bootstrap.php
	Yii::setAlias('@storage', dirname(dirname(__DIR__)) . '/storage'); //存储目录path
	Yii::setAlias('@storageUrl', env('STORAGE_URL')); //存储url
// 上传文件位置 common/config/params.php
	'upload' => [
        'url'  => Yii::getAlias('@storageUrl/image/'),
        'path' => Yii::getAlias('@storage/web/image/'),
    ],
~~~

#### view中应用图片控件
~~~php
// cover中只存了一个ID,ID关联yii2_picture表
<?=$form->field($model, 'cover')->widget('\common\widgets\images\Images',[
    'saveDB'=>1, //图片是否保存到picture表，默认不保存
],['class'=>'c-md-12'])->label(Yii::t('backend','封面圖片'))->hint(Yii::t('backend','圖片尺寸').':300*300');?>
~~~
由该widget生成的html(上传按钮:file_buttom1/存放图片ID:hidden input/显示图片:file_img)
~~~html
<div class="form-group field-article-cover">
<div><label class="" for="article-cover">封面圖片</label><span class="help-inline">（圖片尺寸:300*300）</span></div><div class="c-md-12">
<!-- image表图集 -->
<div class="fileinput fileinput-new" data-provides="fileinput">
    <div style="margin-bottom:5px;">
        <span class="btn red btn-outline btn-file">
            <span class="fileinput-new"> 上传图片 </span>
            <input type="hidden" id="article-cover" name="Article[cover]" value="20">            <input type="file" name="..." class="file_buttom1">
        </span>
    </div>
    <div class="fileinput-preview thumbnail" data-trigger="fileinput" style="width: 200px; height: 150px;">
        <img class="file_img" src="/storage/image/201808/1535353946646.jpg">
    </div>
</div>
~~~


#### 加载图片控件
~~~php
$form是common\core\ActiveForm
调用field()方法, 通过 public $fieldClass = 'common\core\ActiveField'; 控制返回field为core类的field
common\core\ActiveField.php 调用 widget()方法
然后这一句: $this->parts['{input}'] = $divstring.$class::widget($config).'</div>'; 触发进入基类
vendor/yiisoft/yii2/base/Widget.php 137: $widget = Yii::createObject($config);
经过几重调用才进入common:
    vendor/yiisoft/yii2/BaseYii.php:349
    vendor/yiisoft/yii2/di/Container.php:156
    vendor/yiisoft/yii2/di/Container.php:383
    vendor/yiisoft/yii2/di/Container.php:383
    vendor/yiisoft/yii2/base/BaseObject.php:109
    common/widgets/images/Images.php:25

common/widgets/images/Images.php
// 继承InputWidget
class Images extends InputWidget
// 先执行Init()
public function init()
// 再执行run()
public function run(){
// 在run()内render页面
return $this->render($this->type,$opt);
// 图片(单图)控件页面文件(这个页面就是上面html的源码)
common/widgets/images/views/image.php
	// 其中hidden保存picture表id
	<?=Html::activeInput('hidden', $model, $attribute, ['value'=>$picture['id']])?>
	// 原有图片展现
	<img class="file_img" src="<?= !empty($picture['path']) ? \common\helpers\Html::src($picture['path']) : \yii\helpers\Url::to('@web/static/images/no.png'); ?>">
	// 其中js实现上传图片功能
	$(".file_buttom<?=$saveDB?>").on("change", function(){
	// 上传按钮的js中,读取文件成功后会post控制器方法 : /tpadmin/public/uploadimage
	backend/controllers/PublicController.php
	'uploadimage' => [
                  'class' => 'common\widgets\images\UploadAction',
              ],
    // uploadimage调用类,应该是进run()方法
    common/widgets/images/UploadAction.php
    // run()方法中调用savePic保存图片url 及 图片(imgbase64)
    $url = FuncHelper::uploadImage($imgbase64);
    public function savePic($url){
    // FuncHelper 存图片文件于服务器上storage/web/image/
    common\helpers\FuncHelper.php
    public static function uploadImage($imgbase64){

~~~

