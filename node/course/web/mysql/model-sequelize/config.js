// 用config.js实现不同环境读取不同的配置文件：
const defaultConfig = './config-default.js';
// 可设定为绝对路径，如 /opt/product/config-override.js
const overrideConfig='./config-override.js';
const testConfig='./config-test.js';
const fs=require('fs');
var config=null;
if (process.env.NODE_ENV==='test'){
        console.log(`Load ${testConfig}...`);
        config=require(testConfig);
}else{
        console.log(`Load ${defaultConfig}...`);
        config=require(defaultConfig);
        try{
                if (fs.statSync(overrideConfig).isFile()){
                        console.log(`Load ${overrideConfig}...`);
                        config=Object.assign(config,require(overrideConfig));
                }
        }catch(err){
                console.log(`Cannot load ${overrideConfig}.`);
        }
}
module.exports=config;

/* 如果是测试环境，就读取config-test.js。
如果不是测试环境，
先读取config-default.js；
然后读取config-override.js，如果文件不存在，就忽略。 */

/* 这样做的好处是，开发环境下，团队统一使用默认的配置，并且无需config-override.js。部署到服务器时，由运维团队配置好config-override.js，以覆盖config-override.js的默认设置。测试环境下，本地和CI服务器统一使用config-test.js，测试数据库可以反复清空，不会影响开发。

配置文件表面上写起来很容易，但是，既要保证开发效率，又要避免服务器配置文件泄漏，还要能方便地执行测试，就需要一开始搭建出好的结构，才能提升工程能力。 */