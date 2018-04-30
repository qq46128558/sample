## Canvas

- 绘图环境的save()方法会将当前的绘图环境压入堆栈顶部。对应的restore()方法则会从堆栈顶部弹出一组状态信息，并根据此恢复当前绘图环境的各个状态。这意味着可以嵌套式地调用save()/restore()方法。

- 在canvas规范书中，将canvas元素的实现者称为User Agent(UA)，而非浏览器(browser)，因为任何软件都可以实现canvas元素的功能，并不是只有browser才行。
