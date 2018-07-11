#### 查看当前使用的别名
    alias

#### 设置一个别名
    alias `aliasName`='`shellCommand`'
    如
    alias ll='ls -alF'
    #临时生效

#### 删除别名
    unalias `aliasName`
    如
    unalias ll
    
#### 设置别名的文件位置
    #环境变量配置文件
    #永久生效
    ~/.bashrc
    
    #其实.bashrc由.profile调用
    # ~/.profile: executed by Bourne-compatible login shells.
    if [ "$BASH" ]; then
    if [ -f ~/.bashrc ]; then
        . ~/.bashrc
    fi
    fi

    mesg n || true