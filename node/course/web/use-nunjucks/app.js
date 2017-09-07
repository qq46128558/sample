const nunjucks=require('nunjucks');

function createEnv(path,opts){
    // 创建env需要的参数可以查看文档获知
    // http://mozilla.github.io/nunjucks/
    var
        autoescape=opts.autoescape===undefined?true:opts.autoescape,
        noCache=opts.noCache||false,
        watch=opts.watch||false,
        throwOnUndefined=opts.throwOnUndefined||false,
        env=new nunjucks.Environment(
            // 创建一个文件系统加载器，从views目录读取模板
            new nunjucks.FileSystemLoader('views',{
                noCache:noCache,
                watch:watch,
            }),{
                autoescape:autoescape,
                throwOnUndefined:throwOnUndefined,
            }
        );
        if (opts.filters){
            for(var f in opts.filters){
                env.addFilter(f,opts.filters[f]);
            }
        }
        return env;
}

var env=createEnv("views",{
    watch:true,
    // 在options中自定义过滤器
    filters:{
        // 名为hex的过滤器，将n返回16进制的字符串
        hex:function(n){
            return '0x'+n.toString(16);
        }
    }
})

// 变量env就表示Nunjucks模板引擎对象
// 它有一个render(view, model)方法，正好传入view和model两个参数，并返回字符串。
// 用下面的代码来渲染这个模板
var s=env.render('hello.html',{name:'Peter'});
console.log('01.'+s);

// 咋一看，这和使用JavaScript模板字符串没啥区别嘛。不过，试试
s=env.render('hello.html',{name:'<script>alert("Peter")</script>'});
console.log('02.'+s);
// 避免了输出恶意脚本

// (模版继承)对子模板进行渲染：
s=env.render('extend.html',{
    header:'Hello',
    body:'bla bla bla...'
})
console.log('03.');
console.log(s);

// 在开发环境下，可以关闭cache，这样每次重新加载模板，便于实时修改模板。在生产环境下，一定要打开cache，这样就不会有性能问题。