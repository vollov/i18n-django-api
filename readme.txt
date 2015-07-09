mysqldump -uroot -p  --default-character-set=utf8 i18n_lab > i18n_lab.sql
mysqldump -uroot -p  --default-character-set=utf8 --no-create-info i18n_lab > i18n_lab_data.sql
CREATE DATABASE i18n_lab CHARACTER SET utf8 COLLATE utf8_bin;

LOCK TABLES `page_page` WRITE;
/*!40000 ALTER TABLE `page_page` DISABLE KEYS */;
INSERT INTO `page_page` VALUES (1,'Django restful framework Installation','django-restful-framework-installation','2015-07-06 02:48:07'),(2,'Django restful framework view sets','django-restful-framework-view-sets','2015-07-06 02:48:55');
/*!40000 ALTER TABLE `page_page` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `page_pagetranslation`
--

LOCK TABLES `page_pagetranslation` WRITE;
/*!40000 ALTER TABLE `page_pagetranslation` DISABLE KEYS */;
INSERT INTO `page_pagetranslation` VALUES (1,'Django restful framework Installation','en',1),(2,'安装Django restful 框架','zh',1),(3,'Django restful framework view sets','en',2),(4,'Django restful 框架视图','zh',2);
/*!40000 ALTER TABLE `page_pagetranslation` ENABLE KEYS */;
UNLOCK TABLES;