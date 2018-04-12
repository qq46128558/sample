## 防止 XSS 攻击

#### 你希望数据以纯文本输出
    <?= \yii\helpers\Html::encode($username) ?>

#### 你希望数据以 HTML 形式输出
    <?= \yii\helpers\HtmlPurifier::process($description) ?>
    <!-- 注意： HtmlPurifier 帮助类的处理过程较为费时，建议增加缓存 -->


