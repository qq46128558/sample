## [数据格式器](http://www.yiichina.com/doc/guide/2.0/output-formatting "http://www.yiichina.com/doc/guide/2.0/output-formatting")


#### 使用
~~~
$formatter = \Yii::$app->formatter;
// output: January 1, 2014
echo $formatter->asDate('2014-01-01', 'long');
// output: 12.50%
echo $formatter->asPercent(0.125, 2);
// output: <a href="mailto:cebe@example.com">cebe@example.com</a>
echo $formatter->asEmail('cebe@example.com'); 
// output: Yes
echo $formatter->asBoolean(true); 
// it also handles display of null values:
// output: (Not set)
echo $formatter->asDate(null); 
// 注意：formatter 组件用来格式化最终展示给用户的数据. 

// output: January 1, 2014
echo $formatter->format('2014-01-01', 'date'); 
// 你可以在第二个参数指定一个数组，这个数组提供了一些配置的参数
// 例如这个 2 就是 asPercent() 方法的 $decimals 参数
// output: 12.50%
echo $formatter->format(0.125, ['percent', 2]); 
~~~

#### 格式化时间/日期数据
~~~
默认支持一下几种格式化格式
- date: 这个变量将被格式化为日期 January 01, 2014.
- time: 这个变量将被格式化为时间 14:23.
- datetime: 这个变量将被格式化为日期+时间 January 01, 2014 14:23.
- timestamp: 这个变量将被格式化为 UNIX 时间戳 unix timestamp, 例如 1412609982.
- relativeTime: 这个变量将被格式化为人类可读的当前相对时间 1 hour ago.
- duration: 这个变量将被格式化为人类可读的时长 1 day, 2 minutes.

// ICU format
echo $formatter->asDate('now', 'yyyy-MM-dd'); // 2014-10-06
// PHP date()-format
echo $formatter->asDate('now', 'php:Y-m-d'); // 2014-10-06
~~~

#### 格式化数字
~~~
formatter 支持如下的方法
- integer: 这个变量将被格式化为整形 e.g. 42.
- decimal: 这个变量将被格式化为带着逗号的指定精度的浮点型 e.g. 2,542.123 or 2.542,123.
- percent: 这个变量将被格式化为百分比 e.g. 42%.
- scientific: 这个变量将被格式化为科学计数法 e.g. 4.2E4.
- currency: 这个变量将被格式化为货币 £420.00. 使用这个方法前请确认是否已经正确配置 locale
- size: 这个变量将被格式化为人类可读的字节数 e.g. 410 kibibytes.
- shortSize: 这个变量将被格式化为人类可读的字节数（缩写） size, e.g. 410 KiB.
~~~