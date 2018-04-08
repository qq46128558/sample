## 数据提供者
数据提供者是一个实现了 yii\data\DataProviderInterface 接口的类。 它主要用于获取分页和数据排序。它经常用在 data widgets 小物件里，方便终端用户进行分页与数据排序。

- yii\data\ActiveDataProvider：使用 yii\db\Query 或者 yii\db\ActiveQuery 从数据库查询数据并且以数组项的方式或者 Active Record 实例的方式返回。
- yii\data\SqlDataProvider：执行一段SQL语句并且将数据库数据作为数组返回。
- yii\data\ArrayDataProvider：将一个大的数组依据分页和排序规格返回一部分数据。

#### 所有的这些数据提供者遵守以下模式
~~~
// 根据配置的分页以及排序属性来创建一个数据提供者
$provider = new XyzDataProvider([
    'pagination' => [...],
    'sort' => [...],
]);

// 获取分页和排序数据
$models = $provider->getModels();

// 在当前页获取数据项的数目
$count = $provider->getCount();

// 获取所有页面的数据项的总数
$totalCount = $provider->getTotalCount();
~~~