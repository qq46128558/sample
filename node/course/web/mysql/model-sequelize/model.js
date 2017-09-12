// 导入model
/* 要使用Model，就需要引入对应的Model文件，例如：User.js。一旦Model多了起来，如何引用也是一件麻烦事。
自动化永远比手工做效率高，而且更可靠。我们写一个model.js，自动扫描并导入所有Model： */
const fs=require('fs');
const db=require('./db');
let files=fs.readdirSync(__dirname+'/models');
// 第二个参数files:
// 可选。对象作为该执行回调时使用，传递给函数，用作 "this" 的值。
// 如果省略了 thisValue ，"this" 的值为 "undefined"
// an object to which the this keyword can refer in the callbackfn function.
let js_files=files.filter((f)=>{
    return f.endsWith('.js');
},files);
module.exports={};
for (let f of js_files){
    console.log(`Import model from field ${f}...`);
    let name=f.substring(0,f.length-3);
    module.exports[name]=require(__dirname+'/models/'+f);
}
module.exports.sync=()=>{
    db.sync();
    // return db.sync();
}


// 这样，需要用的时候，写起来就像这样：
/* const model = require('./model');

let
    Pet = model.Pet,
    User = model.User;

var pet = await Pet.create({ ... }); */

