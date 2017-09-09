// 使用Sequelize操作MySQ
// 创建一个sequelize对象实例
const Sequelize = require('sequelize');
const config = require('./config');
var sequelize = new Sequelize(config.database, config.username, config.password, {
    host: config.host,
    dialect: 'mysql',
    pool: {
        max: 5,
        min: 0,
        idle: 3000
    }
})
// 定义模型Pet，告诉Sequelize如何映射数据库表
// 用sequelize.define()定义Model时，传入名称pet，默认的表名就是pets。(此处未明白)
// 第二个参数指定列名和数据类型，如果是主键，需要更详细地指定。
// 第三个参数是额外的配置，我们传入{ timestamps: false }是为了关闭Sequelize的自动添加timestamp的功能。
// 我们把通过sequelize.define()返回的Pet称为Model，它表示一个数据模型。
var Pet = sequelize.define('pet', {
    id: {
        type: Sequelize.STRING(50),
        primaryKey: true
    },
    name: Sequelize.STRING(100),
    gender: Sequelize.BOOLEAN,
    birth: Sequelize.STRING(10),
    createdAt: Sequelize.BIGINT,
    updatedAt: Sequelize.BIGINT,
    version: Sequelize.BIGINT,
}, {
        timestamps: false
    })

// 接下来，我们就可以往数据库中塞一些数据了。我们可以用Promise的方式写
var now = Date.now();
Pet.create({
    id: 'g-' + now,
    name: "Gaffey",
    gender: false,
    birth: "2007-07-07",
    createdAt: now,
    updatedAt: now,
    version: 0
}).then(function (p) {
    console.log('created.' + JSON.stringify(p));
}).catch(function (err) {
    console.log('failed:' + err);
});

// 也可以用await写
(async () => {
    var dog = await Pet.create({
        id: 'd-' + now,
        name: "Odie",
        gender: false,
        birth: "2008-08-08",
        createdAt: now,
        updatedAt: now,
        version: 0
    });
    console.log('created.' + JSON.stringify(dog));
})();

// 运行代码，可以看到Sequelize打印出的每一个SQL语句，便于我们查看
// Executing (default): INSERT INTO `pets` (`id`,`name`,`gender`,`birth`,`createdAt`,`updatedAt`,`version`) VALUES ('g-1471961204219','Gaffey',false,'2007-07-07',1471961204219,1471961204219,0);


// 查询数据时，用await写法如下
// 我们把通过Pet.findAll()返回的一个或一组对象称为Model实例，每个实例都可以直接通过JSON.stringify序列化为JSON字符串。但是它们和普通JSON对象相比，多了一些由Sequelize添加的方法，比如save()和destroy()。调用这些方法我们可以执行更新或者删除操作。
(async () => {
    // 刚新增的不会查询出来,可多运行几次看效果
    var pets = await Pet.findAll({
        where: {
            name: 'Gaffey'
        }
    });
    console.log(`find ${pets.length} pet(s):`);
    for (let p of pets) {
        console.log(JSON.stringify(p));
        console.log('update pet...');
        p.gender = true;
        p.updatedAt = Date.now();
        p.version++;
        await p.save();
        if (p.version === 3) {
            await p.destroy();
            console.log(`${p.name} was destroyed.`);
        }
    }
})();

// 如果要更新数据，可以对查询到的实例调用save()方法：
/* (async()=>{
    var p=await queryFromSomewhere();
    p.gender=true;
    p.updatedAt=Date.now();
    p.version++;
    await p.save();
})(); */

// 如果要删除数据，可以对查询到的实例调用destroy()方法：
/* (async()=>{
    var p=await queryFromSomewhere();
    await p.destroy();
})(); */

/* 使用Sequelize操作数据库的一般步骤就是：
首先，通过某个Model对象的findAll()方法获取实例；
如果要更新实例，先对实例属性赋新值，再调用save()方法；
如果要删除实例，直接调用destroy()方法。
注意findAll()方法可以接收where、order这些参数，这和将要生成的SQL语句是对应的。 */

// Sequelize的API可以参考官方文档。
// http://docs.sequelizejs.com/