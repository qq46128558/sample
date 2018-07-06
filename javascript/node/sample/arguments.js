// 读取js方法中的参数值
'use strict';

function getInfo(){
    console.info(arguments);
}

getInfo(1,'Peter',true,undefined,null);
