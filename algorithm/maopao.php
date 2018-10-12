<?php
/* PHP冒泡排序算法是怎么实现的 */

// 升序排列指的就是从小到大排列，就如同泉水冒泡的现象
// 将值小的数据移至在前面，值大的数据就放在后面。
$arr=[6,2,4,8,5,9,7,1,3,8];
$len=count($arr);
$innerlen=$len-1;
// 将数组转换为字符串显示
echo join('',$arr),PHP_EOL;

// 第一个for循环来控制数据比较的轮次数
for ($i=0;$i<$len;$i++){
    // 第二个for循环来控制次数并判断大小交换位置
    for ($j=0;$j<$innerlen;$j++){
        if ($arr[$j]>$arr[$j+1]){
            // 通过$temp变量交换位置
            $temp=$arr[$j];
            $arr[$j]=$arr[$j+1];
            $arr[$j+1]=$temp;
        }
    }
}

echo join('',$arr);
// 6248597138
// 1234567889