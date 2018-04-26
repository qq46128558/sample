

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


        /* 音频接口 */
        // 监听录音自动停止接口
        // 未完善
        wx.onVoiceRecordEnd({
            // 录音时间超过一分钟没有停止的时候会执行 complete 回调
            complete: function (res) {
                console.info('wx.onVoiceRecordEnd:complete');
                var localId = res.localId;
            }
        });

        // 监听语音播放完毕接口
        // 未测试
        wx.onVoicePlayEnd({
            success: function (res) {
                console.info('wx.onVoicePlayEnd:success');
                var localId = res.localId; // 返回音频的本地ID
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
    // weixin://resourceid/295c2d51e54988ee6200bcb26e883a2b
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

    // 预览图片接口 http
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
    // Cc0T6MuZVwe9keFD2r7Vh7fIfKgq0kg4_lr4Gbpyp2RJklJVtuK9dPjsG8B-fjw9
    function uploadImage(localId){
        return new Promise(function(s,f){
            wx.uploadImage({
                localId: localId.toString(), // 需要上传的图片的本地ID，由chooseImage接口获得
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
    
    // 下载图片接口
    function downloadImage(serverId){
        return new Promise(function(s,f){
            wx.downloadImage({
                serverId: serverId, // 需要下载的图片的服务器端ID，由uploadImage接口获得
                isShowProgressTips: 1, // 默认为1，显示进度提示
                success: function (res) {
                    console.info("wx.downloadImage:success");
                    var localId = res.localId; // 返回图片下载后的本地ID
                    s(localId);
                },
                fail:function(res){
                    console.info("wx.downloadImage:fail");
                    f(JSON.stringify(res));
                }
            });
        });
    }
    
    // 获取本地图片接口
    // 备注：此接口仅在 iOS WKWebview 下提供，用于兼容 iOS WKWebview 不支持 localId 直接显示图片的问题
    // base64数据
    function getLocalImgData(localId){
        return new Promise(function(s,f){
            wx.getLocalImgData({
                localId: localId, // 图片的localID
                success: function (res) {
                    console.info("wx.getLocalImgData:success");
                    var localData = res.localData; // localData是图片的base64数据，可以用img标签显示
                    localData="data:image/png;base64,"+localData;
                    s(localData);
                },
                fail:function(res){
                    console.info("wx.getLocalImgData:fail");
                    f(JSON.stringify(res));
                }
            });
        });
    }

    /* 音频接口 */
    // 开始录音接口
    function startRecord(){
        wx.startRecord();
    }

    // 停止录音接口
    function stopRecord(){
        return new Promise(function(s,f){
            wx.stopRecord({
                success: function (res) {
                    console.info("wx.stopRecord:success");
                    var localId = res.localId;
                    s(localId);
                },
                fail:function(res){
                    console.info("wx.stopRecord:fail");
                    f(JSON.stringify(res));
                }
            });
        });
    }
    
    // 播放语音接口
    function playVoice(localId){
        wx.playVoice({
            localId: localId // 需要播放的音频的本地ID，由stopRecord接口获得
        });
    }
    
    // 暂停播放接口
    function pauseVoice(localId){
        wx.pauseVoice({
            localId: localId // 需要暂停的音频的本地ID，由stopRecord接口获得
        });
    }
    
    // 停止播放接口
    function stopVoice(localId){
        wx.stopVoice({
            localId: localId // 需要停止的音频的本地ID，由stopRecord接口获得
        });
    }
    
    // 上传语音接口
    // 备注：上传语音有效期3天，可用微信多媒体接口下载语音到自己的服务器，此处获得的 serverId 即 media_id，参考文档 .目前多媒体文件下载接口的频率限制为10000次/天，如需要调高频率，请登录微信公众平台，在开发 - 接口权限的列表中，申请提高临时上限。
    function uploadVoice(localId){
        return new Promise(function(s,f){
            wx.uploadVoice({
                localId: localId, // 需要上传的音频的本地ID，由stopRecord接口获得
                isShowProgressTips: 1, // 默认为1，显示进度提示
                success: function (res) {
                    console.info("wx.uploadVoice:success");
                    var serverId = res.serverId; // 返回音频的服务器端ID
                    s(serverId);
                },
                fail:function(res){
                    console.info("wx.uploadVoice:fail");
                    f(JSON.stringify(res));
                }
            });
        });
    }
    
    // 下载语音接口
    function downloadVoice(serverId){
        return new Promise(function(s,f){
            wx.downloadVoice({
                serverId: serverId, // 需要下载的音频的服务器端ID，由uploadVoice接口获得
                isShowProgressTips: 1, // 默认为1，显示进度提示
                success: function (res) {
                    console.info("wx.downloadVoice:success");
                    var localId = res.localId; // 返回音频的本地ID
                    s(localId);
                },
                fail:function(res){
                    console.info("wx.downloadVoice:fail");
                    f(JSON.stringify(res));
                }
            });
        });
    }
    /* 智能接口 */
    // 识别音频并返回识别结果接口
    function translateVoice(localId){
        return new Promise(function(s,f){
            wx.translateVoice({
                localId: localId, // 需要识别的音频的本地Id，由录音相关接口获得
                isShowProgressTips: 1, // 默认为1，显示进度提示
                success: function (res) {
                    console.info("wx.translateVoice:success");
                    s(res.translateResult); // 语音识别的结果
                },
                fail:function(res){
                    console.info("wx.translateVoice:fail");
                    f(JSON.stringify(res));
                }
            });
        });
    }
    
    /* 设备信息 */
    // 获取网络状态接口
    function getNetworkType(){
        return new Promise(function(s,f){
            wx.getNetworkType({
                success: function (res) {
                    console.info("wx.getNetworkType:success");
                    var networkType = res.networkType; // 返回网络类型2g，3g，4g，wifi
                    s(networkType);
                },
                fail:function(res){
                    console.info("wx.getNetworkType:fail");
                    f(JSON.stringify(res));
                }
            });
        });
    }
    
    /* 地理位置 */
    // 获取地理位置接口
    function getLocation(){
        return new Promise(function(s,f){
            wx.getLocation({
                type: 'wgs84', // 默认为wgs84的gps坐标，如果要返回直接给openLocation用的火星坐标，可传入'gcj02'
                success: function (res) {
                    console.info("wx.getLocation:success");
                    var latitude = res.latitude; // 纬度，浮点数，范围为90 ~ -90
                    var longitude = res.longitude; // 经度，浮点数，范围为180 ~ -180。
                    var speed = res.speed; // 速度，以米/每秒计
                    var accuracy = res.accuracy; // 位置精度
                    // {"speed":"0.0","indoor_building_floor":"1000","longitude":"113.55883","latitude":"22.373041","indoor_building_type":"-1","accuracy":"30.0","indoor_building_id":"","errMsg":"getLocation:ok"}
                    s(res);
                },
                fail:function(res){
                    console.info("wx.getLocation:fail");
                    f(JSON.stringify(res));
                }
            });
        });
    }
    
    // 使用微信内置地图查看位置接口
    // 目前发现定位有偏差
    function openLocation(latitude,longitude,scale=28,infoUrl="ser.yn-ce.com",name="地图定位",address="我的位置"){
        wx.openLocation({
            latitude: latitude, // 纬度，浮点数，范围为90 ~ -90
            longitude: longitude, // 经度，浮点数，范围为180 ~ -180。
            name: name, // 位置名
            address: address, // 地址详情说明
            scale: scale, // 地图缩放级别,整形值,范围从1~28。默认为最大
            infoUrl: infoUrl // 在查看位置界面底部显示的超链接,可点击跳转
        });
    }


// }


