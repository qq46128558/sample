- 阿里云ubuntu服务器,防火墙端口由安全组规则控制(iptables默认无规则)

#### 查看防火墙规则
    #-L 显示规则链中已有的条目
    iptables -L
    #-n 显示规则链中已有的条目,带端口号
    iptables -L -n
    #--line-numbers 以序号显示
    iptables -L --line-nubmers

#### 清除已有规则
    iptables -F
    iptables -X
    iptables -Z

#### 将规则存入文件
    iptables-save > /etc/sysconfig/iptables.rules

#### 从文件中还原规则
    #使防火墙规则生效
    iptables-restore </etc/sysconfig/iptables.rules

#### 使开机生效
    vim /etc/network/if-pre-up.d/iptables
        #!/bin/bash
        iptables-restore </etc/sysconfig/iptables.rules
    #添加执行权限
    chmod +x /etc/network/if-pre-up.d/iptables 
    
#### 开放22端口(ssh远程)
    iptables -I INPUT -p tcp --dport 22 -j ACCEPT
    iptables-save
    #-I：向规则链中插入条目
    #-A：向规则链中追加条目
    #-p：指定要匹配的数据包协议类型
    #-j <目标>：指定要跳转的目标

#### 开放80端口(http)
    iptables -I INPUT -p tcp --dport 80 -j ACCEPT
    iptables-save

#### 查看每个链的默认规则
    iptables -S
        -P INPUT ACCEPT
        -P FORWARD ACCEPT
        -P OUTPUT ACCEPT
    #-P：定义规则链中的默认目标

#### 禁止其他未允许的规则访问
    iptables -A INPUT -j REJECT

#### 删除INPUT里序号为8的规则
    #-D：从规则链中删除条目
    iptables -D INPUT 8

#### 屏蔽IP/IP段
    #-s：指定要匹配的数据包源ip地址
    #123.45.6.1到123.45.6.254
    iptables -I INPUT -s 123.45.6.0/24 -j DROP