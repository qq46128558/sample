#### 版本
    $.fn.jquery

#### 按ID获取Jquery对象(并取第1个Dom元素)
    #直接获取的是Jquery对象,get(0)再取dom元素
    $('#ID').get(0)
    #Dom元素转回Jquery对象
    $($('#ID').get(0))

#### 获得内容和属性
    $('#ID').text()
    $('#ID').html()
    $('#ID').val()
    $('#ID').attr('attributeName')

#### 修改内容和属性
    $('#ID').text('修改内容')
    $('#ID').attr('attributeName','修改属性')

#### 操作元素的Style属性
    $("p").css("color");  //获取p元素的样式颜色
    $("p").css("color","red");  //设置p元素的样式颜色为红色
    $("p").css({"fontSize":"30px" ,"backgroundColor":"#ccc"})；

#### 判断Checkbox的勾选值
    $("#checkboxID").prop('checked');
    $("#checkboxID").is(':checked');
    $("#checkboxID").get(0).checked;
    // checkbox未选中, 则post不传值
    
#### 给Checkbox加Click和Change事件
    $("#checkboxID").change(function() { 
        alert("checked"); 
    });

#### 选取指定ID:top-alert的类名为alert-content的子元素
    $('#top-alert .alert-content').text('abc')

#### 选取指定tag指定class的元素
    // <ul class="page-sidebar-menu page-header-fixed hidden-sm hidden-xs"...
    $('ul.page-sidebar-menu.page-header-fixed.hidden-sm.hidden-xs')


#### 取label标签下for属性为article-content的子节点a的文本
    //<label class="" for="article-content">文章內容<a href="javascript:void(0)" onclick="switchContent('_cn')">(隐藏)</a></label>
    $('label[for=article-content] a').text()

#### 取目标的上层节点
    $('#article-content_cn').parent()