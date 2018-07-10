## emacs

### 安装
    apt-get update (可选)
    apt-get install emacs -y



### 初学
- C 表示按下Ctrl键, M 表示按下Alt键
- Emacs快速指南: C-h t
- 光标移动上,下,左,右: C-p, C-n, C-b, C-f
- 退出: C-x C-c
- 删除一行: C-k
- 删除前一个字符：C-Backspace(老子研究了半天)
- 删除后一个字符：C-d
- 保存：C-x C-s
- 下翻一页: C-v 上翻一页: M-v(或Esc+v)
- 居中显示光标文本: C-l (多次按则依次切换中部/上部/下部)

### 基本概念
buffer是文件的内存表示, windows则是显示buffer的区域, 一个frame中可以有多个window, Emacs则可以有多个frame

- buffer
~~~
缓冲区. Emacs并不直接对文件进行操作, 它是把文件加载进buffer, 用户直接操作buffer, 只有当用户确定把buffer中所做的修改写入文件时, Emacs才把buffer中的内容写入文件. buffer实际上就是一个内存缓冲区, 这和一般编辑器中都一样.
~~~
- windows
~~~
窗口. 由于Emacs很早就诞生了, 它的窗口概念和现在基于窗口的操作系统中的窗口概念不是一样的. Emacs中的窗口是用来显示buffer的一个区域. 它并不像操作系统中的窗口拥有自己的标题栏,系统菜单栏.
~~~
- frame
~~~
Emacs中的frame就是操作系统中的窗口
~~~
- mode
~~~
mode有major mode和minor mode之分, 每个缓冲区对应一个major mode, 也只有一个major mode, 但是可以有多个minor mode. Emacs对每一种文件都有一个mode.
~~~
- 命令
~~~
你对Emacs所有的操作都是对Emacs的命令的调用。比如，你在text-mode里，当你按下任何字母键进行编辑的时候，实际上是调用的emacs的命令self-insert-command.
~~~
- 快捷键
~~~
Emacs中Control键用C表示,Alt键用M表示, 即: C-c表示Control C, M-x表示Alt x.
除掉以Alt键开头的，比如Alt a，Emacs中的快捷键基本上都有一个前缀，Emacs中最多的快捷键前缀就是C-x，C-c，前缀表示，你不必要一起按下前缀和后缀，可以先按下前缀，Emacs会等待你按下剩余的快捷键，这样Emacs中的快捷键按起来非常的方便
~~~
- keymap
~~~
键盘映射. Emacs的快捷键是通过keymap来控制的. 有全局和局部的keymap. 每个mode都会有一个自己的局部的keymap, 局部的keymap会覆盖全局的keymap, 另外如果对应的major mode有开启的minor mode, 而且这个minor mode有keymap的话, 这个minor mode的keymap会覆盖major mode的keymap.
~~~

### help文档
- 查看指南
    - C-h t
- 查看变量的值和文档
    - C-h v (describe-variable)
- 查看函数的文档
    - C-h f (describe-function)
- 查看face的文档
    - M-x describe-face
- 查看某个mode的文档
    - C-h m (describe-mode)
    - 刚开始学习某个mode的时候, 可以用C-h m看看当前buffer对应的主mode和副mode的文档, 这个文档一般都会包括mode中的命令和快捷键列表.
- 查看某个快捷键对应的命令
    - C-h k (describe-key)
- **查看某个命令对应的快捷键**
    - C-h w (where-is)
- 查看当前buffer所有的快捷键列表
    - C-h b (describe-bindings)
- 查看当前buffer中以某个快捷键序列开头的快捷键列表
    - <待查看的快捷键序列> C-h，比如你想查看当前buffer中所有以C-c开头的快捷键列表，按C-c C-h就可以了。
- 查看函数的代码
    - find-function
- 查看变量的代码
    - find-variable
- 查看face的代码
    - find-face-definition
- M-x apropos
    - 查看包含某个关键词的函数,变量,face

### 配置
    - 当你的配置出现问题时, 在Emacs启动命令后增加参数 –debug-init
