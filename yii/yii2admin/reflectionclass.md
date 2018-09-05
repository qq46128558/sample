## [反射](https://www.cnblogs.com/KeenLeung/p/6041280.html "https://www.cnblogs.com/KeenLeung/p/6041280.html")

#### 基本应用
~~~php
$model = $this->findModel($id);
$targetmodel=null;
if ($model->model){
    $class = new \ReflectionClass("\\backend\\models\\".$model->model);
    $targetmodel=$class->newInstanceArgs();
}

// 调用
$targetmodel->is_picture($key);
$targetmodel->getPicturesrc($value);
~~~

