#####改变数据库字符集,使支持unicode
ALTER DATABASE `database` CHARACTER SET=utf8mb4 COLLATE=utf8mb4\_unicode\_ci;

#####改变表字符集,使支持unicode
ALTER TABLE `tablename` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4\_unicode\_ci;

#####改变字段字符集,使支持unicode
ALTER TABLE `tablename` CHANGE `fieldname` `fieldname` `fieldtype` CHARACTER SET utf8mb4 COLLATE utf8mb4\_unicode\_ci;

- CHARACTER SET 字符集
- COLLATE 排序规则


