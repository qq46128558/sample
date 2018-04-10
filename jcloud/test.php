<?php
require_once(__DIR__."/jos-php-open-api-sdk-2.0/jd/JdClient.php");
require_once(__DIR__."/jos-php-open-api-sdk-2.0/jd/request/ActyQueryRegistrationDataCountRequest.php");

$app_key='5EC3009052005867E016BE59E6AA2D90';
$app_secret='9eb78cd1d9ef4816a853ead79b59ce96';
$access_token='e3202ea8-5a4d-437d-b9ce-6c6fe9f51a31';

$c = new \JdClient();
$c->appKey = $app_key;
$c->appSecret = $app_secret;
$c->accessToken = $access_token;
$c->serverUrl = "https://api.jd.com/routerjson";
// $c->serverUrl = "http://open-api.jcloud.com/routerjson";
$req = new \ActyQueryRegistrationDataCountRequest();

$req->setSkuId( 123 ); $req->setOrderId( 123 ); $req->setBeginDate( "jingdong" ); $req->setEndDate( "jingdong" );

$resp = $c->execute($req, $c->accessToken);
var_dump($resp);
