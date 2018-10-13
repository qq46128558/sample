<?php
/*PHP怎么实现字符串全排列组合？*/

$str='abc';
// 字符串转换为数组
$arr_str=str_split($str);
// 调用perm函数
perm($arr_str,0,strlen($str)-1);

/**
 * 定义perm函数
 * @param $ar // 排列的字符串,传址
 * @param $k // 初始值
 * @param $m // 最大值
 */
function perm(&$ar,$k,$m){ 
    // 初始值是否等于最大值
    if ($k==$m){
        // 将数组转换为字符串
        echo join('',$ar)," ",PHP_EOL;
    }else{
        // 循环调用函数
        for ($i=$k;$i<=$m;$i++){
            // 调用swap函数 交换位置
            swap($ar[$k],$ar[$i]);
            echo "Swap:",join('',$ar)," ";
            // 递归调用自己
            perm($ar,$k+1,$m);
            // 再次调用swap函数 还原位置
            swap($ar[$k],$ar[$i]);
            echo "Reswap:",join('',$ar)," ";

        }
    }
}

function swap(&$a,&$b){
    $c=$a;
    $a=$b;
    $b=$c;
}

