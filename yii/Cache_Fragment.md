## 片段缓存 Fragment_Caching.

片段缓存指的是缓存页面内容中的某个片段。例如，一个页面显示了逐年销售额的摘要表格， 可以把表格缓存下来，以消除每次请求都要重新生成表格的耗时。 片段缓存是基于[数据缓存](Yii__$app-cache.md "Yii__$app-cache.md")实现的。

#### 基本使用
~~~
// 在视图中使用以下结构启用片段缓存：
if ($this->beginCache($id)) {

    // ... 在此生成内容 ...

    $this->endCache();
}
// 和数据缓存一样，每个片段缓存也需要全局唯一的 $id 标记
~~~

**如果缓存中存在该内容，beginCache() 方法将渲染内容并返回 false， 因此将跳过内容生成逻辑。否则，内容生成逻辑被执行， 一直执行到endCache() 时， 生成的内容将被捕获并存储在缓存中。**


#### 缓存选项-过期时间
~~~
if ($this->beginCache($id, ['duration' => 3600])) {

    // ... 在此生成内容 ...

    $this->endCache();
}
// 如果该选项未设置，则它将采用默认值 60，这意味着缓存的内容将在 60 秒后过期
~~~

#### 缓存选项-依赖
~~~
// 以下代码指定了一个片段缓存，它依赖于 update_at 字段是否被更改过的
$dependency = [
    'class' => 'yii\caching\DbDependency',
    'sql' => 'SELECT MAX(updated_at) FROM post',
];
if ($this->beginCache($id, ['dependency' => $dependency])) {

    // ... 在此生成内容 ...

    $this->endCache();
}
~~~

#### 缓存选项-变化(未理解)
缓存的内容可能需要根据一些参数的更改而变化。 例如一个 Web 应用支持多语言，同一段视图代码也许需要生成多个语言的内容。 因此可以设置缓存根据应用当前语言而变化。

~~~
// 例如设置缓存根据当前语言而变化可以用以下代码
if ($this->beginCache($id, ['variations' => [Yii::$app->language]])) {

    // ... 在此生成内容 ...

    $this->endCache();
}
~~~

#### 缓存选项-开关
有时你可能只想在特定条件下开启片段缓存。例如，一个显示表单的页面，可能只需要在初次请求时缓存表单（通过 GET 请求）。 随后请求所显示（通过 POST 请求）的表单不该使用缓存，因为此时表单中可能包含用户输入内容。 鉴于此种情况，可以使用 enabled 选项来指定缓存开关， 如下所示：

~~~
if ($this->beginCache($id, ['enabled' => Yii::$app->request->isGet])) {

    // ... 在此生成内容 ...

    $this->endCache();
}
~~~

#### 缓存嵌套
片段缓存可以被嵌套使用。一个片段缓存可以被另一个包裹。 例如，评论被缓存在里层，同时整个评论的片段又被缓存在外层的文章中。 以下代码展示了片段缓存的嵌套使用：

如果外层片段缓存没有过期而被视为有效， 此时即使内层片段缓存已经失效，它也将继续提供同样的缓存副本。

因此，你必须谨慎处理缓存嵌套中的过期时间和依赖， 否则外层的片段很有可能返回的是不符合你预期的失效数据。

**外层的失效时间应该短于内层，外层的依赖条件应该低于内层，以确保最小的片段，返回的是最新的数据**

~~~
if ($this->beginCache($id1)) {

    // ...在此生成内容...

    if ($this->beginCache($id2, $options2)) {

        // ...在此生成内容...

        $this->endCache();
    }

    // ...在此生成内容...

    $this->endCache();
}
~~~

#### 动态内容
动态内容的意思是这部分输出的内容不该被缓存，即便是它被包裹在片段缓存中。 为了使内容保持动态，每次请求都执行 PHP 代码生成， 即使这些代码已经被缓存了。

~~~
// 可以在片段缓存中调用 yii\base\View::renderDynamic() 去插入动态内容， 如下所示：
if ($this->beginCache($id1)) {

    // ...在此生成内容...

    echo $this->renderDynamic('return Yii::$app->user->identity->name;');

    // ...在此生成内容...

    $this->endCache();
}
// renderDynamic() 方法接受一段 PHP 代码作为参数。 代码的返回值被看作是动态内容。这段代码将在每次请求时都执行， 无论其外层的片段缓存是否被存储。
~~~

从版本 2.0.14 开始，动态内容 API 通过 yii\base\DynamicContentAwareInterface 接口及其 yii\base\DynamicContentAwareTrait 特质开放。 可以参考 yii\widgets\FragmentCache 类。
