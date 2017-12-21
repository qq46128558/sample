// js判断是否为数组的函数: isArray()
// http://www.jb51.net/article/28737.htm

var isArray = function (obj) {
    return Object.prototype.toString.call(obj) === '[object Array]';
}

console.log(isArray('abc'));
console.log(isArray(123));
console.log(isArray(['a', 'b', 'c']));

// 判断类型
var is = function (obj, type) {
    return (type === "Null" && obj === null) ||
        (type === "Undefined" && obj === void 0) ||
        (type === "Number" && isFinite(obj)) ||
        Object.prototype.toString.call(obj).slice(8, -1) === type;
}
console.log('--------');
console.log(is(123, 'Number'));
console.log(is(['a'],'Array'));
console.log(is(123, 'Array'));
console.log(is(['a'],'Number'));