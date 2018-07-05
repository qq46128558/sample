
#### 查看系统进程的地址空间
    cat /proc/<pid>/maps

#### cpu信息
    cat /proc/cpuinfo

#### tcp建立连接,accept(全连接)队列溢出,os如何处理
    cat /proc/sys/net/ipv4/tcp_abort_on_overflow 
    - 0表示如果三次握手第三步的时候全连接队列满了那么server扔掉client 发过来的ack（在server端认为连接还没建立起来）
    - 1表示第三步的时候如果全连接队列满了，server发送一个reset包给client，表示废掉这个握手过程和这个连接（本来在server端这个连接就还没建立起来）
    ss -lnt
    # 查看队列溢出指标
    
#### tcp连接,半连接队列的大小
    cat /proc/sys/net/ipv4/tcp_max_syn_backlog
    而全连接队列的大小取决于：min(backlog, somaxconn) . backlog是在socket创建的时候传入的，somaxconn是一个os级别的系统参数