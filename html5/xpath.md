## XPath 语法
用于处理XML文档

- 根节点和非根节点
    - /div 选择 div 节点，只有当它是文档的根节点时
    - //div 选择文档中所有的 div 节点（包括非根节点）
- 通过属性选择节点
    - //@href 选择带 href 属性的所有节点
    - //a[@href='http://google.com'] 选择页面中所有指向 Google 网站的链接
- 通过位置选择节点
    - //a[3] 选择文档中的第三个链接
    - //table[last()] 选择文档中的最后一个表
    - //a[position() < 3] 选择文档中的前三个链接
- 星号（ * ）匹配任意字符或节点，可以在不同条件下使用
    - //table/tr/* 选择所有表格行 tr 标签的所有的子节点（这很适合选择 th 和 td 标签）
    - //div[@*] 选择带任意属性的所有 div 标签

### [微软XPath语法](https://msdn.microsoft.com/en-us/enus/library/ms256471,"https://msdn.microsoft.com/en-us/enus/library/ms256471")

