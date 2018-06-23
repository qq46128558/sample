
### 隐藏linux进程的方法
    - 创建进程的时候，把pid设为0
    - 直接修改ps和top的代码
    - hook libc里的readdir和opendir等函数
    