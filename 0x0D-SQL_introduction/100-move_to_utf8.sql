-- convert hbtn_0c_0 database to UTF8
ALTER DATABASE hbtn_0c_0 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table COLLATE utf8mb4_unicode_ci;
ALTER INDEX name COLLATE utf8mb4_unicode_ci;
