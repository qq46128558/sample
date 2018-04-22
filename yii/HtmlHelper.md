## Html 帮助类
yii\helpers\Html

如果超文本标记是静态的， 那么将 PHP 和 HTML 混合在一个文件里 这种做法是非常高效的。但是，如果这些超文本标记是动态生成的，那么如果没有额外的辅助工具，这个过程将会变得复杂。 Yii 通过 HTML 帮助类来提供生成超文本标记的方法。这个帮助类包含有一系列的用于处理通用的 HTML 标签和其属性以及内容的静态方法。

### 生成标签
    <?= Html::tag('p', Html::encode($user->name), ['class' => 'username']) ?>

- 第一个参数是标签名称。
- 第二个是要装入到开始和结束标签间的内容。
- 第三个参数是一个 HTML 配置数组，或者换言之，标签属性。

### 生成 CSS 类和样式
~~~
$options = ['class' => 'btn btn-default'];

if ($type === 'success') {
    Html::removeCssClass($options, 'btn-default');
    Html::addCssClass($options, 'btn-success');
}

echo Html::tag('div', 'Pwede na', $options);

// in case of $type of 'success' it will render
// <div class="btn btn-success">Pwede na</div>
~~~

~~~
$options = ['style' => ['width' => '100px', 'height' => '100px']];

// gives style="width: 100px; height: 200px; position: absolute;"
Html::addCssStyle($options, 'height: 200px; position: absolute;');

// gives style="position: absolute;"
Html::removeCssStyle($options, ['width', 'height']);
~~~

### 标签内容的转码和解码
~~~
$userName = Html::encode($user->name);
echo $userName;

$decodedUserName = Html::decode($userName);
~~~

### 创建表单
    <?= Html::beginForm(['order/update', 'id' => $id], 'post', ['enctype' => 'multipart/form-data']) ?>

- 第一个参数为表单将要被提交的 URL 地址。它可以以 Yii 路由的形式被指定，并由 yii\helpers\Url::to() 来接收处理。
- 第二个参数是使用的方法，默认为 post 方法。
- 第三个参数为表单标签的属性数组。

    <?= Html::endForm() ?>

### 按钮
~~~
<?= Html::button('Press me!', ['class' => 'teaser']) ?>
<?= Html::submitButton('Submit', ['class' => 'submit']) ?>
<?= Html::resetButton('Reset', ['class' => 'reset']) ?>
~~~

### 输入栏
~~~
type, input name, input value, options
<?= Html::input('text', 'username', $user->name, ['class' => $username]) ?>

type, model, model attribute name, options
<?= Html::activeInput('text', $user, 'name', ['class' => $username]) ?>
~~~

如果你知道 input 类型，更方便的做法是使用以下快捷方法：

- yii\helpers\Html::buttonInput()
- yii\helpers\Html::submitInput()
- yii\helpers\Html::resetInput()
- yii\helpers\Html::textInput(), yii\helpers\Html::activeTextInput()
- yii\helpers\Html::hiddenInput(), yii\helpers\Html::activeHiddenInput()
- yii\helpers\Html::passwordInput() / yii\helpers\Html::activePasswordInput()
- yii\helpers\Html::fileInput(), yii\helpers\Html::activeFileInput()
- yii\helpers\Html::textarea(), yii\helpers\Html::activeTextarea()

~~~
<?= Html::radio('agree', true, ['label' => 'I agree']);
<?= Html::activeRadio($model, 'agree', ['class' => 'agreement'])

<?= Html::checkbox('agree', true, ['label' => 'I agree']);
<?= Html::activeCheckbox($model, 'agree', ['class' => 'agreement'])
~~~

~~~
<?= Html::dropDownList('list', $currentUserId, ArrayHelper::map($userModels, 'id', 'name')) ?>
<?= Html::activeDropDownList($users, 'id', ArrayHelper::map($userModels, 'id', 'name')) ?>

