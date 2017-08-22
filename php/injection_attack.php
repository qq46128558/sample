<?php
/**
 * 防止XSS攻击,安全过滤函数
 * @param $string
 * @return string
 */
function xss_replace($string) {
    $string = str_replace('%20','',$string);
    $string = str_replace('%27','',$string);
    $string = str_replace('%2527','',$string);
    $string = str_replace('*','',$string);
    $string = str_replace('"','&quot;',$string);
    $string = str_replace("'",'',$string);
    $string = str_replace('"','',$string);
    $string = str_replace(';','',$string);
    $string = str_replace('<','&lt;',$string);
    $string = str_replace('>','&gt;',$string);
    $string = str_replace("{",'',$string);
    $string = str_replace('}','',$string);
    $string = str_replace('\\','',$string);
    return $string;
}

/**
 * 防sql注入字符串转义,同时调用了防止XSS攻击方法
 * @param $content 要转义内容
 * @return array|string
 */
function ia_replace($content) {
    $pattern = "/(select[\s])|(insert[\s])|(update[\s])|(delete[\s])|(from[\s])|(where[\s])|(drop[\s])/i";
    if (is_array($content)) {
        foreach ($content as $key=>$value) {
        	$content[$key]=htmlspecialchars($content[$key]);
            //$content[$key] = mysql_real_escape_string($value);
            /*addslashes() 函数返回在预定义字符之前添加反斜杠的字符串。 预定义字符是： 单引号（'） 双引号（"） 反斜杠（\） NULL */
            $content[$key] = addslashes(trim($value));
            if(preg_match($pattern,$content[$key])) {
                $content[$key] = '';
            }
            $content[$key]=xss_replace($content[$key]);
        }
    } else {
    	$content=htmlspecialchars($content);
        //$content=mysql_real_escape_string($content);
        $content=addslashes(trim($content));
        if(preg_match($pattern,$content)) {
            $content = '';
        }
        $content=xss_replace($content);
    }
    return $content;
}


echo '<br>01.'.ia_replace('<script>alert("abc");</script>');
echo '<br>02.'.ia_replace('delete from base_setting');
echo '<br>03.'.ia_replace('SQL XSS 防注入测试.');

