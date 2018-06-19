## BBC商派认证准备

#### widgets
~~~
如何制作一个挂件
- 新建挂件目录public/themes/模版名称/widgets/helloworld
- 建立挂件定义文件widgets.php
- 进入模板管理,选择一个页面,源码编辑>>在某个位置,增加<{widgets id="test"}
- 可视化编辑>>可以看到多了一个框,添加挂件>>选择新增的挂件HelloWorld
- 增加一个配置页面文件_config.html, 这个配置页面文件会呈现在后台挂件编辑里面
- 加入控制程序, 新建文件 
theme_widget_helloworld.php
<?php
function theme_widget_helloworld(&$setting,&$system){
    return '<b style="color:red">'.$setting['inputtext1'].'</b>';
}
- 新建挂件页面文件default.html, 让它输出通过php控制程序修改过的文字
<h1>Hello:<{$data}></h1>
- 清除模板缓存或维护.即可看到效果: Hello:红色文字

挂件文件结构说明
widgets
    comment：某一挂件目录。
        images：图片目录。
            icon.jpg：挂件对应logo图片
        _config.html：配置页面文件.
        default.html：挂件页面文件
        theme_widget_comment.php:挂件页面控制程序(获取数据操作)。
        widgets.php：挂件定义文件。
        theme_widget_cfg_<挂件目录名>.php：配置页面控制程序(即获取系统的某些数据抛到_config.html页面，命名应与内部代码函数名保持一致)。
        _preview.html: 预览文件,可选,主要是用来在后台模板编辑器里面可以显示预览的内容.

挂件相关数据表
site_widgets: 挂件表, id,app,theme,name信息.
site_widgets_instance: 挂件实例表. params字段存有配置页面文件_config.html中, 用户录入的值.
~~~


#### Template
~~~
模板位置
    public/themes/
    pc端>>luckymall
    移动端>>mobilemall
~~~

#### Model
~~~
客开的model 继承dbeav_model 再继承base_db_model 实现base_interface_model接口
model文件位置：app/应用名称/model/目录(可选)/模型名称.php
获取model：app::get('应用名称')->model('模型名称')
model的方法：
    getList($cols='*', $filter=array(), $offset=0, $limit=-1, $orderBy=null), 查找数据
    count($filter=null);合计记录数
    get_schema(); 获取dbschema目录中类定义的数组
    getRow($cols='*', $filter=array(), $orderType=null), 查找一行
    _filter($filter = array()), 数据过滤
    insert(&$data), 插入数据
    delete($filter,$subSdf = 'delete'),删除数据
    update($data,$filter=array(),$mustUpdate = null), 更新数据
    save(&$data,$mustUpdate = null, $mustInsert=false), 保存数据
    dump($filter,$field = '*',$subSdf = null), 查找关联数据
    searchOptions(),返回简单搜索项, 就是dbschema中带searchtype的
~~~

#### Route
~~~
路由文件：bootstrap/routes.php
路由配置如：route::get('topics-{cat_id}.html', [ 'as' => 'topc.topics', 'uses' => 'topc_ctl_topics@index' ]);
    应用topc
    控制器topics
    index入口方法
~~~

#### Middleware
~~~

~~~

#### Event
~~~
订阅事件
应用程序中订阅事件：event::listen('user.login', 'pam_events_listeners_loginLog', 'sync', 5);
    //参数1: 订阅的事件
    //参数2: 事件触发后执行的类&方法
    //参数3: 同步执行还是异步执行
    //参数4: 执行的优先级, 数值越大越先执行, 默认0
配置文件中订阅事件config/events.php
    //触发事件后执行被监听的任务
    //第一个参数为执行任务的执行类和方法 执行方法未指定则默认为handle
    //第二个参数设置该任务为同步执行还是异步执行
    //第三个参数为执行任务的优先级，数值越大则越先执行，相同等级则按照顺序执行 默认为0 此处无
    //指定参数 queue 对应为该任务异步执行的队列 默认为system_tasks_events 此处无
    'test' => [
        ['system_events_listeners_testSync', 'sync'],
        ['system_events_listeners_testAsync@test', 'async'],
    ],

触发事件
    $response = event::fire('test', array(['key1'=>'value1','key2'=>'value2']) );

停止继续传递事件
    监听方法中返回false

异步执行需实现 base_events_interface_queue 接口

我的理解
    1.使用 event::listen('test', function ($data) 订阅了"test事件".
    2.test事件触发后, 先进入到订阅的function中.
    3.function中的第一个参数$data, 由test事件触发时传入.
    4.使用 event::fire('test', array(['key1'=>'value1','key2'=>'value2']) ); 单独触发test事件.
    5.同时test事件也会触发配置文件(config/events.php )中订阅的事件.
    6.触发事件结束后, 整个过程结束.
~~~

#### Queue
~~~
创建一个队列
    - 创建一个类,继承base_task_abstract,实现base_interface_task接口,如
        class system_tasks_testSendSms extends base_task_abstract implements base_interface_task {
            exec($params=null) 具体执行队列方法
            getDelayTime() 定义队列执行失败后重试的延时时间 默认为300秒
            getTries() 定义队列可以重试次数，默认为5次
    - 在base_crontab表中增加队列的执行周期
    - crontab * * * * * 分别代表：分 时 日 月 周

队列默认配置文件为config/queue.php

单个队列推送
    queue::push($exchange_name, $worker, $params);
    queue::push('emailbus_tasks_sendemail', 'emailbus_tasks_sendemail', array('tel'=>'18888888888', 'content'=>'幸运用户您好，你中奖了！'));

批量推送
    queue::bulk($workers, $params);
    queue::bulk(array('emailbus_tasks_sendemail', 'emailbus_tasks_sendSms'), array('tel'=>'18888888888', 'email'=>'888888@qq.com', 'content'=>'幸运用户您好，你中奖了！'));

事件方式推送
    queue::action($action, $params);
~~~ 


#### Api
~~~
API接口路由：config/apis.php
路由配置如: 'api.test'=>array('uses'=>'sysitem_api_test@index','version'=>['v1']),
    应用sysitem
    控制器test
    index入口方法

创建一个Api接口
    - 在客开目录, 增加文件: custom/sysitem/api/test.php
        $apiDescription, 表示api接口名称
        getParams(), 用于返回对入口参数的描述
        定义入口方法, 名称可自定义, 如index
    - 修改配置文件, config/apis.php 注册一个接口
         'routes' => array(
               'api.test'=>array('uses'=>'sysitem_api_test@index','version'=>['v1']),

调用Api接口
    - 内部调用：$showapi=app::get('sysitem')->rpcCall('api.test',$data);
    - 外部调用
        method：api.test
        url：xxxx/index.php/api
        sign：用token+传入参数按签名算法计算
        post请求调用
~~~

