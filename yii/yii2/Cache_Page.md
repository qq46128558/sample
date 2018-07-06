## 页面缓存 PageCahce

页面缓存指的是在服务器端缓存整个页面的内容。 随后当同一个页面被请求时，内容将从缓存中取出，而不是重新生成。

页面缓存由 yii\filters\PageCache 类提供支持，该类是一个过滤器。 它可以像这样在控制器类中使用：
~~~
public function behaviors()
{
    return [
        [
            'class' => 'yii\filters\PageCache',
            'only' => ['index'],
            'duration' => 60,
            'variations' => [
                \Yii::$app->language,
            ],
            'dependency' => [
                'class' => 'yii\caching\DbDependency',
                'sql' => 'SELECT COUNT(*) FROM post',
            ],
        ],
    ];
}
~~~

上述代码表示:
- 页面缓存只在 index 操作时启用，
- 页面内容最多被缓存 60 秒， 
- 会随着当前应用的语言更改而变化。 
- 如果文章总数发生变化则缓存的页面会失效。

页面缓存和片段缓存极其相似:
它们的主要区别是**页面缓存是由过滤器实现，而片段缓存则是一个小部件**。
