
-- 产看数据库字符集
SHOW CREATE DATABASE flask_shop;
-- 修改数据库字符集
ALTER DATABASE flask_shop CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
-- 查看表格字符集
SHOW CREATE TABLE t_menu;
-- 修改表格字符集
ALTER TABLE t_menu CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;


insert into t_menu (id,name,level) value (0,'全部',0);
insert into t_menu (id,name,level,pid) value (2,'用户管理',1,0);
insert into t_menu (id,name,level,pid) value (3,'权限管理',1,0);
insert into t_menu (id,name,level,pid) value (4,'商品管理',1,0);
insert into t_menu (id,name,level,pid) value (5,'订单管理',1,0);
insert into t_menu (id,name,level,pid) value (6,'数据统计',1,0);
insert into t_menu (id,name,level,pid,path) value (21,'用户列表',2,2,'/user_list');
insert into t_menu (id,name,level,pid,path) value (31,'角色列表',2,3,'/author_list');
insert into t_menu (id,name,level,pid,path) value (32,'权限列表',2,3,'/role_list');
insert into t_menu (id,name,level,pid,path) value (22,'商品列表',2,4,'/product_list');
insert into t_menu (id,name,level,pid,path) value (23,'分类列表',2,4,'/group_list');

