<?php
require_once __DIR__.'/../../b2b2c/bootstrap/autoload.php';
require_once __DIR__.'/../../b2b2c/bootstrap/start.php';

$queue_params=array(
        'filter'=>array(),
        'app_id'=>'system',
        'model'=>'system_mdl_adminlog',
        'filetype'=>'xls',//csv,xls
        'policy'=>'ftp',
        //控制器,无法直接用
        //'key'=>kernel::single('importexport_controller')->gen_key(),                 
        'key'=>'export-'.time(),
);
//直接导出数据到存储服务器,需要进行存储方式配置
try{
        $result=kernel::single('importexport_tasks_runexport')->exec($queue_params);
        if ($result){
                echo '导出成功:'.$queue_params['key'].'.'.$queue_params['filetype'];
        }else{
                echo '导出失败.';
        }
}catch(Exception $e){
        echo '导出失败:'.$e->getMessage();
}
