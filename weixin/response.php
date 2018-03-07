<?php  
define("TOKEN", "beautiful");  
$wechatObj = new wechatCallbackapiTest();
//record by peter: 有时候验证签名是错误的? 未解决.
$wechatObj->valid();  
$wechatObj->responseMsg();

// 封装类的代码实现Token验证及被动回复消息
class wechatCallbackapiTest  
{  
    private function wlog($obj,$level)
    {
	//2 error 4 info
	$currentLevel=4;
	if ($currentLevel>=$level){
		file_put_contents('all.log',var_export($obj,true),FILE_APPEND);
	}
    }

    public function valid()  
    {  
        $echoStr = $_GET["echostr"];
	$this->wlog($echoStr,4);
        if($this->checkSignature()){
            if ($echoStr){
                $this->wlog($echoStr,4);
                echo $echoStr;
                exit;
            } else{
                return;
            }
        }
	$this->wlog('Check signature failed.',2);
        exit;
    }  
  
    public function responseMsg()  
    {  
        //get post data, May be due to the different environments  
        // $postStr = $GLOBALS["HTTP_RAW_POST_DATA"];
        $postStr=file_get_contents('php://input');
        $this->wlog($postStr,4);
        // $postStr无值(php版本较低),php.ini中开启 always_populate_raw_post_data = On  
        // 还可以用file_get_contents('php://input')获取$_POST无法接收的数据类型如XML数据

        //extract post data  
        if (!empty($postStr)){  
                  
                $postObj = simplexml_load_string($postStr, 'SimpleXMLElement', LIBXML_NOCDATA);  
                $fromUsername = $postObj->FromUserName;  
                $toUsername = $postObj->ToUserName;  
                $keyword = trim($postObj->Content);  
                $msgType=$postObj->MsgType;
                $mediaid=$postObj->MediaId;
                $time = time();  
                $textTpl = "<xml>  
                            <ToUserName><![CDATA[%s]]></ToUserName>  
                            <FromUserName><![CDATA[%s]]></FromUserName>  
                            <CreateTime>%s</CreateTime>  
                            <MsgType><![CDATA[%s]]></MsgType>  
                            <Content><![CDATA[%s]]></Content>  
                            <FuncFlag>0</FuncFlag>  
                            </xml>";
                $imageTpl="<xml>
                            <ToUserName><![CDATA[%s]]></ToUserName>
                            <FromUserName><![CDATA[%s]]></FromUserName>
                            <CreateTime>%s</CreateTime>
                            <MsgType><![CDATA[image]]></MsgType>
                            <Image>
                            <MediaId><![CDATA[%s]]></MediaId>
                            </Image>
                            </xml>";
                switch ($msgType) {
                    case "text":
                        if(!empty($keyword))
                        {  
                            $msgType = "text";  
                            $contentStr = "Welcome to wechat world!";  
                            $resultStr = sprintf($textTpl, $fromUsername, $toUsername, $time, $msgType, $contentStr);  
                            echo $resultStr;  
                        }else{  
                            echo "success";  
                        };
                        break;
                    case "image":
                        $result = sprintf($imageTpl, $fromUsername, $toUsername, $time, $mediaid);  
                        echo $result;
                        break; 
                        
                }
  
        }else {  
            echo "success";  
            exit;  
        }  
    }  
          
    private function checkSignature()  
    {  
	$this->wlog($_GET,4);
        $signature = $_GET["signature"];  
        $timestamp = $_GET["timestamp"];  
        $nonce = $_GET["nonce"];      
                  
        $token = TOKEN;  
        $tmpArr = array($token, $timestamp, $nonce);  
        sort($tmpArr);  
        // sort($tmpArr, SORT_STRING);
        $tmpStr = implode( $tmpArr );  
        $tmpStr = sha1( $tmpStr );  
        
        $this->wlog($tmpStr,4);
        if( $tmpStr == $signature ){  
            return true;  
        }else{  
            return false;  
        }  
    }  
}  
  

