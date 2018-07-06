const assert = require('assert');
const hello = require('../hello.js');
// 用mocha测试一个函数是非常简单的，但是，在JavaScript的世界中，更多的时候，我们编写的是异步代码，所以，我们需要用mocha测试异步函数。
// 测试异步函数，我们要传入的函数需要带一个参数，通常命名为done：
/*
it('test async function',(done)=>{
    (async function(){
        try{
            let r=await hello();
            assert.strictEqual(r,15);
            done();
        }catch(err){
            done(err);
        }
    })();
})
*/

// 但是用try...catch太麻烦。还有一种更简单的写法，就是直接把async函数当成同步函数来测试：
describe('#async hello', () => {
    describe('#asyncCalculate()', () => {
        it('#async function', async () => {
            // var err;
            // try {
                let r = await hello();
                assert.strictEqual(r, 15);
            // } catch (e) {
            //     err = e;
            // }
            // assert(err);
            // assert.strictEqual(err.message, 'io error');
        })
    })
})

// 编写异步代码时，我们要坚持使用async和await关键字，这样，编写测试也同样简单。