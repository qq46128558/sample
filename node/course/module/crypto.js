// MD5是一种常用的哈希算法，用于给任意数据一个“签名”。这个签名通常用一个十六进制的字符串表示：
// 未知为何用const
const crypto=require('crypto');
const hash=crypto.createHash('md5');
hash.update('123456');
console.log('01.md5:'+hash.digest('hex'));
// e10adc3949ba59abbe56e057f20f883e

var sha256=crypto.createHash('sha256');
sha256.update('123456');
console.log('02.sha256:'+sha256.digest('hex'));

// Hmac算法也是一种哈希算法，它可以利用MD5或SHA1等哈希算法。不同的是，Hmac还需要一个密钥：
const hmac=crypto.createHmac('sha256','secret-key');
hmac.update('123456');
console.log('03.hmac sha256:'+hmac.digest('hex'));

// AES是一种常用的对称加密算法，加解密都用同一个密钥。crypto模块提供了AES支持，但是需要自己封装好函数，便于使用：
function aesEncrypt(data,key){
    const cipher=crypto.createCipher('aes192',key);
    var crypted=cipher.update(data,'utf8','hex');
    crypted+=cipher.final('hex');
    return crypted;
}

function aesDecrypt(encrypted,key){
    const decipher=crypto.createDecipher('aes192',key);
    var decrypted=decipher.update(encrypted,'hex','utf8');
    decrypted+=decipher.final('utf8');
    return decrypted;
}

var data='This is a secret message!';
var key='secret key';
var encrypted=aesEncrypt(data,key);
var decrypted=aesDecrypt(encrypted,key);
console.log('04.Plain text:'+data);
console.log('05.Encrypted text:'+encrypted);
console.log('06.Decrypted text:'+decrypted);

// DH算法是一种密钥交换协议，它可以让双方在不泄漏密钥的情况下协商出一个密钥来。
/* 小明先选一个素数和一个底数，例如，素数p=23，底数g=5（底数可以任选），再选择一个秘密整数a=6，计算A=g^a mod p=8，然后大声告诉小红：p=23，g=5，A=8；
小红收到小明发来的p，g，A后，也选一个秘密整数b=15，然后计算B=g^b mod p=19，并大声告诉小明：B=19；
小明自己计算出s=B^a mod p=2，小红也自己计算出s=A^b mod p=2，因此，最终协商的密钥s为2。 */
// 在这个过程中，密钥2并不是小明告诉小红的，也不是小红告诉小明的，而是双方协商计算出来的。第三方只能知道p=23，g=5，A=8，B=19，由于不知道双方选的秘密整数a=6和b=15，因此无法计算出密钥2。
// xiaoming's keys:
var ming=crypto.createDiffieHellman(512);
var ming_keys=ming.generateKeys();
var prime=ming.getPrime();
var generator=ming.getGenerator();
console.log('07.Prime:'+prime.toString('hex'));
console.log('08.Generator:'+generator.toString('hex'));
// xiaohong's keys:
var hong=crypto.createDiffieHellman(prime,generator);
var hong_keys=hong.generateKeys();

// exchange and generate secret:
var ming_secret=ming.computeSecret(hong_keys);
var hong_secret=hong.computeSecret(ming_keys);

// print secret:
console.log('Secret of Xiao Ming:'+ming_secret.toString('hex'));
console.log('Secret of Xiao Hong:'+hong_secret.toString('hex'));
// 注意每次输出都不一样，因为素数的选择是随机的。
