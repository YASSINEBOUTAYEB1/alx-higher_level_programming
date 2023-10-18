100-move_to_utf8.sql
-- Converts the entire database hbtn_0c_0 to UTF8.
USE `hbtn_0c_0`
ALTER TABLE `first_table`
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
