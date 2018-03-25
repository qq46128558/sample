

'use strict';
// 通过document.write引入需要window.onload后写代码
// 引入jquery
// document.write("<script type='text/javascript' src='./jquery-2.2.4.min.js'></script>");
// 引入jweixin
// document.write("<script type='text/javascript' src='https://res.wx.qq.com/open/js/jweixin-1.2.0.js'></script>");  
// document.write("<script type='text/javascript' src='./jweixin-1.2.0.js'></script>");  

// console定制
console.led=function(msg){
    console.log('%c%s%s%s','font-size:15px;font-bold:true;color:#00ff00;background-color:black','---',msg,'---');
}

// 需要在微信开发者工具(或微信)中才能使用微信的jssdk
// window.onload=function(){
    // 通过config接口注入权限验证配置
    var jsapilist;
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
            jsapilist=data.jsApiList;
            console.info('wx.config');
            // console.dir(data);
            wx.config({
                debug: false, // 开启调试模式,调用的所有api的返回值会在客户端alert出来，若要查看传入的参数，可以在pc端打开，参数信息会通过log打出，仅在pc端时才会打印。
                appId:data.appId, // 必填，公众号的唯一标识
                timestamp:data.timestamp, // 必填，生成签名的时间戳
                nonceStr:data.nonceStr, // 必填，生成签名的随机串
                signature:data.signature,// 必填，签名
                jsApiList:data.jsApiList // 必填，需要使用的JS接口列表
            });
        }
    ).fail(function(xhr,status)
        {console.led(status+":"+xhr.status+" " +xhr.responseText);}
    ).always(function(){});

    // 通过ready接口处理成功验证  
    // config信息验证后会执行ready方法，所有接口调用都必须在config接口获得结果之后  
    wx.ready(function(){
        console.info('wx.ready');
        // 判断当前客户端版本是否支持指定JS接口
        wx.checkJsApi({
            jsApiList: jsapilist, // 需要检测的JS接口列表，所有JS接口列表见附录2,
            // 接口调用成功时执行的回调函数
            success:function(res) {
            // 以键值对的形式返回，可用的api值true，不可用为false
            // 如：{"checkResult":{"chooseImage":true},"errMsg":"checkJsApi:ok"}
                console.info('wx.checkJsApi:success');
            },
            // 接口调用失败时执行的回调函数
            fail:function(res){
                console.info('wx.checkJsApi:fail');
                console.error(res);
            },
            // 接口调用完成时执行的回调函数，无论成功或失败都会执行
            complete:function(res){
                console.info('wx.checkJsApi:complete');
            },
            // 用户点击取消时的回调函数，仅部分有用户取消操作的api才会用到
            cancel:function(res){
                console.info('wx.checkJsApi:cancel');
            },
            // 监听Menu中的按钮点击时触发的方法，该方法仅支持Menu中的相关接口
            trigger:function(res){
                console.info('wx.checkJsApi:trigger');
            }

        });
    });
    // 通过error接口处理失败验证
    wx.error(function(res){
        console.info('wx.error');
        console.error(res.errMsg);
    });
// }


