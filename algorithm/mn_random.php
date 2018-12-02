<?php
/**
 * https://blog.csdn.net/llfdhr/article/details/53330841
 * PHP高效产生m个n范围内的不重复随机数（m<=n)
 * 场景案例：抽奖
 * 
 */

 
 /**
  * 该算法非常巧妙的取随机数的位置（数组的下标），替代取随机数本身，每次取到一个随机数之后，就将其在取值范围中排除，下一次仅会在剩下的数字中取，一次遍历就可以完成随机数的选取，效率相当高。
  * @var $n 数的范围，下限
  * @var $m 随机选的数
  */
 function getRandomArray($n,$m){
    // 如果$m>=$n，则不随机，直接返回全部数
    if ($m>=$n) return range(1,$n);
    // 如果同一时间多次执行，则不能调用make_seed，否则有可能是相同的随机数
    // mt_srand(make_seed());
    // 返回的数组中从 start 到 end （含 start 和 end）的单元
    $base=range(1,$n);
    // 循环个数
    for($i=0;$i<$m;$i++){
        // 生成随机数($base数组的上下标)(如果随机数为$i,应该是没交换到)
        $rand=mt_rand($i,$n-1);
        // 如果为初始值
        if($base[$i]==$i+1){
            // 则交换值
            $base[$i]=$base[$rand];
            $base[$rand]=$i+1;
        }
        $sift[]=$base[$i];
    }
    return $sift;
 }

 function make_seed ()
 {
    list( $usec ,  $sec ) =  explode ( ' ' ,  microtime ());
    return (float)  $sec  + ((float)  $usec  *  100000 );
 }

 // for($i=0;$i<10;$i++){
    echo implode(getRandomArray(100,5),',').'</br>';
 // }