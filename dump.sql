-- MySQL dump 10.13  Distrib 5.7.30, for Linux (x86_64)
--
-- Host: localhost    Database: BF
-- -----------------------------------------------------
-- Server version	5.7.30-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add Address and Details',7,'add_address'),(26,'Can change Address and Details',7,'change_address'),(27,'Can delete Address and Details',7,'delete_address'),(28,'Can view Address and Details',7,'view_address'),(29,'Can add Messages',8,'add_messages'),(30,'Can change Messages',8,'change_messages'),(31,'Can delete Messages',8,'delete_messages'),(32,'Can view Messages',8,'view_messages'),(33,'Can add Counter',9,'add_visitcount'),(34,'Can change Counter',9,'change_visitcount'),(35,'Can delete Counter',9,'delete_visitcount'),(36,'Can view Counter',9,'view_visitcount'),(37,'Can add Website Count',10,'add_webcounter'),(38,'Can change Website Count',10,'change_webcounter'),(39,'Can delete Website Count',10,'delete_webcounter'),(40,'Can view Website Count',10,'view_webcounter'),(41,'Can add Mini Locations',11,'add_minilocation'),(42,'Can change Mini Locations',11,'change_minilocation'),(43,'Can delete Mini Locations',11,'delete_minilocation'),(44,'Can view Mini Locations',11,'view_minilocation'),(45,'Can add State',12,'add_statedata'),(46,'Can change State',12,'change_statedata'),(47,'Can delete State',12,'delete_statedata'),(48,'Can view State',12,'view_statedata'),(49,'Can add Category',13,'add_category'),(50,'Can change Category',13,'change_category'),(51,'Can delete Category',13,'delete_category'),(52,'Can view Category',13,'view_category'),(53,'Can add Cities',14,'add_citydata'),(54,'Can change Cities',14,'change_citydata'),(55,'Can delete Cities',14,'delete_citydata'),(56,'Can view Cities',14,'view_citydata'),(57,'Can add Offers',15,'add_files'),(58,'Can change Offers',15,'change_files'),(59,'Can delete Offers',15,'delete_files'),(60,'Can view Offers',15,'view_files'),(61,'Can add Visitor Counts',16,'add_visitors'),(62,'Can change Visitor Counts',16,'change_visitors'),(63,'Can delete Visitor Counts',16,'delete_visitors'),(64,'Can view Visitor Counts',16,'view_visitors'),(65,'Can add Profiles',17,'add_userprofile'),(66,'Can change Profiles',17,'change_userprofile'),(67,'Can delete Profiles',17,'delete_userprofile'),(68,'Can view Profiles',17,'view_userprofile');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$180000$wqkhlEpATZ1r$Qchwu6t178/rKBMvzkxPsy/2THDvZs8Wyd/fYKIlM60=','2020-09-30 17:37:06.577897',1,'admin','','','admin@gmail.com',1,1,'2020-09-30 14:30:12.611712'),(2,'pbkdf2_sha256$180000$YCFT8zLYmnLh$aUn0ASWM7EQbpeZiwytYOT2dfLcpwAag98o5TI+Tk4g=','2020-09-30 17:36:55.014620',0,'roshan','','','pandeyroshan556@gmail.com',0,1,'2020-09-30 17:36:48.514043'),(3,'pbkdf2_sha256$180000$lwXGhWRVZV68$2WWXgCB0i6+vmlg0QSiHeu8+5hHmb+tdbVJ0DCUxic0=',NULL,0,'staff_1','Staff','Name','staff@gmail.com',1,1,'2020-09-30 17:37:38.000000');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2020-09-30 14:33:17.881276','1','Address and Detail',1,'[{\"added\": {}}]',7,1),(2,'2020-09-30 17:11:17.958439','1','Bhopal',1,'[{\"added\": {}}]',14,1),(3,'2020-09-30 17:11:23.421912','1','Madhya Pradesh',1,'[{\"added\": {}}]',12,1),(4,'2020-09-30 17:16:22.623581','1','Bhopal',1,'[{\"added\": {}}]',16,1),(5,'2020-09-30 17:16:30.083244','1','Counter',1,'[{\"added\": {}}]',9,1),(6,'2020-09-30 17:18:21.824635','1','Click to change',1,'[{\"added\": {}}]',10,1),(7,'2020-09-30 17:25:07.989841','1','Bhopal',2,'[{\"added\": {\"name\": \"Mini Locations\", \"object\": \"Upper Lake\"}}]',14,1),(8,'2020-09-30 17:26:02.496665','1','Bhopal',2,'[{\"added\": {\"name\": \"Mini Locations\", \"object\": \"Moti Masjid\"}}]',14,1),(9,'2020-09-30 17:37:38.377889','3','staff_1',1,'[{\"added\": {}}]',4,1),(10,'2020-09-30 17:38:02.633092','3','staff_1',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Email address\", \"Staff status\"]}}]',4,1),(11,'2020-09-30 17:40:00.268165','1','Fashion',1,'[{\"added\": {}}]',13,1),(12,'2020-09-30 17:41:30.786804','1','Bhopal - 1',1,'[{\"added\": {}}]',15,1),(13,'2020-09-30 17:50:18.218551','1','Bhopal - 1',2,'[{\"changed\": {\"fields\": [\"Google Location URL\"]}}]',15,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'management','address'),(13,'management','category'),(14,'management','citydata'),(15,'management','files'),(8,'management','messages'),(11,'management','minilocation'),(12,'management','statedata'),(9,'management','visitcount'),(16,'management','visitors'),(10,'management','webcounter'),(6,'sessions','session'),(17,'users','userprofile');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-09-30 13:55:55.364400'),(2,'auth','0001_initial','2020-09-30 13:55:55.541065'),(3,'admin','0001_initial','2020-09-30 13:55:55.920919'),(4,'admin','0002_logentry_remove_auto_add','2020-09-30 13:55:56.023055'),(5,'admin','0003_logentry_add_action_flag_choices','2020-09-30 13:55:56.044572'),(6,'contenttypes','0002_remove_content_type_name','2020-09-30 13:55:56.138645'),(7,'auth','0002_alter_permission_name_max_length','2020-09-30 13:55:56.159250'),(8,'auth','0003_alter_user_email_max_length','2020-09-30 13:55:56.181960'),(9,'auth','0004_alter_user_username_opts','2020-09-30 13:55:56.191101'),(10,'auth','0005_alter_user_last_login_null','2020-09-30 13:55:56.228002'),(11,'auth','0006_require_contenttypes_0002','2020-09-30 13:55:56.233620'),(12,'auth','0007_alter_validators_add_error_messages','2020-09-30 13:55:56.266038'),(13,'auth','0008_alter_user_username_max_length','2020-09-30 13:55:56.283957'),(14,'auth','0009_alter_user_last_name_max_length','2020-09-30 13:55:56.297665'),(15,'auth','0010_alter_group_name_max_length','2020-09-30 13:55:56.311569'),(16,'auth','0011_update_proxy_permissions','2020-09-30 13:55:56.321493'),(17,'sessions','0001_initial','2020-09-30 13:55:56.339637'),(18,'management','0001_initial','2020-09-30 14:16:56.427611'),(19,'users','0001_initial','2020-09-30 14:17:45.408845'),(20,'management','0002_files_minilocation','2020-09-30 17:29:24.417034'),(21,'management','0003_files_user','2020-09-30 17:30:27.586157'),(22,'management','0004_auto_20200930_2313','2020-09-30 17:43:11.395689');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('y8eado9c1dn1swsu6st9oj0afymheedu','ZjM1MjBiMWI2N2ZmYzU3YmZkOWIxYjYxNWU3MGQ5OTg5ODQyYjI1NDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyNTFiNGU5YmMyYTYxMTI2OTAzYTllZTY1ZjNhOWY5MjMzZTRlNThhIn0=','2020-10-14 17:37:06.582252');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `management_address`
--

DROP TABLE IF EXISTS `management_address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `management_address` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `address` varchar(1000) NOT NULL,
  `mail` varchar(1000) NOT NULL,
  `phone_number` varchar(15) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `management_address`
--

LOCK TABLES `management_address` WRITE;
/*!40000 ALTER TABLE `management_address` DISABLE KEYS */;
INSERT INTO `management_address` VALUES (1,'Rewa, Madhya Pradesh - 486450','pandeyroshan556@gmail.com','9752315423');
/*!40000 ALTER TABLE `management_address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `management_category`
--

DROP TABLE IF EXISTS `management_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `management_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(1000) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `management_category`
--

LOCK TABLES `management_category` WRITE;
/*!40000 ALTER TABLE `management_category` DISABLE KEYS */;
INSERT INTO `management_category` VALUES (1,'Fashion');
/*!40000 ALTER TABLE `management_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `management_citydata`
--

DROP TABLE IF EXISTS `management_citydata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `management_citydata` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `city_name` varchar(300) NOT NULL,
  `lat` double NOT NULL,
  `lon` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `management_citydata`
--

LOCK TABLES `management_citydata` WRITE;
/*!40000 ALTER TABLE `management_citydata` DISABLE KEYS */;
INSERT INTO `management_citydata` VALUES (1,'Bhopal',23.2599,77.4126);
/*!40000 ALTER TABLE `management_citydata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `management_files`
--

DROP TABLE IF EXISTS `management_files`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `management_files` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `heading` varchar(300) NOT NULL,
  `phone_number` varchar(1000) NOT NULL,
  `whatsapp_link` varchar(1000) NOT NULL,
  `img` varchar(100) NOT NULL,
  `active` tinyint(1) NOT NULL,
  `category_id` int(11) NOT NULL,
  `city_id` int(11) NOT NULL,
  `MiniLocation_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `location` varchar(50000) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `management_files_category_id_dd455d15_fk_management_category_id` (`category_id`),
  KEY `management_files_city_id_230f1b97_fk_management_citydata_id` (`city_id`),
  KEY `management_files_MiniLocation_id_7d89fafb_fk_managemen` (`MiniLocation_id`),
  KEY `management_files_user_id_ee788d7d_fk_auth_user_id` (`user_id`),
  CONSTRAINT `management_files_MiniLocation_id_7d89fafb_fk_managemen` FOREIGN KEY (`MiniLocation_id`) REFERENCES `management_minilocation` (`id`),
  CONSTRAINT `management_files_category_id_dd455d15_fk_management_category_id` FOREIGN KEY (`category_id`) REFERENCES `management_category` (`id`),
  CONSTRAINT `management_files_city_id_230f1b97_fk_management_citydata_id` FOREIGN KEY (`city_id`) REFERENCES `management_citydata` (`id`),
  CONSTRAINT `management_files_user_id_ee788d7d_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `management_files`
--

LOCK TABLES `management_files` WRITE;
/*!40000 ALTER TABLE `management_files` DISABLE KEYS */;
INSERT INTO `management_files` VALUES (1,'Heading','9752315423','https://wa.me/919752315423','img/pachori.jpg',0,1,1,1,3,'https://goo.gl/maps/NtpHBL8cAS81EEwf8');
/*!40000 ALTER TABLE `management_files` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `management_messages`
--

DROP TABLE IF EXISTS `management_messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `management_messages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(500) NOT NULL,
  `email` varchar(500) NOT NULL,
  `subject` varchar(1000) NOT NULL,
  `text` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `management_messages`
--

LOCK TABLES `management_messages` WRITE;
/*!40000 ALTER TABLE `management_messages` DISABLE KEYS */;
/*!40000 ALTER TABLE `management_messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `management_minilocation`
--

DROP TABLE IF EXISTS `management_minilocation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `management_minilocation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(1000) NOT NULL,
  `lat` double NOT NULL,
  `lon` double NOT NULL,
  `main_city_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `management_minilocat_main_city_id_35e34a0b_fk_managemen` (`main_city_id`),
  CONSTRAINT `management_minilocat_main_city_id_35e34a0b_fk_managemen` FOREIGN KEY (`main_city_id`) REFERENCES `management_citydata` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `management_minilocation`
--

LOCK TABLES `management_minilocation` WRITE;
/*!40000 ALTER TABLE `management_minilocation` DISABLE KEYS */;
INSERT INTO `management_minilocation` VALUES (1,'Upper Lake',23.2532,77.3382,1),(2,'Moti Masjid',23.2556,77.399,1);
/*!40000 ALTER TABLE `management_minilocation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `management_statedata`
--

DROP TABLE IF EXISTS `management_statedata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `management_statedata` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `state_name` varchar(300) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `management_statedata`
--

LOCK TABLES `management_statedata` WRITE;
/*!40000 ALTER TABLE `management_statedata` DISABLE KEYS */;
INSERT INTO `management_statedata` VALUES (1,'Madhya Pradesh');
/*!40000 ALTER TABLE `management_statedata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `management_statedata_cities`
--

DROP TABLE IF EXISTS `management_statedata_cities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `management_statedata_cities` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `statedata_id` int(11) NOT NULL,
  `citydata_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `management_statedata_cit_statedata_id_citydata_id_7ce7e75d_uniq` (`statedata_id`,`citydata_id`),
  KEY `management_statedata_citydata_id_b9e6a290_fk_managemen` (`citydata_id`),
  CONSTRAINT `management_statedata_citydata_id_b9e6a290_fk_managemen` FOREIGN KEY (`citydata_id`) REFERENCES `management_citydata` (`id`),
  CONSTRAINT `management_statedata_statedata_id_15ba7139_fk_managemen` FOREIGN KEY (`statedata_id`) REFERENCES `management_statedata` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `management_statedata_cities`
--

LOCK TABLES `management_statedata_cities` WRITE;
/*!40000 ALTER TABLE `management_statedata_cities` DISABLE KEYS */;
INSERT INTO `management_statedata_cities` VALUES (1,1,1);
/*!40000 ALTER TABLE `management_statedata_cities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `management_visitcount`
--

DROP TABLE IF EXISTS `management_visitcount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `management_visitcount` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `count` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `management_visitcount`
--

LOCK TABLES `management_visitcount` WRITE;
/*!40000 ALTER TABLE `management_visitcount` DISABLE KEYS */;
INSERT INTO `management_visitcount` VALUES (1,0);
/*!40000 ALTER TABLE `management_visitcount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `management_visitors`
--

DROP TABLE IF EXISTS `management_visitors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `management_visitors` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `counter` int(11) NOT NULL,
  `city_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `city_id` (`city_id`),
  CONSTRAINT `management_visitors_city_id_aefc5cf9_fk_management_citydata_id` FOREIGN KEY (`city_id`) REFERENCES `management_citydata` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `management_visitors`
--

LOCK TABLES `management_visitors` WRITE;
/*!40000 ALTER TABLE `management_visitors` DISABLE KEYS */;
INSERT INTO `management_visitors` VALUES (1,27,1);
/*!40000 ALTER TABLE `management_visitors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `management_webcounter`
--

DROP TABLE IF EXISTS `management_webcounter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `management_webcounter` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `visit` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `management_webcounter`
--

LOCK TABLES `management_webcounter` WRITE;
/*!40000 ALTER TABLE `management_webcounter` DISABLE KEYS */;
INSERT INTO `management_webcounter` VALUES (1,59);
/*!40000 ALTER TABLE `management_webcounter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_userprofile`
--

DROP TABLE IF EXISTS `users_userprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mobile_number` varchar(15) NOT NULL,
  `pwd` varchar(500) NOT NULL,
  `city_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `users_userprofile_city_id_957df051_fk_management_citydata_id` (`city_id`),
  CONSTRAINT `users_userprofile_city_id_957df051_fk_management_citydata_id` FOREIGN KEY (`city_id`) REFERENCES `management_citydata` (`id`),
  CONSTRAINT `users_userprofile_user_id_87251ef1_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_userprofile`
--

LOCK TABLES `users_userprofile` WRITE;
/*!40000 ALTER TABLE `users_userprofile` DISABLE KEYS */;
INSERT INTO `users_userprofile` VALUES (1,'9752315423','Linux@123',1,2);
/*!40000 ALTER TABLE `users_userprofile` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-10-01 19:21:48
