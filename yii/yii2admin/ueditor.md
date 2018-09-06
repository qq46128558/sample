## [UEditor](https://ueditor.baidu.com/website/index.html "https://ueditor.baidu.com/website/index.html")富文本web编辑器

#### 相关文件
- 前端配置文件 vendor/kucha/ueditor/assets/ueditor.config.js
- 编辑器源码文件 vendor/kucha/ueditor/assets/ueditor.all.js
- widget后台入口文件 vendor/kucha/ueditor/UEditor.php
- 在后台入口文件中注册ueditor的js文件: UEditorAsset::register($this->view)
- UEditorAsset 即 endor/kucha/ueditor/UEditorAsset.php
- 前端参数: 'serverUrl' => Url::to(['/public/ueditor']) (服务器统一请求接口路径)
	- 指向控制器 backend/controllers/PublicController.php
	- ueditor方法:
		- 'class' => 'common\actions\UEditorAction',
 		- 'config' => Yii::$app->params['ueditorConfig'],
 	- 指向 common/actions/UEditorAction.php 文件
 	- 基类 vendor/kucha/ueditor/UEditorAction.php
 	- 读取 config配置与后端配置文件 vendor/kucha/ueditor/config.php 合并



#### view中前端配置参数
~~~php
<?=$form->field($model, 'content_cn')->widget('\kucha\ueditor\UEditor',
[
    'clientOptions' => [
    ...
    ]
],
['class'=>'','style'=>'display:none']
)->label();

// 其中clientOptions中可配置各参数
// toolbars工具栏按钮,一个数组为一行, 配置项里用竖线 '|' 代表分割线
'toolbars'=>[
    ['fullscreen', 'source', '|', 'undo', 'redo', 'bold'],
    ['bold', 'italic', 'underline']
],

// 服务器统一请求接口路径
'serverUrl' => Url::to(['/public/ueditor']),
// /public/ueditor控制器 指向类 common\actions\UEditorAction 再继承 \kucha\ueditor\UEditorAction
// 编辑的语言 zh-cn中文, en英文
'lang' =>'zh-cn',
// 初始化编辑器宽度
'initialFrameWidth' => '100%',
// 初始化编辑器高度
'initialFrameHeight' => '400',
~~~

#### [前端配置项说明](http://fex.baidu.com/ueditor/#start-config "http://fex.baidu.com/ueditor/#start-config")

#### 备用配置摘录
- elementPathEnabled {Boolean} [默认值：true] //是否启用元素路径，默认是显示
- wordCount {Boolean} [默认值：true] //是否开启字数统计
- maximumWords {Number} [默认值：10000] //允许的最大字符数
- wordCountMsg {String} [默认值：] //当前已输入 {#count} 个字符，您还可以输入{#leave} 个字符，字数统计提示，{#count}代表当前字数，{#leave}代表还可以输入多少字符数，留空支持多语言自动切换，否则按此配置显示
- wordOverFlowMsg {String} [默认值：] //超出字数限制提示 留空支持多语言自动切换，否则按此配置显
- autoHeightEnabled {Boolean} [默认值：true] //是否自动长高，默认true
- scaleEnabled {Boolean} [默认值：false] //是否可以拉伸长高，默认true(当开启时，自动长高失效)


