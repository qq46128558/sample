## 主题
主题是一种将当前的一套视图 views 替换为另一套视图，而无需更改视图渲染代码的方法。 你可以使用主题来系统地更改应用的外观和体验。

#### 主题继承

有的时候，你可能想要定义一个基本的主题，其中包含一个基本的应用外观和体验，**然后根据当前的节日，你可能想要稍微地改变一下外观和体验** 。 这个时候，你就可以使用主题继承实现这一目标，主题继承是通过一个单视图路径去映射多个目标， 例如，

~~~
'pathMap' => [
    '@app/views' => [
        '@app/themes/christmas',
        '@app/themes/basic',
    ],
]
~~~

在这种情况下，视图 @app/views/site/index.php 将被主题化成 @app/themes/christmas/site/index.php 或者 @app/themes/basic/site/index.php， **这取决于哪个主题文件存在。假如都存在，那么第一个将被优先使用**。在现实情况中， 你会将大部分的主题文件放在 @app/themes/basic 里，而一些自定义的放在 @app/themes/christmas里。