####比较同一文件不同版本的差异
git diff `commit-id1` `commit-id2` -- `filename`


####diff结果说明
diff --git a/test.php b/test.php

--- a/test.php :表示-符号代表a版本, 即前面的版本.

+++ b/test.php: 表示+符号代表b版本, 即后面的版本.

-与+不代表增加与删除, 只代表两个版本的内容对比, 一般旧版写前面(a位置), 新版写后面(b位置)


####对比工作区与版本库(包括stage)的文件的区别
git diff `filename`

