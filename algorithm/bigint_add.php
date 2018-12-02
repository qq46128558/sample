<?php 
// 如何实现大整数相加: 使用数组存储每一位数(或每几位数)
// 原始代码未优化

// 生成两个大整数(100位)并存入数组
$max=100;
foreach (range(1,$max) as $i) {
	if ($i==1){
		$big1[]=mt_rand(1,9);
		$big2[]=mt_rand(1,9);
	}else{
		$big1[]=mt_rand(0,9);
		$big2[]=mt_rand(0,9);
	}
}
print_r(str_pad(implode('',$big1),$max+1," ",STR_PAD_LEFT));
echo "\n+\n";
print_r(str_pad(implode('',$big2),$max+1," ",STR_PAD_LEFT));
echo "\n=\n";

// 1把整数倒序存储，整数的个位存于数组0下标位置
$big1_reverse=array_reverse($big1);
$big2_reverse=array_reverse($big2);
// 2创建结果数组
$max=count($big1_reverse)>count($big2_reverse)?count($big1_reverse):count($big2_reverse);
$result=range(1,$max);
for ($i=0; $i < $max; $i++) { 
	$result[$i]=0;
}
// 2结果数组的最大长度是较大整数的位数+1
$result[]=0;
// 3遍历两个数组，从左到右按照对应下标把元素两两相加，就像小学生计算竖式一样。
for ($i=0; $i < $max; $i++) { 
	$result[$i]+=$big1_reverse[$i]+$big2_reverse[$i];
	if ($result[$i]>=10){
		$result[$i]=$result[$i]-10;
		$result[$i+1]=1;
	}
}
// 把Result数组的全部元素再次逆序，去掉首位的0(若有)，就是最终结果
if ($result[$max]==0) array_pop($result);
$result=array_reverse($result);
print_r(str_pad(implode('', $result),$max+1," ",STR_PAD_LEFT));