<?= Html::listBox('list', $currentUserId, ArrayHelper::map($userModels, 'id', 'name')) ?>
<?= Html::activeListBox($users, 'id', ArrayHelper::map($userModels, 'id', 'name')) ?>
~~~

~~~
<?= Html::checkboxList('roles', [16, 42], ArrayHelper::map($roleModels, 'id', 'name')) ?>
<?= Html::activeCheckboxList($user, 'role', ArrayHelper::map($roleModels, 'id', 'name')) ?>
~~~

~~~
<?= Html::radioList('roles', [16, 42], ArrayHelper::map($roleModels, 'id', 'name')) ?>
<?= Html::activeRadioList($user, 'role', ArrayHelper::map($roleModels, 'id', 'name')) ?>
~~~

### Labels 和 Errors
~~~
<?= Html::label('User name', 'username', ['class' => 'label username']) ?>
<?= Html::activeLabel($user, 'username', ['class' => 'label username']) ?>

<?= Html::errorSummary($posts, ['class' => 'errors']) ?>

<?= Html::error($post, 'title', ['class' => 'error']) ?>
~~~

### Input 的名和值
~~~
// Post[title]
echo Html::getInputName($post, 'title');

// post-title
echo Html::getInputId($post, 'title');

// my first post
echo Html::getAttributeValue($post, 'title');

// $post->authors[0]
echo Html::getAttributeValue($post, '[0]authors[0]');
~~~

在上面的例子中，第一个参数为模型，而第二个参数是属性表达式。在最简单的表单中，这个属性表达式就是属性名称，但是在一些多行输入的时候，它也可以是属性名以数组下标前缀或者后缀（也可能是同时）。

- [0]content 代表多行输入时第一个 model 的 content 属性的数据值。
- dates[0] 代表 dates 属性的第一个数组元素。
- [0]dates[0] 代表多行输入时第一个 model 的 dates 属性的第一个数组元素。

为了获取一个没有前缀或者后缀的属性名称，我们可以如下做：

~~~
// dates
echo Html::getAttributeName('dates[0]');
~~~

### 样式表和脚本
~~~
<?= Html::style('.danger { color: #f00; }') ?>

Gives you

<style>.danger { color: #f00; }</style>


<?= Html::script('alert("Hello!");', ['defer' => true]);

Gives you

<script defer>alert("Hello!");</script>
~~~

~~~
<?= Html::cssFile('@web/css/ie5.css', ['condition' => 'IE 5']) ?>

generates

<!--[if IE 5]>
    <link href="http://example.com/css/ie5.css" />
<![endif]-->
~~~

- condition 来让 `<link 被条件控制注释包裹（ IE hacker ）`。 希望你在未来不再需要条件控制注释。
- noscript 可以被设置为 true ，这样 `<link就会被 <noscript>`包裹，如此那么这段代码只有在浏览器不支持 JavaScript 或者被用户禁用的时候才会被引入进来。

外联 JavaScript 文件
    <?= Html::jsFile('@web/js/main.js') ?>

### 超链接
    <?= Html::a('Profile', ['user/view', 'id' => $id], ['class' => 'profile-link']) ?>

- 第一个参数是超链接的标题。它不会被转码，所以如果是用户输入数据， 你需要使用 Html::encode() 方法进行转码。
- 第二个参数是 `<a 标签的 href 属性的值`。 关于该参数能够接受的更详细的数据值，请参阅 Url::to()。 
- 第三个参数是标签的属性数组。

    <?= Html::mailto('Contact us', 'admin@example.com') ?>

### 图片
~~~
<?= Html::img('@web/images/logo.png', ['alt' => 'My logo']) ?>

generates

<img src="http://example.com/images/logo.png" alt="My logo" />
~~~

### 列表
~~~
<?= Html::ul($posts, ['item' => function($item, $index) {
    return Html::tag(
        'li',
        $this->render('post', ['item' => $item]),
        ['class' => 'post']
    );
}]) ?>
~~~

有序列表请使用 Html::ol() 方法。
