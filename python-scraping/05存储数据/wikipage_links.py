#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Mysql里的六度空间游戏(维基百科六度分隔)'

# 设计一个带有两张数据表的数据库来分别存储页面和链接，两张表都带有创建时间和独立的 ID 号
# CREATE DATABASE wikipedia;
# CREATE TABLE `wikipedia`.`pages`(`id` INT NOT NULL AUTO_INCREMENT,`url` VARCHAR(255) NOT NULL,`created` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,PRIMARY KEY(`id`));
# CREATE TABLE `wikipedia`.`links`(`id` INT NOT NULL AUTO_INCREMENT,`fromPageId` INT NULL,`toPageId` INT NULL,`created` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,PRIMARY KEY(`id`));

