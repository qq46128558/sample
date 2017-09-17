MVVM是Model-View-ViewModel的缩写。
Tim Berners-Lee发明了超文本标记语言（HyperText Markup Language），简称HTML
动态生成不同的html文件。一个最直接的想法就是利用C、C++这些编程语言，直接向浏览器输出拼接后的字符串。这种技术被称为CGI：Common Gateway Interface。
在ASP中，一个asp文件就是一个HTML，但是，需要替换的变量用特殊的<%=var%>标记出来了，再配合循环、条件判断，创建动态HTML就比CGI要容易得多。
但是，一旦浏览器显示了一个HTML页面，要更新页面内容，唯一的方法就是重新向服务器获取一份新的HTML内容。如果浏览器想要自己修改HTML页面的内容，就需要等到1995年年底，JavaScript被引入到浏览器。

用JavaScript在浏览器中操作HTML，经历了若干发展阶段：
第一阶段，直接用JavaScript操作DOM节点，使用浏览器提供的原生API：
var dom = document.getElementById('name');
dom.innerHTML = 'Homer';
dom.style.color = 'red';
第二阶段，由于原生API不好用，还要考虑浏览器兼容性，jQuery横空出世，以简洁的API迅速俘获了前端开发者的芳心：
$('#name').text('Homer').css('color', 'red');
第三阶段，MVC模式，需要服务器端配合，JavaScript可以在前端修改服务器渲染后的数据。
MVVM最早由微软提出来，它借鉴了桌面应用程序的MVC思想，在前端页面中，把Model用纯JavaScript对象表示，View负责显示，两者做到了最大限度的分离。

改变JavaScript对象的状态，会导致DOM结构作出对应的变化！这让我们的关注点从如何操作DOM变成了如何更新JavaScript对象的状态，而操作JavaScript对象比DOM简单多了！

这就是MVVM的设计思想：关注Model的变化，让MVVM框架去自动更新DOM的状态，从而把开发者从操作DOM的繁琐步骤中解脱出来！

目前，常用的MVVM框架有：
Angular：Google出品，名气大，但是很难用；
Backbone.js：入门非常困难，因为自身API太多；
Ember：一个大而全的框架，想写个Hello world都很困难。
我们选择MVVM的目标应该是入门容易，安装简单，能直接在页面写JavaScript，需要更复杂的功能时又能扩展支持。
所以，综合考察，最佳选择是尤雨溪大神开发的MVVM框架：Vue.js

MVVM最大的优势是编写前端逻辑非常复杂的页面，尤其是需要大量DOM操作的逻辑，利用MVVM可以极大地简化前端页面的逻辑。
对于以展示逻辑为主的页面，例如，新闻，博客、文档等，不能使用MVVM展示数据，因为这些页面需要被搜索引擎索引，而搜索引擎无法获取使用MVVM并通过API加载的数据。
所以，需要SEO（Search Engine Optimization）的页面，不能使用MVVM展示数据。不需要SEO的页面，如果前端逻辑复杂，就适合使用MVVM展示数据，例如，工具类页面，复杂的表单页面，用户登录后才能操作的页面等等。
