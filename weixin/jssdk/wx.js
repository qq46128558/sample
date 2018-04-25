

'use strict';
// 通过document.write引入需要window.onload后写代码
// 引入jquery
// document.write("<script type='text/javascript' src='./jquery-2.2.4.min.js'></script>");
// 引入jweixin
// document.write("<script type='text/javascript' src='https://res.wx.qq.com/open/js/jweixin-1.2.0.js'></script>");  
// document.write("<script type='text/javascript' src='./jweixin-1.2.0.js'></script>");  

// console定制
console.led=function(msg){
    console.log('%c---%s---','font-size:15px;font-bold:true;color:#00ff00;background-color:black',msg);
}

// 需要在微信开发者工具(或微信)中才能使用微信的jssdk
// window.onload=function(){
    // 通过config接口注入权限验证配置
    var jsapilist;
    var title='蟹宝盒';
    var imgUrl='https://plugs.yn-ce.com/ynbox/wx/img/links.png';
    var link="http://ser.yn-ce.com";
    var desc="这里是分享描述";

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
        /* 基础接口 */
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

        /* 分享接口 */
        // 获取“分享到朋友圈”按钮点击状态及自定义分享内容接口
        wx.onMenuShareTimeline({
            title: title, // 分享标题
            link: link, // 分享链接，该链接域名或路径必须与当前页面对应的公众号JS安全域名一致
            imgUrl: imgUrl, // 分享图标
            success: function () {
                // 用户确认分享后执行的回调函数
                console.log('wx.onMenuShareTimeline:success');
                alert('分享成功');
            },
            cancel: function () {
                // 用户取消分享后执行的回调函数
                console.log('wx.onMenuShareTimeline:cancel');
            }
        });

        // 获取“分享给朋友”按钮点击状态及自定义分享内容接口
        wx.onMenuShareAppMessage({
            title: title, // 分享标题
            desc: desc, // 分享描述
            link: link, // 分享链接，该链接域名或路径必须与当前页面对应的公众号JS安全域名一致
            imgUrl: imgUrl, // 分享图标
            type: '', // 分享类型,music、video或link，不填默认为link
            dataUrl: '', // 如果type是music或video，则要提供数据链接，默认为空
            success: function () {
                // 用户确认分享后执行的回调函数
                console.log('wx.onMenuShareTimeline:success');
                alert('分享成功');
            },
            cancel: function () {
                // 用户取消分享后执行的回调函数
                console.log('wx.onMenuShareTimeline:cancel');
            }
        });

        // 获取“分享到QQ”按钮点击状态及自定义分享内容接口
        wx.onMenuShareQQ({
            title: title, // 分享标题
            desc: desc, // 分享描述
            link: link, // 分享链接
            imgUrl: imgUrl, // 分享图标
            success: function () {
                // 用户确认分享后执行的回调函数
                console.log('wx.onMenuShareQQ:success');
                // 会先弹出这个提示,所以注释
                // alert('分享成功');
            },
            cancel: function () {
                // 用户取消分享后执行的回调函数
                console.log('wx.onMenuShareQQ:cancel');
            }
        });

        // 未有此菜单
        // 获取“分享到腾讯微博”按钮点击状态及自定义分享内容接口
        wx.onMenuShareWeibo({
            title: title, // 分享标题
            desc: desc, // 分享描述
            link: link, // 分享链接
            imgUrl: imgUrl, // 分享图标
            success: function () {
                // 用户确认分享后执行的回调函数
                console.log('wx.onMenuShareWeibo:success');
                alert('分享成功');
            },
            cancel: function () {
                // 用户取消分享后执行的回调函数
                console.log('wx.onMenuShareWeibo:cancel');
            }
        });

        // 获取“分享到QQ空间”按钮点击状态及自定义分享内容接口
        wx.onMenuShareQZone({
            title: title, // 分享标题
            desc: desc, // 分享描述
            link: link, // 分享链接
            imgUrl: imgUrl, // 分享图标
            success: function () {
                // 用户确认分享后执行的回调函数
                console.log('wx.onMenuShareQZone:success');
                // 会先弹出这个提示,所以注释
                // alert('分享成功');
            },
            cancel: function () {
                // 用户取消分享后执行的回调函数
                console.log('wx.onMenuShareQZone:cancel');
            }
        });






        // 批量隐藏功能按钮接口
        wx.hideMenuItems({
            // 发送给朋友: "menuItem:share:appMessage",分享到朋友圈: "menuItem:share:timeline",分享到QQ: "menuItem:share:qq",分享到Weibo: "menuItem:share:weiboApp",收藏: "menuItem:favorite",分享到FB: "menuItem:share:facebook",分享到 QQ 空间/menuItem:share:QZone
            // 编辑标签: "menuItem:editTag",删除: "menuItem:delete",复制链接: "menuItem:copyUrl",原网页: "menuItem:originPage",阅读模式: "menuItem:readMode",在QQ浏览器中打开: "menuItem:openWithQQBrowser",在Safari中打开: "menuItem:openWithSafari",邮件: "menuItem:share:email",一些特殊公众号: "menuItem:share:brand"
            menuList: ["menuItem:share:facebook","menuItem:openWithQQBrowser","menuItem:openWithSafari","menuItem:share:email","menuItem:share:brand"] // 要隐藏的菜单项，只能隐藏“传播类”和“保护类”按钮，所有menu项见附录3
        });

    });
    // 通过error接口处理失败验证
    wx.error(function(res){
        console.info('wx.error');
        console.error(res.errMsg);
    });

    /* 图像接口 */
    // 拍照或从手机相册中选图接口
    // 使用Promise来异步返回
    // 调用 p=chooseImage;p.then(function(res){});
    function chooseImage(count=9){
        return new Promise(function(s,f){
            wx.chooseImage({
                count: count, // 默认9
                sizeType: ['original', 'compressed'], // 可以指定是原图还是压缩图，默认二者都有
                sourceType: ['album', 'camera'], // 可以指定来源是相册还是相机，默认二者都有
                success: function (res) {
                    var localIds = res.localIds; // 返回选定照片的本地ID列表，localId可以作为img标签的src属性显示图片
                    console.info('wx.chooseImage:success');
                    s(localIds);
                },
                fail:function(res){
                    console.info('wx.chooseImage:fail');
                    f(JSON.stringify(res));
                }
            });
        });
    }

    // 判断对象是否为数组
    var isArray = function (obj) {
        return Object.prototype.toString.call(obj) === '[object Array]';
    }

    // 预览图片接口
    function previewImage(current,urls){
        if (!isArray(urls)) {urls=[urls];}
        wx.previewImage({
            current: current, // 当前显示图片的http链接
            urls: urls, // 需要预览的图片http链接列表
            success:function(res){console.info("wx.previewImage:success");},
            fail:function(res){console.info("wx.previewImage:fail");}
        });
    }

    // 上传图片接口(单个)
    // 备注：上传图片有效期3天，可用微信多媒体接口下载图片到自己的服务器，此处获得的 serverId 即 media_id。
    function uploadImage(imageId){
        return new Promise(function(s,f){
            wx.uploadImage({
                localId: imageId.toString(), // 需要上传的图片的本地ID，由chooseImage接口获得
                isShowProgressTips: 1, // 默认为1，显示进度提示
                success: function (res) {
                    console.info("wx.uploadImage:scuuess");
                    var serverId = res.serverId; // 返回图片的服务器端ID
                    s(serverId);
                },
                fail:function(res){
                    console.info("wx.uploadImage:fail");
                    f(JSON.stringify(res));
                }
            });
        });
    }
    


// }


