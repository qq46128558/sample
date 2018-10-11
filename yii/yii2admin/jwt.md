#JWT

[yii2_jwt](https://github.com/sizeg/yii2-jwt "https://github.com/sizeg/yii2-jwt")

基于cobucci/jwt 3.2

## 基于yii2admin+layuiadmin的使用记录(参考太平项目)

1. config/main.php中增加jwt(component)

	~~~php
	'jwt'=>[
	            'class'=>'sizeg\jwt\Jwt',
	            'key'=>'secret',
	        ],
	~~~

2. 登入接口不指定认证方式,只验证密码

	~~~php
	Yii::$app->getSecurity()->validatePassword($password, $result['password']
	~~~

3. 验证密码成功则生成token

	~~~php
	// 校验通过返回token
    $signer = new Sha256();
    $token = Yii::$app->jwt->getBuilder()
                ->setIssuer('taiping') // Configures the issuer (iss claim)
                ->setAudience('taiping') // Configures the audience (aud claim)
                ->setIssuedAt(time()) // Configures the time that the token was issue (iat claim)
                ->setExpiration(time() + 3600*24*30) // Configures the expiration time of the token (exp claim)
                ->set('username', $username) // Configures a new claim, called "uid"
                ->sign($signer,Yii::$app->jwt->key) // creates a signature using "testing" as key
                ->getToken(); // Retrieves the generated token

    $response=PubFunction::layuiSuccess(['accesstoken'=>(string)$token]);
	~~~

4. 其它接口加自定义认证方式,以校验token

	~~~php
	public function behaviors(){
        $behaviors=parent::behaviors();
        $behaviors['authenticator']=['class'=>\api\modules\v1\JwtHttpTokenAuth::className(),];
        return $behaviors;
    }
	~~~

5. 自定义认证方式核心代码

	~~~php
	public function authenticate($user, $request, $response)
    {
        // edit by peter 2018-10-10 驗證token(某些http測試工具取不了access_token?)
        $token = $request->getHeaders()->get('accesstoken');
        if ($token !== null) {
            // 將string轉成object
            $token = $this->jwt->getParser()->parse($token);
            if ($token === null) {
                return null;
            }
            // 基本校驗 Validating
            $data = $this->jwt->getValidationData();
            $data->setIssuer('taiping');
            $data->setAudience('taiping');
            if (!$token->validate($data)){
                return null;
            }
            // 簽名驗證 Token signature
            $signer = new \Lcobucci\JWT\Signer\Hmac\Sha256();
            if (!$token->verify($signer, $this->jwt->key)){
                return null;
            }
            return true;
        }
        return null;
    }
	~~~


## yii2-jwt常用代码

Creating

~~~php
$token = Yii::$app->jwt->getBuilder()
            ->setIssuer('http://example.com') // Configures the issuer (iss claim)
            ->setAudience('http://example.org') // Configures the audience (aud claim)
            ->setId('4f1g23a12aa', true) // Configures the id (jti claim), replicating as a header item
            ->setIssuedAt(time()) // Configures the time that the token was issue (iat claim)
            ->setNotBefore(time() + 60) // Configures the time before which the token cannot be accepted (nbf claim)
            ->setExpiration(time() + 3600) // Configures the expiration time of the token (exp claim)
            ->set('uid', 1) // Configures a new claim, called "uid"
            ->getToken(); // Retrieves the generated token


$token->getHeaders(); // Retrieves the token headers
$token->getClaims(); // Retrieves the token claims

echo $token->getHeader('jti'); // will print "4f1g23a12aa"
echo $token->getClaim('iss'); // will print "http://example.com"
echo $token->getClaim('uid'); // will print "1"
echo $token; // The string representation of the object is a JWT string (pretty easy, right?)
~~~

Parsing from strings

~~~php
$token = Yii::$app->jwt->getParser()->parse((string) $token); // Parses from a string
$token->getHeaders(); // Retrieves the token header
$token->getClaims(); // Retrieves the token claims

echo $token->getHeader('jti'); // will print "4f1g23a12aa"
echo $token->getClaim('iss'); // will print "http://example.com"
echo $token->getClaim('uid'); // will print "1"
~~~

Validating

~~~php
$data = Yii::$app->jwt->getValidationData(); // It will use the current time to validate (iat, nbf and exp)
$data->setIssuer('http://example.com');
$data->setAudience('http://example.org');
$data->setId('4f1g23a12aa');

var_dump($token->validate($data)); // false, because we created a token that cannot be used before of `time() + 60`

$data->setCurrentTime(time() + 60); // changing the validation time to future

var_dump($token->validate($data)); // true, because validation information is equals to data contained on the token

$data->setCurrentTime(time() + 4000); // changing the validation time to future

var_dump($token->validate($data)); // false, because token is expired since current time is greater than exp
~~~

Token signature

~~~php
use Lcobucci\JWT\Signer\Hmac\Sha256;

$signer = new Sha256();

$token = Yii::$app->jwt->getBuilder()
            ->setIssuer('http://example.com') // Configures the issuer (iss claim)
            ->setAudience('http://example.org') // Configures the audience (aud claim)
            ->setId('4f1g23a12aa', true) // Configures the id (jti claim), replicating as a header item
            ->setIssuedAt(time()) // Configures the time that the token was issue (iat claim)
            ->setNotBefore(time() + 60) // Configures the time before which the token cannot be accepted (nbf claim)
            ->setExpiration(time() + 3600) // Configures the expiration time of the token (exp claim)
            ->set('uid', 1) // Configures a new claim, called "uid"
            ->sign($signer, 'testing') // creates a signature using "testing" as key
            ->getToken(); // Retrieves the generated token


var_dump($token->verify($signer, 'testing 1')); // false, because the key is different
var_dump($token->verify($signer, 'testing')); // true, because the key is the same
~~~

## 经验记录

1. yii2框架下request组件读不了headers内的access_token, 后来改为accesstoken则可以读取到

	~~~php
	$token = $request->getHeaders()->get('accesstoken');
	~~~

2. 自定义认证方式中的返回处理,通过修改$response,控制返回值

	~~~html
	<!-- 自定义认证方式:继承yii\filters\auth\AuthMethod -->
	class JwtHttpTokenAuth extends AuthMethod

	<!-- 调用接口时首先进入authenticate -->
	public function authenticate($user, $request, $response)

	<!-- authenticate中返回null则调用challenge和handleFailure -->
	~~~

	~~~php
	public function challenge($response)
    {
        $response->getHeaders()->set(
            'WWW-Authenticate',
            "{$this->schema} realm=\"{$this->realm}\", error=\"invalid_token\", error_description=\"The access token invalid or expired\""
        );
    }

    public function handleFailure($response){
        // 簽名證書已失效,使layui logout
        $response->format=\yii\web\Response::FORMAT_JSON;
        $response->data=array('msg'=>Yii::t('common','簽名證書不正確或已失效,請重新登錄'),'code'=>1001,'data'=>null);
        // throw new \yii\web\UnauthorizedHttpException(\Yii::t('api','請求的證書簽名無效'));
        
    }
    ~~~
