## OPTIMIZE TABLE 优化表
如果您已经删除了表的一大部分，或者如果您已经对含有可变长度行的表（含有VARCHAR,BLOB或TEXT列的表）进行了很多更改，则应使用OPTIMIZE TABLE。被删除的记录被保持在链接清单中，后续的INSERT操作会重新使用旧的记录位置。您可以使用OPTIMIZE TABLE来重新
利用未使用的空间，并整理数据文件的碎片。

- 在多数的设置中，您根本不需要运行OPTIMIZE TABLE 
- 即使您对可变长度的行进行了大量的更新，您也不需要经常运行，每周一次或每月一次即可
- 只对特定的表运行
- OPTIMIZE TABLE只对MyISAM, BDB和InnoDB表起作用
- 在OPTIMIZE TABLE运行过程中，MySQL会锁定表

#### 总结
	当你删除数据时，mysql并不会回收，被已删除数据的占据的存储空间，以及索引位。而是空在那里，而是等待新的数据来弥补这个空缺，这样就有一个缺少，如果一时半会，没有数据来填补这个空缺，那这样就太浪费资源了。所以对于写比较频烦的表，要定期进行optimize，一个月一次，看实际情况而定了。

#### 优化表
	OPTIMIZE TABLE `table name[,tablename]`;
	OPTIMIZE TABLE ad_visit_history;
	OPTIMIZE TABLE ad_visit_history,ad_log;