<?php
require_once(__DIR__."/jos-php-open-api-sdk-2.0/jd/JdClient.php");
require_once(__DIR__."/jos-php-open-api-sdk-2.0/jd/request/ActyQueryRegistrationDataCountRequest.php");

$app_key='5EC3009052005867E016BE59E6AA2D90';
$app_secret='9eb78cd1d9ef4816a853ead79b59ce96';
$access_token='35edcec6-5906-4ce6-ad50-f553de8ff284';

$c = new \JdClient();
$c->appKey = $app_key;
$c->appSecret = $app_secret;
$c->accessToken = $access_token;
$c->serverUrl = "https://api.jd.com/routerjson";
$req = new \ActyQueryRegistrationDataCountRequest();

$req->setSkuId(""); $req->setOrderId(""); $req->setBeginDate(""); $req->setEndDate("");

$resp = $c->execute($req, $c->accessToken);
var_dump($resp);

// object(stdClass)#4 (2) { ["code"]=> string(1) "0" ["queryregistrationdatacount_result"]=> object(stdClass)#5 (2) { ["message"]=> string(31) "venderId must be greater than 0" ["resultCode"]=> int(0) } }