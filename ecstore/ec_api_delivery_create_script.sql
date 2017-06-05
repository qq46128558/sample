-- 删除发货单API接口测试时生成的发货单
set @order_id='170503105491428';
update sdb_b2c_order_items set sendnum=0 where order_id=@order_id;
update sdb_b2c_orders set ship_status='0',ship_receive_status=NULL,received_status='0',received_time=null where order_id=@order_id;
delete from sdb_b2c_delivery_items where delivery_id=(select delivery_id from sdb_b2c_delivery where order_id=@order_id LIMIT 1);
delete from sdb_b2c_delivery where order_id=@order_id;
delete from sdb_b2c_order_delivery where order_id=@order_id;
delete from sdb_apiactionlog_apilog where apilog like concat('DC',@order_id,'%');
delete from sdb_apiactionlog_apilog where apilog like concat('OU',@order_id,'%');
