# seq

seq命令用于产生从某个数到另外一个数之间的所有整数。

## 语法

* seq [选项]... 尾数
* seq [选项]... 首数 尾数
* seq [选项]... 首数 增量 尾数

## 选项

* -f, --format=格式        使用printf 样式的浮点格式
* -s, --separator=字符串   使用指定字符串分隔数字（默认使用：\n）
* -w, --equal-width        在列前添加0 使得宽度相同

## 实例

### 产生100个1M的临时文件

	seq -w 1 100|xargs -n1 -i dd if=/dev/zero of=tempfile_{}.log bs=1M count=1