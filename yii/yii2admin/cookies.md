## cookies 应用

#### js传值到php
~~~
// 通过ajax传值(jquery)
$.get('<?=\yii\helpers\Url::toRoute("index/savecookie");?>',{
                      'local_pagerows':parseInt((window.innerHeight-60-170-44)/29),
                  }); 

// 通过ajax传值XMLHttpRequest
var request=new XMLHttpRequest();
var rows=parseInt((window.innerHeight-60-170-44)/29);
request.open('GET','<?=\yii\helpers\Url::toRoute("index/savecookie");?>?local_pagerows='+rows)
request.send();

// php的savecookie方法
public function actionSavecookie(){
        $params=Yii::$app->request->get();
        $cookies = Yii::$app->response->cookies;
        if (is_array($params)){
            foreach ($params as $name=>$value){
                $cookies->add(new \yii\web\Cookie([
                    'name'=>$name,
                    'value'=>$value,
                ]));
            }
        }
    }

// php中取cookie值
$cookies=Yii::$app->request->cookies;                                                    
$rows=$cookies->getValue('local_pagerows','20');
$dataProvider->getPagination()->setPageSize($rows);
~~~