<?php
/**
 * 响应微信公众平台发送的信息
 */
error_reporting(E_ALL ^ E_NOTICE);

define('TOKEN','beautiful');
$wechatobj=new wechatCallbackAPI();
$value=$wechatobj->dealwithMsg();
echo $value;

function wlog($value,$level=4)
{
    //2 error 4 info
    $currentLevel=4;
    if ($currentLevel>=$level){
        file_put_contents("all.log","\n",FILE_APPEND);
		file_put_contents('all.log',$value,FILE_APPEND);
	}
}
class wechatCallbackAPI
{
    private $textTpl=<<<STR
    <xml>
    <ToUserName><![CDATA[%s]]></ToUserName>
    <FromUserName><![CDATA[%s]]></FromUserName>
    <CreateTime>%s</CreateTime>  
    <MsgType><![CDATA[%s]]></MsgType>  
    <Content><![CDATA[%s]]></Content>  
    <FuncFlag>0</FuncFlag>  
    </xml>
STR;

    private $imageTpl=<<<STR
    <xml>
    <ToUserName><![CDATA[%s]]></ToUserName>
    <FromUserName><![CDATA[%s]]></FromUserName>
    <CreateTime>%s</CreateTime>
    <MsgType><![CDATA[image]]></MsgType>
    <Image>
    <MediaId><![CDATA[%s]]></MediaId>
    </Image>
    </xml>
STR;

    // 校验是否微信发过来的消息
    private function checkSignature()  
    {  
	    wlog("$_GET:".var_export($_GET,1));
        $signature=$_GET["signature"];  
        $timestamp=$_GET["timestamp"];  
        $nonce=$_GET["nonce"];      
                  
        $token=TOKEN;  
        $tmpArr=array($token, $timestamp, $nonce);  
        // sort($tmpArr);  
        sort($tmpArr, SORT_STRING);
        $tmpStr=implode($tmpArr);  
        $tmpStr=sha1($tmpStr);  
        
        wlog("sha1:".$tmpStr);
        if($tmpStr==$signature){  
            return true;  
        }else{  
            return false;  
        }  
    }

    public function dealwithMsg()
    {
        $echoStr=$_GET["echostr"];
        wlog('echoStr:'.$echoStr);
        //是否微信服务器调用
        if (!$this->checkSignature()){
            return 'Not from wechat.';
        }

        //是否微信服务器的token验证
        if ($echoStr){
            return $echoStr;
        }

        //其他消息处理
        $postStr=file_get_contents('php://input');
        wlog("Post Data:".var_export($postStr,1));

        //解释post过来的xml
        if (empty($postStr)){
            return 'Post data empty.';
        }

        $postObj=simplexml_load_string($postStr, 'SimpleXMLElement', LIBXML_NOCDATA);
        $msgType=$postObj->MsgType;
        wlog("MsgType:".$msgType);

        $fromUsername=$postObj->FromUserName;
        $toUsername=$postObj->ToUserName;  
        $content=trim($postObj->Content);
        $mediaId=$postObj->MediaId;
        $time = time();
        
        switch($msgType){
            case "text":
                if (empty($content)){return 'success';}
                $contentStr="Welcome to wechat world!";
                $resultStr=sprintf($this->textTpl, $fromUsername, $toUsername, $time, $msgType, $contentStr);  
                return  $resultStr;
            case "image":
                $result = sprintf($this->imageTpl, $fromUsername, $toUsername, $time, $mediaId);  
                return  $result;
        }
        return "success";
    }
}