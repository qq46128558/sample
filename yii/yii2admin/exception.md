## 异常处理
error handler 错误处理器默认启用， 可通过在应用的入口脚本中定义常量YII_ENABLE_ERROR_HANDLER来禁用


#### 所有异常进入此文件
~~~php
// 用try捕获的异常也进入此处,暂未理清楚
vendor/yiisoft/yii2/base/ErrorHandler.php
	public function handleException($exception)
		$this->renderException($exception);
// render页面时进入此文件
vendor/yiisoft/yii2/web/ErrorHandler.php
	protected function renderException($exception)

// 根据条件判断返回404页面或错误的response
// 配置文件中的404页面:'errorHandler' => ['errorAction' => 'public/404',],
$result = Yii::$app->runAction($this->errorAction);

// 或者直接返回response(需要在浏览器开发者工具的network>>response中查看)
$response->data = '<pre>' . $this->htmlEncode(static::convertExceptionToString($exc    eption)) . '</pre>';
$response->send();
~~~

经验证可以在 vendor/yiisoft/yii2/base/ErrorHandler.php 中加入写异常的日志记录,示例如:
~~~php
\common\core\PubFunction::exceptionAdminLog($exception->getMessage());

// Undefined constant 'Yii\db\ActiveRecord'
$exception->getMessage()
// 0
$exception->getCode()
// /data/www/yii/backend/controllers/BaseController.php
$exception->getFile()
// 123
$exception->getLine()
// array
$exception->getTrace()
// 其他(未验证)
// $exception->getString()
// $exception->getPrevious()
// $exception->getXdebug_message()
~~~





#### 捕获异常注意事项
~~~php
//a文件: 
function a() {
  throw new \yii\web\HttpException('我是数据库异常');
}
//b文件:
use yii\db\Exception;
try{
  a();
}
catch(Exception $e)
{
  echo "捕获到异常了";
}
然而并没有输出捕获到异常了，因为catch的Exception实际指的是捕获yii\db\Exception抛出的异常，不能捕获HttpException抛出的异常。

yii中所有异常都是继承于Exception，所以有两种改写方法:
catch(\yii\web\HttpException $e)
catch(\Exception $e)
~~~
