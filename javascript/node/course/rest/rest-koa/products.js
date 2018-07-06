// 为了操作Product，我们用products.js封装所有操作，可以把它视为一个Service：
var id=0;
function nextId(){
    id++;
    return 'p'+id;
}

function Product(name, manufacturer,price){
    this.id=nextId();
    this.name=name;
    this.manufacturer=manufacturer;
    this.price=price;
}

// 变量products相当于在内存中模拟了数据库，这里是为了简化逻辑。
var products=[
    new Product('iPhone 7','Apple',6800),
    new Product('Thinkpad T440','Lenovo',5999),
    new Product('LBP2900','Canon',1099)
];

module.exports={
    getProducts:()=>{
        return products;
    },
    getProduct:(id)=>{
        for (var i = 0; i < products.length; i++) {
            if (products[i].id===id){
                return producst[i];
            }
        }
        return null;
    },
    createProduct:(name,manufacturer,price)=>{
        var p=new Product(name,manufacturer,price);
        products.push(p);
        return p;
    },
    deleteProduct:(id)=>{
        var index=-1;
        for (var i = 0; i < products.length; i++) {
            if (products[i].id===id){
                index=i;
                break;
            }
        }
        if (index>=0){
            // remove products[index]:
            // splice()方法是修改Array的“万能方法”，它可以从指定的索引开始删除若干元素，然后再从该位置添加若干元素,后面的[0]表示取删除的第一个元素
            return products.splice(index,1)[0];
        }
        return null;
    }
}