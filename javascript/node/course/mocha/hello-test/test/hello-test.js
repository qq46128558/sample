// mocha默认会执行test目录下的所有测试，不要去改变默认目录。
const assert=require('assert');
const sum=require('../hello.js');
describe('#hello.js',()=>{
    describe('#sum()',()=>{
        // 在测试前初始化资源，测试后释放资源是非常常见的。mocha提供了before、after、beforeEach和afterEach来实现这些功能。
        before(function(){
            console.log('Before...');
        });
        after(function(){
            console.log('After...');
        });
        beforeEach(function(){
            console.log("   Beforeeach...");
        });
        afterEach(function(){
            console.log("   Aftereach...");
        });

        
        it('sum() should return 0',()=>{
            assert.strictEqual(sum(),0);
        });
        it('sum(1) should return 1',()=>{
            assert.strictEqual(sum(1),1);
        });
        it ('sum(1,2) should return 3',()=>{
            assert.strictEqual(sum(1,2),3);
        });
        it ('sum(1,2,3) should return 6',()=>{
            assert.strictEqual(sum(1,2,3),6);
        });
    })
})
// 这里我们使用mocha默认的BDD-style的测试。describe可以任意嵌套，以便把相关测试看成一组测试。
// 每个it("name", function() {...})就代表一个测试
// 编写测试的原则是，一次只测一种情况，且测试代码要非常简单。我们编写多个测试来分别测试不同的输入，并使用assert判断输出是否是我们所期望的。

/*
如何运行？有三种方法。
方法一，可以打开命令提示符，切换到hello-test目录，然后执行命令：
C:\...\hello-test> node_modules\mocha\bin\mocha
方法二，我们在package.json中添加npm命令：
"scripts": {
    "test": "mocha"
  },
  然后在hello-test目录下执行命令：
  C:\...\hello-test> npm test
方法三,是配置launch.json,未测试通.
*/