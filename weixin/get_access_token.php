<?php
// access_token是调用微信接口的唯一凭据，每两小时刷新一次，我们需要每两小时就获取一次access_token。
// 但1天内获取次数有限，开发者需自行存储

$access=new TokenUtil();
// 第一次获取用
$access->build_access_token();
// echo $access->read_token();

class TokenUtil {
    //获取access_token并保存到token.txt文件中
    public static function build_access_token(){
        $secret="f6d0edf04c31754b92e108c9fb20a180";
        $appid="wx817b492673790402";
        //初始化一个CURL对象
        $ch = curl_init(); 
        //设置你所需要抓取的URL
        curl_setopt($ch, CURLOPT_URL, "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=".$appid."&secret=".$secret);
        // 请求HTTPS协议接口api
        // 跳过证书检查
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER,0);
        // 从证书中检查SSL加密算法是否存在
        curl_setopt($ch, CURLOPT_SSL_VERIFYHOST,2);
        //设置curl参数，要求结果是否输出到屏幕上，为true的时候是不返回到网页中,假设上面的0换成1的话，那么接下来的$data就需要echo一下。
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);

        // {
        //     "access_token": "7_P3WLjzZqX-vmxzzgVHinQ6NzphQ1lx3ymjsB_L4iWiVsqbEz6IsC6oAyMTVHr79ThPlch6angEW4fCL0L1YRuNWxc9cfpt4A69eDNijkw1tnw41-9e-bFFV38x8jv6hwG5SlqmiIlObMyMRVUMHaABAJBW", 
        //     "expires_in": 7200
        // }
        $data = json_decode(curl_exec($ch));
        if($data && $data->access_token){
            //打开token.txt文件，没有会新建
            $token_file = fopen("./token.txt","w") or die("Unable to open file!");
            //重写token.txt全部内容
            fwrite($token_file,$data->access_token);
            //关闭文件流
            fclose($token_file);
        }else{
            echo $data->errmsg or die('failed to get access_token');
        }
        curl_close($ch);
    }
    
    //设置定时器，每两小时执行一次build_access_token()函数获取一次access_token
    public static function set_interval(){
        ignore_user_abort();//关闭浏览器仍然执行
        set_time_limit(0);//让程序一直执行下去
        $interval = 7200;//每隔一定时间运行
        do{
            build_access_token();
            sleep($interval);//等待时间，进行下一次操作。
        }while(true);
    }
    
    //读取token
    public static function read_token(){
        $token_file = fopen("./token.txt", "r") or die("Unable to open file!");
        $rs = fgets($token_file);
        fclose($token_file);
        return $rs;
    }
}