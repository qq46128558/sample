## 多语言实现记录


#### 方法一: 单表加字段
	比如分类表的标题(title)需要实现多语言,则增加相应的语言字段即可,如title_cn, title_en
	目前由于太平项目多语言的扩展性要求不高, 需要加多语言的字段不多, 建议使用此方法.

#### 方法二: 语言对照表
	增加一张语言对照表, 对前端需要呈现多语言的资源, 以录入此表并翻译相应的多语言. 这也是Yii::t()进行多语言切换的使用的方式.(但对应文章这种类型的字段,翻译不太方便)

#### 方法三: Trl多语言表
	用友U9使用的方式, 在Yii2Admin上也验证通过.相应修改记录如下:
~~~
1. 对应增加业务表的Trl表,如yii2_article_cat_trl
2. 字段有:id/main_id/title/flag
3. 增加对应模型:\common\modelsgii\ArticleCatTrl
4. 控制器增加相应处理:
	findTrlModel($main_id,$flag='zh-cn')
	保存待业务表保存成功后, 再保存多语言信息,如:
	saveTrlRow($model,$model1,$model2,$data)
	$data2=array(
        'main_id'=>$model->id,
        'title'=>$data['title2'],
        'flag'=>'en-us',
    );
    $this->saveRow($model2,$data2);
5. render时传入多语言model
6. view中呈现多语言字段
	<?=$form->field($model2, 'title')->textInput(['class'=>'form-control c-md-2','name'=>'ArticleCat[title2]'])->label(Yii::t('backend','名稱(英)'))->hint('')?>
~~~

