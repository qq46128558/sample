// 定义model
// db.js的作用就是统一Model的定义：
// 每个Model必须遵守一套规范：

/* 统一主键，名称必须是id，类型必须是STRING(50)；
主键可以自己指定，也可以由框架自动生成（如果为null或undefined）；
所有字段默认为NOT NULL，除非显式指定；
统一timestamp机制，每个Model必须有createdAt、updatedAt和version，分别记录创建时间、修改时间和版本号。其中，createdAt和updatedAt以BIGINT存储时间戳，最大的好处是无需处理时区，排序方便。version每次修改时自增 */

const Sequelize = require('sequelize');
const uuid=require('node-uuid');
const config=require('./config');
console.log('init sequelize...');
function generateId(){
    return uuid.v4();
}
var sequelize = new Sequelize(config.database, config.username, config.password, {
    host: config.host,
    dialect: config.dialect,
    pool: {
        max: 5,
        min: 0,
        idle: 10000
    }
})

const ID_TYPE = Sequelize.STRING(50);
function defineModel(name,attributes){
    var attrs={};
    for (let key in attributes){
        let value=attributes[key];
        if (typeof value==='object' && value['type']){
            value.allowNull=value.allowNull||false,
            attrs[key]=value;
        }else{
            attrs[key]={
                type:value,
                allowNull:false
            }
        }
    }
    attrs.id={
        type:ID_TYPE,
        primaryKey:true
    }
    attrs.createdAt={
        type:Sequelize.BIGINT,
        allowNull:false
    }
    attrs.updatedAt={
        type:Sequelize.BIGINT,
        allowNull:false
    }
    attrs.version={
        type:Sequelize.BIGINT,
        allowNull:false
    }

    console.log('Model defined for table: ' + name + '\n' + JSON.stringify(attrs, function (k, v) {
        if (k === 'type') {
            for (let key in Sequelize) {
                if (key === 'ABSTRACT' || key === 'NUMBER') {
                    continue;
                }
                let dbType = Sequelize[key];
                if (typeof dbType === 'function') {
                    if (v instanceof dbType) {
                        if (v._length) {
                            return `${dbType.key}(${v._length})`;
                        }
                        return dbType.key;
                    }
                    if (v === dbType) {
                        return dbType.key;
                    }
                }
            }
        }
        return v;
    }, '  '));

    return sequelize.define(name,attrs,{
        tableName:name,
        timestamps:false,
        hooks:{
            beforeValdate:function(obj){
                let now=Date.now();
                if (obj.isNewRecord){
                    console.log('Will create entity...'+ojb);
                    if (!obj.id){
                        obj.id=generateId();
                    }
                    obj.createdAt=now;
                    obj.updatedAt=now;
                    obj.version=0;
                }else{
                    console.log('Will update entity...');
                    obj.updatedAt=now;
                    obj.version++;
                }
            }
        }
    })
}
// 定义的defineModel就是为了强制实现上述规则。
// Sequelize在创建、修改Entity时会调用我们指定的函数，这些函数通过hooks在定义Model时设定。我们在beforeValidate这个事件中根据是否是isNewRecord设置主键（如果主键为null或undefined）、设置时间戳和版本号。

/* 注意到我们其实不需要创建表的SQL，因为Sequelize提供了一个sync()方法，可以自动创建数据库。这个功能在开发和生产环境中没有什么用，但是在测试环境中非常有用。测试时，我们可以用sync()方法自动创建出表结构，而不是自己维护SQL脚本。这样，可以随时修改Model的定义，并立刻运行测试。开发环境下，首次使用sync()也可以自动创建出表结构，避免了手动运行SQL的问题。 */
const TYPES=['STRING','INTEGER','BIGINT','TEXT','DOUBLE','DATEONLY','BOOLEAN'];
var exp={
    defineModel:defineModel,
    sync:()=>{
        // only allow create ddl in non-production environment:
        if (process.env.NODE_ENV!=='production'){
            sequelize.sync({force:true});
            // return sequelize.sync({force:true});
        }else{
            throw new Error('Cannot sync() when NODE_ENV is set to \'production\'.');
        }
    }
}

for (let type of TYPES){
    exp[type]=Sequelize[type];
}

exp.ID=ID_TYPE;
exp.generateId=generateId;

module.exports=exp;