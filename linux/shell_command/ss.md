ss命令用来显示处于活动状态的套接字信息。ss命令可以用来获取socket统计信息，它可以显示和netstat类似的内容。但ss的优势在于它能够显示更多更详细的有关TCP和连接状态的信息，而且比netstat更快速更高效。

#### 如果TCP连接队列溢出，有哪些指标可以看
    ss -lnt
    State       Recv-Q Send-Q      Local Address:Port                     Peer Address:Port
    LISTEN      0      50                    :::3306                               :::*
    Send-Q 值是50，表示listen端口上的全连接队列最大为50，Recv-Q为全连接队列当前使用了多少
    
    -l, --listening     display listening sockets
    -n, --numeric       don't resolve service names
    -t, --tcp           display only TCP sockets
