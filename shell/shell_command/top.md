## top 性能分析工具
- 一个动态显示过程,即可以通过用户按键来不断刷新当前状态.
- 如果在前台执行该命令,它将独占前台,直到用户终止该程序为止.
- 比较准确的说,top命令提供了实时的对系统处理器的状态监视.
- 它将显示系统中CPU最“敏感”的任务列表.
- 该命令可以按CPU使用.内存使用和执行时间对任务进行排序；而且该命令的很多特性都可以通过交互式命令或者在个人定制文件中进行设定.

### 信息说明
~~~
top - 17:43:23 up 2 days,  4:00,  1 user,  load average: 0.08, 0.02, 0.01
~~~
- 当前时间
- 系统运行时间 时:分
- 当前登录用户数
- 系统负载, 即任务队列的平均长度. 分别是1min,5min,15min前到现在的平均值

~~~
Tasks: 107 total,   2 running, 105 sleeping,   0 stopped,   0 zombie
~~~
- 进程总数
- 

### 键盘操作
- q: 退出

