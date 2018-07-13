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