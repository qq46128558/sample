<?php
try{
        $host="127.0.0.1:3306";
        $dbname="information_schema";
        $user="root";
        $password="root";
        $pdb=new PDO("mysql:host=$host;dbname=$dbname",$user,$password); 
        echo 'Connect succeed.'.'<br>';
         
        /* $result=$pdb->query('select * from schemata')->fetchAll();
        foreach($result as $k=>$v){
                echo $v['SCHEMA_NAME']."<br>";
        } */
       
}catch(Exception $ex){
        echo $ex->getMessage();
}