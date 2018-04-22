## 数组助手类（ArrayHelper）

### 获取值 getValue
用原生PHP从一个对象、数组、或者包含这两者的一个复杂数据结构中获取数据是非常繁琐的。 你首先得使用 isset 检查 key 是否存在, 然后如果存在你就获取它，如果不存在， 则提供一个默认返回值

~~~
class User
{
    public $name = 'Alex';
}

$array = [
    'foo' => [
        'bar' => new User(),
    ]
];
~~~

    $value = ArrayHelper::getValue($array, 'foo.bar.name');

第二个参数指定了如何获取数据， 它可以是下述几种类型中的一个

- 数组键名或者欲从中取值的对象的属性名称；
- 以点号分割的数组键名或者对象属性名称组成的字符串，上例中使用的参数类型就是该类型；
- 返回一个值的回调函数。

回调函数如下例所示：
~~~
$fullName = ArrayHelper::getValue($user, function ($user, $defaultValue) {
    return $user->firstName . ' ' . $user->lastName;
});
~~~

第三个可选的参数如果没有给定值，则默认为 null，如下例所示
    $username = ArrayHelper::getValue($comment, 'user.username', 'Unknown');


### 设定值 setValue
~~~
$array = [
    'key' => [
        'in' => ['k' => 'value']
    ]
];

ArrayHelper::setValue($array, 'key.in', ['arr' => 'val']);
// 在 `$array` 中写入值的路径可以被指定为一个数组
ArrayHelper::setValue($array, ['key', 'in'], ['arr' => 'val']);
~~~

结果，`$array['key']['in']` 的初始值将被新值覆盖

~~~
[
    'key' => [
        'in' => ['arr' => 'val']
    ]
]
~~~

**如果路径包含一个不存在的键，它将被创建**

~~~
// 如果 `$array['key']['in']['arr0']` 不为空，则该值将被添加到数组中
ArrayHelper::setValue($array, 'key.in.arr0.arr1', 'val');

// 如果你想完全覆盖值 `$array['key']['in']['arr0']`
ArrayHelper::setValue($array, 'key.in.arr0', ['arr1' => 'val']);
~~~

结果将是

~~~
[
    'key' => [
        'in' => [
            'k' => 'value',
            'arr0' => ['arr1' => 'val']
        ]
    ]
]
~~~


### 获取并删除 remove
remove 仅支持简单的键名称
~~~
$array = ['type' => 'A', 'options' => [1, 2]];
$type = ArrayHelper::remove($array, 'type');
~~~

### 检查键名的存在
第三个参数支持大小写不敏感的键名比较
~~~
if (!ArrayHelper::keyExists('username', $data1, false) || !ArrayHelper::keyExists('username', $data2, false)) {
    echo "Please provide username.";
}
~~~

### 检索列
~~~
$data = [
    ['id' => '123', 'data' => 'abc'],
    ['id' => '345', 'data' => 'def'],
];
$ids = ArrayHelper::getColumn($array, 'id');

$result = ArrayHelper::getColumn($array, function ($element) {
    return $element['id'];
});
~~~

### 重建数组索引 index
**个人觉得像分组**

ArrayHelper::index($array,$key,$group);

~~~
$array = [
    ['id' => '123', 'data' => 'abc', 'device' => 'laptop'],
    ['id' => '345', 'data' => 'def', 'device' => 'tablet'],
    ['id' => '345', 'data' => 'hgi', 'device' => 'smartphone'],
];
$result = ArrayHelper::index($array, 'id');
~~~

结果将是一个关联数组，其中键是 id 属性的值

~~~
[
    '123' => ['id' => '123', 'data' => 'abc', 'device' => 'laptop'],
    '345' => ['id' => '345', 'data' => 'hgi', 'device' => 'smartphone']
    // 原始数组的第二个元素由于相同的 ID 而被最后一个元素覆盖
]
~~~

匿名函数作为 $key 传递，给出了相同的结果

~~~
$result = ArrayHelper::index($array, function ($element) {
    return $element['id'];
});
~~~

传递 id 作为第三个参数将 id 分配给 $array：

    $result = ArrayHelper::index($array, null, 'id');

结果将是一个多维数组，它由第一级的 id 分组，并且不在第二级索引：

~~~
[
    '123' => [
        ['id' => '123', 'data' => 'abc', 'device' => 'laptop']
    ],
    '345' => [ // all elements with this index are present in the result array
        ['id' => '345', 'data' => 'def', 'device' => 'tablet'],
        ['id' => '345', 'data' => 'hgi', 'device' => 'smartphone'],
    ]
]
~~~

匿名函数也可用于分组数组中：

~~~
$result = ArrayHelper::index($array, 'data', [function ($element) {
    return $element['id'];
}, 'device']);
~~~

结果将是一个多维数组，由第一级的 id 分组，第二级的 device 和第三级的 data 索引：

~~~
[
    '123' => [
        'laptop' => [
            'abc' => ['id' => '123', 'data' => 'abc', 'device' => 'laptop']
        ]
    ],
    '345' => [
        'tablet' => [
            'def' => ['id' => '345', 'data' => 'def', 'device' => 'tablet']
        ],
        'smartphone' => [
            'hgi' => ['id' => '345', 'data' => 'hgi', 'device' => 'smartphone']
        ]
    ]
]
~~~