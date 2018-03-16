##### 版本
    $.fn.jquery

##### 按ID获取Jquery对象(并取第1个Dom元素)
    #直接获取的是Jquery对象,get(0)再取dom元素
    $('#ID').get(0)
    #Dom元素转回Jquery对象
    $($('#ID').get(0))

##### 获得内容和属性
    $('#ID').text()
    $('#ID').html()
    $('#ID').val()
    $('#ID').attr('attributeName')