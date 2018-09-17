## CSS知识点记录

#### 使div固定(如侧边菜单栏)不随滚动条移动
~~~
style="position: fixed;"
如下:
<ul class="page-sidebar-menu  page-header-fixed hidden-sm hidden-xs  " data-keep-expanded="false" data-auto-scroll="true" data-slide-speed="200" style="padding-top: 20px; position: fixed; width: 17.4%;">
<div class="page-sidebar navbar-collapse collapse" style="position:fixed;z-index:999;">
~~~


#### 控制指定类标签不显示下划线
~~~
/* 导航菜单a标签不显示下划线 */
.tp-a-adjust-nounderline:hover{
    text-decoration:none;
}
~~~