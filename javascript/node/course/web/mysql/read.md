MySQL官方网站下载,MySQL Community Server 5.6，这个版本是免费的，其他高级版本是要收钱的
https://dev.mysql.com/downloads/mysql/

在Windows上，安装时请选择UTF-8编码，以便正确地处理中文。
在Mac或Linux上，需要编辑MySQL的配置文件，把数据库默认的编码全部改为UTF-8。MySQL的配置文件默认存放在/etc/my.cnf或者/etc/mysql/my.cnf：
[client]
default-character-set = utf8

[mysqld]
default-storage-engine = INNODB
character-set-server = utf8
collation-server = utf8_general_ci

如果MySQL的版本≥5.5.3，可以把编码设置为utf8mb4，utf8mb4和utf8完全兼容，但它支持最新的Unicode标准，可以显示emoji字符。

test数据库是MySQL安装后自动创建的用于测试的数据库

目前使用最广泛的MySQL Node.js驱动程序是开源的mysql，可以直接使用npm安装。
如果直接使用mysql包提供的接口，我们编写的代码就比较底层，例如，查询代码：
connection.query('SELECT * FROM users WHERE id = ?', ['123'], function(err, rows) {
    if (err) {
        // error
    } else {
        for (let row in rows) {
            processRow(row);
        }
    }
});

ORM技术
Object-Relational Mapping，把关系数据库的表结构映射到对象上
选择Node的ORM框架Sequelize来操作数据库,Sequelize帮我们把对象变成数据库中的行
Sequelize返回的对象是Promise，所以我们可以用then()和catch()分别异步响应成功和失败
Pet.findAll()
   .then(function (pets) {
       for (let pet in pets) {
           console.log(`${pet.id}: ${pet.name}`);
       }
   }).catch(function (err) {
       // error
   });
但是用then()和catch()仍然比较麻烦。有没有更简单的方法呢？
可以用ES7的await来调用任何一个Promise对象
var pets = await Pet.findAll();
await只有一个限制，就是必须在async函数中调用
(async () => {
    var pets = await Pet.findAll();
})();