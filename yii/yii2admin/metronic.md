## metronic 4.5.6

#### 修改后台色彩主题
    backend\assets\LayoutAsset.php
    public $css = ['layouts/layout/css/themes/darkblue.min.css',];

#### 修改组件的边角样式
    backend\assets\LayoutAsset.php
    public $css = ['global/css/components-md.min.css',];

#### 使用自定义样式
    <!-- 修改文件 -->
    common\metronic\layouts\layout\css\custom.css
    <!-- 再压缩成min.css -->
    common\metronic\layouts\layout\css\custom.min.css

#### 如何查找页面元素使用哪些样式?
    - 使用Chrome浏览器>>F12开发者工具
    - ctrl+shift+c定位元素
    - 然后在Elements页签Styles窗口中观察样式(并操作变化)

#### common\metronic\global\css\components-md.css
    <!-- 内容边框的各个间距 -->
    .portlet
    .portlet > .portlet-title {
    .portlet.light > .portlet-title > .actions {
    .portlet.light.portlet-fit > .portlet-title {
    .portlet.light.portlet-fit > .portlet-body {
    .portlet.light.portlet-datatable.portlet-fit > .portlet-body {
    .table-scrollable {
    <!-- 后台表格字体大小 -->
    .table td,
    .table th {
    <!-- 操作按钮的大小 -->
    .btn:not(.md-skip).btn-xs {

#### common\metronic\global\plugins\datatables\plugins\bootstrap\datatables.bootstrap.css
    <!-- 后台表格行间距 -->
    table.table-bordered.dataTable tbody th, table.table-bordered.dataTable tbody td {
    <!-- 后台表格标题间距 -->
    table.table-bordered.dataTable th, table.table-bordered.dataTable td

#### common\metronic\global\plugins\bootstrap\css\bootstrap.css
    <!-- 一般编辑控件间距及大小 -->
    .form-group {
    .form-control {