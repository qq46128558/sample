

'use strict';
// 引入jquery
document.write("<script type='text/javascript' src='./jquery-2.2.4.min.js'></script>");
// 引入jweixin
// document.write("<script type='text/javascript' src='https://res.wx.qq.com/open/js/jweixin-1.2.0.js'></script>");  
document.write("<script type='text/javascript' src='./jweixin-1.2.0.js'></script>");  

// console定制
console.led=function(msg){
    console.log('%c%s%s%s','font-size:15px;font-bold:true;color:#00ff00;background-color:black','---',msg,'---');
}

window.onload=function(){
    // 通过config接口注入权限验证配置
    $.ajax(
        {
            url:"./wxhelper.php",
            method:"post",
            dataType:"json",
            data:{'url':location.href},
            async:false,
        }
    ).done(function(data)
        {
            console.info(data);
        }
    ).fail(function(xhr,status)
        {console.led(status+":"+xhr.status+" " +xhr.responseText);}
    ).always(function(){});
}