## html helper


#### 生成指定标签的html代码
	# <span style="text-align:right;display:block;">100</span>
	\yii\helpers\Html::tag('span','100',['style'=>'text-align:right;display:block;']);

#### 生成a标签
	# <a class="btn green" href="/tpadmin/article/content?id=67&type=cn" target="new">點擊查看</a>
	Html::a(Yii::t('backend','點擊查看'),['content?id='.$model['id']."&type=cn"],['class'=>'btn green','target'=>'new']);