#### 完整工具栏列表
~~~
toolbars: [
    [
        'anchor', //锚点
        'undo', //撤销
        'redo', //重做
        'bold', //加粗
        'indent', //首行缩进
        'snapscreen', //截图
        'italic', //斜体
        'underline', //下划线
        'strikethrough', //删除线
        'subscript', //下标
        'fontborder', //字符边框
        'superscript', //上标
        'formatmatch', //格式刷
        'source', //源代码
        'blockquote', //引用
        'pasteplain', //纯文本粘贴模式
        'selectall', //全选
        'print', //打印
        'preview', //预览
        'horizontal', //分隔线
        'removeformat', //清除格式
        'time', //时间
        'date', //日期
        'unlink', //取消链接
        'insertrow', //前插入行
        'insertcol', //前插入列
        'mergeright', //右合并单元格
        'mergedown', //下合并单元格
        'deleterow', //删除行
        'deletecol', //删除列
        'splittorows', //拆分成行
        'splittocols', //拆分成列
        'splittocells', //完全拆分单元格
        'deletecaption', //删除表格标题
        'inserttitle', //插入标题
        'mergecells', //合并多个单元格
        'deletetable', //删除表格
        'cleardoc', //清空文档
        'insertparagraphbeforetable', //"表格前插入行"
        'insertcode', //代码语言
        'fontfamily', //字体
        'fontsize', //字号
        'paragraph', //段落格式
        'simpleupload', //单图上传
        'insertimage', //多图上传
        'edittable', //表格属性
        'edittd', //单元格属性
        'link', //超链接
        'emotion', //表情
        'spechars', //特殊字符
        'searchreplace', //查询替换
        'map', //Baidu地图
        'gmap', //Google地图
        'insertvideo', //视频
        'help', //帮助
        'justifyleft', //居左对齐
        'justifyright', //居右对齐
        'justifycenter', //居中对齐
        'justifyjustify', //两端对齐
        'forecolor', //字体颜色
        'backcolor', //背景色
        'insertorderedlist', //有序列表
        'insertunorderedlist', //无序列表
        'fullscreen', //全屏
        'directionalityltr', //从左向右输入
        'directionalityrtl', //从右向左输入
        'rowspacingtop', //段前距
        'rowspacingbottom', //段后距
        'pagebreak', //分页
        'insertframe', //插入Iframe
        'imagenone', //默认
        'imageleft', //左浮动
        'imageright', //右浮动
        'attachment', //附件
        'imagecenter', //居中
        'wordimage', //图片转存
        'lineheight', //行间距
        'edittip ', //编辑提示
        'customstyle', //自定义标题
        'autotypeset', //自动排版
        'webapp', //百度应用
        'touppercase', //字母大写
        'tolowercase', //字母小写
        'background', //背景
        'template', //模板
        'scrawl', //涂鸦
        'music', //音乐
        'inserttable', //插入表格
        'drafts', // 从草稿箱加载
        'charts', // 图表
    ]
]
~~~


#### [如何使用补丁文件](http://fex.baidu.com/ueditor/#start-patch "http://fex.baidu.com/ueditor/#start-patch")
~~~html
<!--要在ueditor js下边加载相应的patch文件-->
<script type="text/javascript" charset="utf-8" src="ueditor-patch-149.js"></script>
~~~



#### [编辑后端配置参数](http://fex.baidu.com/ueditor/#server-config "http://fex.baidu.com/ueditor/#server-config")
~~~php
// 配置文件
vendor/kucha/ueditor/config.php
// yii2 admin配置位置 (由前端参数serverUrl指向的控制器加载)
common/config/params.php
	'ueditorConfig'=>[]

// 常用参数
// 上传图片给返回的路径添加指定的前缀
imageUrlPrefix 
// 上传文件大小限制 单位为B 默认2048000(2M)
imageMaxSize
// 上传文件格式控制
imageAllowFiles 
// 图片上传保存路径
imagePathFormat 
~~~



#### [上传路径配置](http://fex.baidu.com/ueditor/#server-path "http://fex.baidu.com/ueditor/#server-path")



#### ueditor的请求
~~~php
// 所有请求向serverUrl的控制器 public/ueditor 发起, 再通过它分发到其他 php 脚本执行

// 测试
http://47.106.160.48/tpadmin/public/ueditor
// 返回 {"state": "请求地址出错"} 表示正常

// 请求配置信息
http://47.106.160.48/tpadmin/public/ueditor?action=config
// 对应代码 common/actions/UEditorAction.php 文件
// 基类: vendor/kucha/ueditor/UEditorAction.php
protected function handleAction()
{   
    $action = Yii::$app->request->get('action');
    switch ($action) {
        case 'config':
            $result = json_encode($this->config);
            break;
            ...
~~~


#### [常用API](http://fex.baidu.com/ueditor/#api-common "http://fex.baidu.com/ueditor/#api-common")
