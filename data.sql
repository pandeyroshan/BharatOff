-- MySQL dump 10.13  Distrib 5.7.30, for Linux (x86_64)
--
-- Host: localhost    Database: BF
-- ------------------------------------------------------
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
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add Cities',7,'add_citydata'),(26,'Can change Cities',7,'change_citydata'),(27,'Can delete Cities',7,'delete_citydata'),(28,'Can view Cities',7,'view_citydata'),(29,'Can add Category',8,'add_category'),(30,'Can change Category',8,'change_category'),(31,'Can delete Category',8,'delete_category'),(32,'Can view Category',8,'view_category'),(33,'Can add Mini Locations',9,'add_minilocation'),(34,'Can change Mini Locations',9,'change_minilocation'),(35,'Can delete Mini Locations',9,'delete_minilocation'),(36,'Can view Mini Locations',9,'view_minilocation'),(37,'Can add State',10,'add_statedata'),(38,'Can change State',10,'change_statedata'),(39,'Can delete State',10,'delete_statedata'),(40,'Can view State',10,'view_statedata'),(41,'Can add Offers',11,'add_files'),(42,'Can change Offers',11,'change_files'),(43,'Can delete Offers',11,'delete_files'),(44,'Can view Offers',11,'view_files'),(45,'Can add Address and Details',12,'add_address'),(46,'Can change Address and Details',12,'change_address'),(47,'Can delete Address and Details',12,'delete_address'),(48,'Can view Address and Details',12,'view_address'),(49,'Can add Visitor Counts',13,'add_visitors'),(50,'Can change Visitor Counts',13,'change_visitors'),(51,'Can delete Visitor Counts',13,'delete_visitors'),(52,'Can view Visitor Counts',13,'view_visitors'),(53,'Can add Counter',14,'add_visitcount'),(54,'Can change Counter',14,'change_visitcount'),(55,'Can delete Counter',14,'delete_visitcount'),(56,'Can view Counter',14,'view_visitcount'),(57,'Can add Messages',15,'add_messages'),(58,'Can change Messages',15,'change_messages'),(59,'Can delete Messages',15,'delete_messages'),(60,'Can view Messages',15,'view_messages'),(61,'Can add Website Count',16,'add_webcounter'),(62,'Can change Website Count',16,'change_webcounter'),(63,'Can delete Website Count',16,'delete_webcounter'),(64,'Can view Website Count',16,'view_webcounter'),(65,'Can add Profiles',17,'add_userprofile'),(66,'Can change Profiles',17,'change_userprofile'),(67,'Can delete Profiles',17,'delete_userprofile'),(68,'Can view Profiles',17,'view_userprofile');
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$180000$sps6PrTxVrbK$/sNQwfhztLiVpICe+j+OqocoeHGl1K9FZ1aRlcOTjh0=','2020-10-16 15:58:06.310660',1,'admin','','','admin@gmail.com',1,1,'2020-10-16 15:57:52.716950');
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
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2020-10-16 15:59:54.987198','1','Address and Detail',1,'[{\"added\": {}}]',12,1),(2,'2020-10-16 16:02:15.600420','1','Andaman and Nicobar Island',1,'[{\"added\": {}}]',10,1),(3,'2020-10-16 16:02:25.008177','2','Andhra Pradesh',1,'[{\"added\": {}}]',10,1),(4,'2020-10-16 16:02:36.910434','3','Arunanchal Pradesh',1,'[{\"added\": {}}]',10,1),(5,'2020-10-16 16:02:56.424343','4','Assam',1,'[{\"added\": {}}]',10,1),(6,'2020-10-16 16:03:01.146660','5','Bihar',1,'[{\"added\": {}}]',10,1),(7,'2020-10-16 16:03:11.400929','6','Chattisgarh',1,'[{\"added\": {}}]',10,1),(8,'2020-10-16 16:03:19.926324','7','Delhi',1,'[{\"added\": {}}]',10,1),(9,'2020-10-16 16:03:23.809517','8','Goa',1,'[{\"added\": {}}]',10,1),(10,'2020-10-16 16:03:33.890754','9','Gujarat',1,'[{\"added\": {}}]',10,1),(11,'2020-10-16 16:04:13.948997','10','Haryana',1,'[{\"added\": {}}]',10,1),(12,'2020-10-16 16:04:17.845507','11','Himanchal',1,'[{\"added\": {}}]',10,1),(13,'2020-10-16 16:04:30.184302','12','Jammu & Kashmir',1,'[{\"added\": {}}]',10,1),(14,'2020-10-16 16:04:38.042405','13','Jharkhand',1,'[{\"added\": {}}]',10,1),(15,'2020-10-16 16:04:42.382823','14','Karnataka',1,'[{\"added\": {}}]',10,1),(16,'2020-10-16 16:04:52.551325','11','Himanchal Pradesh',2,'[{\"changed\": {\"fields\": [\"State Name\"]}}]',10,1),(17,'2020-10-16 16:09:03.228905','1','Address and Detail',3,'',12,1),(18,'2020-10-16 16:14:24.089404','14','Karnataka',3,'',10,1),(19,'2020-10-16 16:14:24.093025','13','Jharkhand',3,'',10,1),(20,'2020-10-16 16:14:24.095244','12','Jammu & Kashmir',3,'',10,1),(21,'2020-10-16 16:14:24.097299','11','Himanchal Pradesh',3,'',10,1),(22,'2020-10-16 16:14:24.100320','10','Haryana',3,'',10,1),(23,'2020-10-16 16:14:24.103940','9','Gujarat',3,'',10,1),(24,'2020-10-16 16:14:24.105464','8','Goa',3,'',10,1),(25,'2020-10-16 16:14:24.107872','7','Delhi',3,'',10,1),(26,'2020-10-16 16:14:24.109490','6','Chattisgarh',3,'',10,1),(27,'2020-10-16 16:14:24.112615','5','Bihar',3,'',10,1),(28,'2020-10-16 16:14:24.115549','4','Assam',3,'',10,1),(29,'2020-10-16 16:14:24.117032','3','Arunanchal Pradesh',3,'',10,1),(30,'2020-10-16 16:14:24.120357','2','Andhra Pradesh',3,'',10,1),(31,'2020-10-16 16:14:24.124118','1','Andaman and Nicobar Island',3,'',10,1);
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
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(12,'management','address'),(8,'management','category'),(7,'management','citydata'),(11,'management','files'),(15,'management','messages'),(9,'management','minilocation'),(10,'management','statedata'),(14,'management','visitcount'),(13,'management','visitors'),(16,'management','webcounter'),(6,'sessions','session'),(17,'users','userprofile');
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
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-09-30 13:55:55.364400'),(2,'auth','0001_initial','2020-09-30 13:55:55.541065'),(3,'admin','0001_initial','2020-09-30 13:55:55.920919'),(4,'admin','0002_logentry_remove_auto_add','2020-09-30 13:55:56.023055'),(5,'admin','0003_logentry_add_action_flag_choices','2020-09-30 13:55:56.044572'),(6,'contenttypes','0002_remove_content_type_name','2020-09-30 13:55:56.138645'),(7,'auth','0002_alter_permission_name_max_length','2020-09-30 13:55:56.159250'),(8,'auth','0003_alter_user_email_max_length','2020-09-30 13:55:56.181960'),(9,'auth','0004_alter_user_username_opts','2020-09-30 13:55:56.191101'),(10,'auth','0005_alter_user_last_login_null','2020-09-30 13:55:56.228002'),(11,'auth','0006_require_contenttypes_0002','2020-09-30 13:55:56.233620'),(12,'auth','0007_alter_validators_add_error_messages','2020-09-30 13:55:56.266038'),(13,'auth','0008_alter_user_username_max_length','2020-09-30 13:55:56.283957'),(14,'auth','0009_alter_user_last_name_max_length','2020-09-30 13:55:56.297665'),(15,'auth','0010_alter_group_name_max_length','2020-09-30 13:55:56.311569'),(16,'auth','0011_update_proxy_permissions','2020-09-30 13:55:56.321493'),(17,'sessions','0001_initial','2020-09-30 13:55:56.339637'),(18,'management','0001_initial','2020-09-30 14:16:56.427611'),(19,'users','0001_initial','2020-09-30 14:17:45.408845'),(20,'management','0002_files_minilocation','2020-09-30 17:29:24.417034'),(21,'management','0003_files_user','2020-09-30 17:30:27.586157'),(22,'management','0004_auto_20200930_2313','2020-09-30 17:43:11.395689'),(23,'management','0005_auto_20201003_1748','2020-10-03 12:18:32.171069'),(24,'management','0006_auto_20201003_1816','2020-10-03 12:46:51.840954'),(25,'management','0007_files_activated_till','2020-10-12 19:21:25.553552'),(26,'users','0002_remove_userprofile_city','2020-10-13 05:23:48.836775'),(27,'users','0003_userprofile_city','2020-10-13 05:49:02.189536'),(28,'users','0004_auto_20201014_2221','2020-10-14 16:51:52.362825'),(29,'users','0005_remove_userprofile_city','2020-10-15 08:16:52.450420'),(30,'management','0008_auto_20201016_2131','2020-10-16 16:01:56.090404'),(31,'management','0009_auto_20201016_2132','2020-10-16 16:02:11.750433');
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
INSERT INTO `django_session` VALUES ('88p17askm1scc30o2wjpebq76mjid56v','YzgzYTAwOGRkNThhN2MxZmNhNDEzZjYzYWQxZTFkMzhhN2EyNThiMzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlMThhZDJhODQwMjA4MjM1ZGJmZWQ2ODE4MzA4ZDYwYjUwMzg5MTk1In0=','2020-10-30 15:58:06.313663');
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
INSERT INTO `management_address` VALUES (1,'Insappa layout Sister’s Convent road behind charles school Kamanahalli main road Bangalore-560048 - INDIA','contact@bharatoff.com','7477012700');
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
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `management_category`
--

LOCK TABLES `management_category` WRITE;
/*!40000 ALTER TABLE `management_category` DISABLE KEYS */;
INSERT INTO `management_category` VALUES (1,'Fashion'),(2,'Salon'),(3,'Grocery'),(4,'Supermarket'),(5,'Electronic'),(6,'Jewellers'),(7,'Bakery and Cake');
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
) ENGINE=InnoDB AUTO_INCREMENT=254 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `management_citydata`
--

LOCK TABLES `management_citydata` WRITE;
/*!40000 ALTER TABLE `management_citydata` DISABLE KEYS */;
INSERT INTO `management_citydata` VALUES (4,'Port Blair',11.6234,92.7265),(5,'Bakultala',22.4854,88.3018),(6,'Bamboo Flat',11.7082,92.7211),(7,'Garacharma',11.606,92.7058),(8,'Prothrapur',11.6186,92.727),(9,'Amaravati',20.932,77.7523),(10,'Anantapur',14.6819,77.6006),(11,'Chittoor',13.2172,79.1003),(12,'East Godavari',17.3213,82.0407),(13,'Guntur',16.3067,80.4365),(14,'YSR Kadapa',14.5767,78.8383),(15,'Krishna',16.61,80.7214),(16,'Kurnool',15.8281,78.0373),(17,'Nellore',14.4426,79.9865),(18,'Prakasam',15.3485,79.5603),(19,'Srikakulam',18.2949,83.8938),(20,'Visakhapatnam',17.6868,83.2185),(21,'Vizianagaram',18.1067,83.3956),(22,'West Godavari',16.9174,81.3399),(23,'Itanagar',27.0844,93.6053),(24,'Changlang',27.7422,96.6424),(25,'Dibang Valley',28.8129,96.1527),(26,'East Kameng',27.4231,93.0176),(27,'East Siang',28.1097,95.1432),(28,'Kurung Kumey',27.799536,93.553841),(29,'Lohit',27.904,96.1739),(30,'Lower Dibang Valley',28.1429,95.8431),(31,'Lower Subansiri',27.6169,93.8392),(32,'Namsai',27.6692,95.8644),(33,'Tawang',27.5861,91.8594),(34,'Upper Siang',28.7589,95.2267),(35,'Upper Subansiri',27.7868,94.336),(36,'West Kameng',27.3428,92.3024),(37,'West Siang',28.1473,94.7485),(38,'Dispur',26.1433,91.7898),(39,'Guwahati',26.1445,91.7362),(40,'Silchar',24.8333,92.7789),(41,'Dibrugarh',27.4728,94.912),(42,'Jorhat',26.7509,94.2037),(43,'Nagaon',26.348,92.6838),(44,'Tinsukia',27.4886,95.3558),(45,'Tezpur',26.6528,92.7926),(46,'Bongaigaon',26.503,90.5536),(47,'Patna',25.5941,85.1376),(48,'Gaya',24.7914,85.0002),(49,'Bhagalpur',25.2425,86.9842),(50,'Muzaffarpur',26.1197,85.391),(51,'Purnia',25.7771,87.4753),(52,'Darbhanga',26.1542,85.8918),(53,'Bihar Sharif',25.205,85.5174),(54,'Arrah',25.5541,84.6665),(55,'Begusarai',25.4182,86.1272),(56,'Katihar',25.5541,87.5591),(57,'Munger',25.3708,86.4734),(58,'Chapra',25.7811,84.7543),(59,'Danapur',25.6241,85.0414),(60,'Bettiah',26.8026,84.5201),(61,'Saharsa',25.8774,86.5928),(62,'Sasaram',24.9539,84.0143),(63,'Hajipur',25.6924,85.2083),(64,'Dehri',24.9061,84.1912),(65,'Siwan',26.2243,84.36),(66,'Motihari',26.6438,84.904),(67,'Nawada',24.8867,85.5435),(68,'Bagaha',27.1222,84.0722),(69,'Buxar',25.5647,83.9777),(70,'Kishanganj',26.0982,87.945),(71,'Sitamarhi',26.5887,85.5013),(72,'Jamalpur',25.318,86.4934),(73,'Jehanabad',25.2133,84.9853),(74,'Aurangabad',19.8762,75.3433),(75,'Raipur',21.2514,81.6296),(76,'Bastar',19.1071,81.9535),(77,'Bijapur',18.7977,80.8129),(78,'Bilaspur',22.0797,82.1409),(79,'Dantewada',18.8456,81.3839),(80,'Dhamtari',20.7015,81.5542),(81,'Durg',21.1623,81.4279),(82,'Janjgir-Champa',21.9706,82.4753),(83,'Jashpur',22.8759,84.1381),(84,'Kawardha',22.0106,81.2359),(85,'Korba',22.3595,82.7501),(86,'Koriya',23.3875,82.3886),(87,'Mahasamund',21.1124,82.096),(88,'Narayanpur',19.7196,81.2472),(89,'Raigarh',21.8974,83.395),(90,'Rajnandgaon',21.0972,81.0338),(91,'Surguja',22.9494,83.1649),(92,'Uttar Bastar Kanker',20.2642,81.498),(93,'New Delhi',28.6139,77.209),(94,'Central Delhi',28.6643,77.2167),(95,'East Delhi',28.628,77.2956),(96,'North Delhi',28.7886,77.1412),(97,'North East Delhi',28.7184,77.258),(98,'North West Delhi',28.7186,77.0685),(99,'South Delhi',28.4817,77.1873),(100,'South West Delhi',28.5929,77.0346),(101,'West Delhi',28.6663,77.068),(102,'Panaji',15.4909,73.8278),(103,'Bicholim',15.5889,73.9654),(104,'Canacona',14.9976,74.0411),(105,'Curchorem',15.2417,74.1123),(106,'Mapusa',15.5937,73.8142),(107,'Margao',15.2832,73.9862),(108,'Mormugao',15.3889,73.8166),(109,'Pernem',15.7198,73.7963),(110,'Ponda',15.4027,74.0078),(111,'Quepem',15.2282,74.0647),(112,'Sanguem',15.2302,74.1504),(113,'Sanquelim',15.5583,74.0124),(114,'Valpoi',15.53,74.1301),(115,'Cuncolim',15.1742,73.9828),(116,'Gandhinagar',23.2156,72.6369),(117,'Ahmedabad',23.0225,72.5714),(118,'Surat',21.1702,72.8311),(119,'Vadodara',22.3072,73.1812),(120,'Rajkot',22.3039,70.8022),(121,'Bhavnagar',21.7645,72.1519),(122,'Jamnagar',22.4707,70.0577),(123,'Junagadh',21.5222,70.4579),(124,'Anand',22.5645,72.9289),(125,'Navsari',20.9467,72.952),(126,'Morbi',22.8252,70.8491),(128,'Gandhidham',23.0753,70.1337),(129,'Nadiad',22.6916,72.8634),(130,'Surendranagar',22.7739,71.6673),(131,'Bharuch',21.7051,72.9959),(132,'Daman and Diu',20.4283,72.8397),(133,'Porbandar',21.6417,69.6293),(134,'Chandigarh',30.7333,76.7794),(135,'Faridabad',28.4089,77.3178),(136,'Gurugram',28.4595,77.0266),(137,'Panipat',29.3909,76.9635),(138,'Ambala',30.3752,76.7821),(139,'Yamuna Nagar',30.129,77.2674),(140,'Rohtak',28.8955,76.6066),(141,'Hisar',29.1492,75.7217),(142,'Karnal',29.6857,76.9905),(143,'Sonipat',28.9931,77.0151),(144,'Panchkula',30.6942,76.8606),(145,'Bhiwani',28.7975,76.1322),(146,'Sirsa',29.5321,75.0318),(147,'Bahadurgarh',28.6914,76.9314),(148,'Jind',29.3255,76.2998),(149,'Thanesar',29.9699,76.8193),(150,'Kaithal',29.8043,76.4039),(151,'Rewari',28.192,76.6191),(152,'Mohindergarh',28.2734,76.1401),(153,'Pundri',29.7621,76.5546),(154,'Kosli',28.3969,76.4852),(155,'Shimla',31.1048,77.1734),(156,'Solan',30.9084,77.0999),(157,'Dharamshala',32.219,76.3234),(158,'Baddi',30.9578,76.7914),(159,'Nahan',30.5599,77.2955),(160,'Mandi',31.5892,76.9182),(161,'Paonta Sahib',30.4453,77.6021),(162,'Sundar Nagar',31.5299,76.8889),(163,'Chamba',32.5534,76.1258),(164,'Una',31.4685,76.2708),(165,'Kullu',31.9592,77.1089),(166,'Hamirpur',31.6862,76.5213),(167,'Bilaspur Himachal',31.3407,76.6875),(168,'Cantonment Board Bakloh',32.4725,75.9245),(169,'Nalagarh',31.0461,76.7026),(170,'Nurpur',32.3001,75.8853),(171,'Kangra',32.0998,76.2691),(172,'Santokhgarh',31.3562,76.3226),(173,'Shamshi',31.8933,77.1384),(174,'Parwanoo',30.8406,76.9584),(175,'Manali',32.2432,77.1892),(176,'Tira Sujanpur',31.8339,76.5055),(177,'Ghumarwin',31.4491,76.7048),(178,'Dalhousie',32.5387,75.971),(179,'Rohru',31.2046,77.7524),(180,'Nagrota Bagwan',32.1054,76.3789),(181,'Rampur Bushahr',31.4492,77.6298),(182,'Kumarsain',31.3183,77.4458),(183,'Jawalamukhi',31.8752,76.3203),(184,'Joginder Nagar',31.9912,76.7899),(185,'Dera Gopipur',31.8818,76.2146),(186,'Sarkaghat',31.699,76.7324),(187,'Jhakri',31.4972,77.708),(188,'Indora',32.1346,75.6892),(189,'Bhuntar',31.8862,77.1455),(190,'Nadaun',31.7785,76.3445),(191,'Theog',31.1183,77.3597),(192,'Kasauli Cantonment',30.8999,76.9677),(193,'Gagret',31.6622,76.0595),(194,'Chowari',32.4312,76.0131),(195,'Daulatpur',31.7747,75.9985),(196,'Sabathu Cantonment',30.9759,76.988),(197,'Dalhousie Cantonment',32.5438,75.9634),(198,'Palampur',32.1109,76.5363),(199,'Arki',31.1521,76.9686),(200,'Dagshai Cantonment',30.8864,77.0521),(201,'Suni',31.2422,77.1221),(202,'Talai',31.4495,76.5228),(203,'Jutogh Cantonment',31.1048,77.1126),(204,'Chopal',30.9479,30.9479),(205,'Rewalsar',31.6322,76.8332),(206,'Bakloh Cantonment',32.4725,75.9245),(207,'Jubbal',31.1117,77.6665),(208,'Bhota',31.6098,76.5676),(209,'Banjar',31.6377,77.3441),(210,'Naina Devi',31.3064,76.5358),(211,'Kotkhai',31.1172,77.5409),(212,'Narkanda',31.2578,77.4602),(213,'Srinagar',34.0837,74.7973),(214,'Jammu',32.7266,74.857),(215,'Anantnag',33.7311,75.1487),(216,'Ranchi',23.3441,85.3096),(217,'Jamshedpur',22.8046,86.2029),(218,'Dhanbad',23.7957,86.4304),(219,'Bokaro Steel City',23.6693,86.1511),(220,'Deoghar',24.4852,86.6948),(221,'Chakradharpur',22.6765,85.6255),(222,'Phusro',23.7623,86.0021),(223,'Hazaribagh',23.9925,85.3637),(224,'Giridih',24.1913,86.2996),(225,'Ramgarh',23.6363,85.5124),(226,'Daltonganj',24.0465,84.0768),(227,'Chirkunda',23.7479,86.7869),(228,'Bengaluru',12.9716,77.5946),(229,'Hubli',15.3647,75.124),(230,'Mysuru',12.2958,76.6394),(231,'Gulbarga',17.3297,76.8343),(232,'Mangalore',12.9141,74.856),(233,'Belgaum',15.8497,74.4977),(234,'Davanagere',14.4644,75.9218),(235,'Ballari',15.1394,76.9214),(236,'Vijayapura',16.8302,75.71),(237,'Shivamogga',13.9299,75.5681),(238,'Tumakuru',13.3379,77.1173),(239,'Raichur',16.216,77.3566),(240,'Bidar',17.9104,77.5199),(241,'Hosapete',15.2689,76.3909),(242,'Gadag',15.4315,75.6355),(243,'Robertsonpete',12.9551,78.2699),(244,'Hassan',13.0033,76.1004),(245,'Bhadravathi',13.8276,75.7064),(246,'Chitradurga',14.2251,76.398),(247,'Udupi',13.3409,74.7421),(248,'Kolar',13.1362,78.1291),(249,'Mandya',12.5218,76.8951),(250,'Chikmagalur',13.3161,75.772),(251,'Gangavathi',15.4319,76.5281),(252,'Bagalkot',16.1357,75.6208),(253,'Ranebennur',14.6154,75.6288);
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
  `user_id` int(11) NOT NULL,
  `location` varchar(50000) NOT NULL,
  `company_name` varchar(300) NOT NULL,
  `date` date NOT NULL,
  `activated_till` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `management_files_category_id_dd455d15_fk_management_category_id` (`category_id`),
  KEY `management_files_user_id_ee788d7d_fk_auth_user_id` (`user_id`),
  CONSTRAINT `management_files_category_id_dd455d15_fk_management_category_id` FOREIGN KEY (`category_id`) REFERENCES `management_category` (`id`),
  CONSTRAINT `management_files_user_id_ee788d7d_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `management_files`
--

LOCK TABLES `management_files` WRITE;
/*!40000 ALTER TABLE `management_files` DISABLE KEYS */;
/*!40000 ALTER TABLE `management_files` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `management_files_MiniLocation`
--

DROP TABLE IF EXISTS `management_files_MiniLocation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `management_files_MiniLocation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `files_id` int(11) NOT NULL,
  `minilocation_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `management_files_MiniLoc_files_id_minilocation_id_d288a3b1_uniq` (`files_id`,`minilocation_id`),
  KEY `management_files_Min_minilocation_id_b828e9d4_fk_managemen` (`minilocation_id`),
  CONSTRAINT `management_files_Min_files_id_d92add40_fk_managemen` FOREIGN KEY (`files_id`) REFERENCES `management_files` (`id`),
  CONSTRAINT `management_files_Min_minilocation_id_b828e9d4_fk_managemen` FOREIGN KEY (`minilocation_id`) REFERENCES `management_minilocation` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `management_files_MiniLocation`
--

LOCK TABLES `management_files_MiniLocation` WRITE;
/*!40000 ALTER TABLE `management_files_MiniLocation` DISABLE KEYS */;
/*!40000 ALTER TABLE `management_files_MiniLocation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `management_files_city`
--

DROP TABLE IF EXISTS `management_files_city`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `management_files_city` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `files_id` int(11) NOT NULL,
  `citydata_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `management_files_city_files_id_citydata_id_a3852048_uniq` (`files_id`,`citydata_id`),
  KEY `management_files_cit_citydata_id_fd9951fa_fk_managemen` (`citydata_id`),
  CONSTRAINT `management_files_cit_citydata_id_fd9951fa_fk_managemen` FOREIGN KEY (`citydata_id`) REFERENCES `management_citydata` (`id`),
  CONSTRAINT `management_files_city_files_id_9f2232cb_fk_management_files_id` FOREIGN KEY (`files_id`) REFERENCES `management_files` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `management_files_city`
--

LOCK TABLES `management_files_city` WRITE;
/*!40000 ALTER TABLE `management_files_city` DISABLE KEYS */;
/*!40000 ALTER TABLE `management_files_city` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `management_minilocation`
--

LOCK TABLES `management_minilocation` WRITE;
/*!40000 ALTER TABLE `management_minilocation` DISABLE KEYS */;
INSERT INTO `management_minilocation` VALUES (6,'Port Blair Gandhi Park',11.5871,92.6156,4),(7,'Bagbahara',21.0595,82.3723,87),(8,'Basna',21.2778,82.8237,87),(9,'Pithora',21.2556,82.5099,87),(10,'Saraipali',21.3181,83.0222,87),(11,'Abhanpur',21.0529,81.7441,75),(12,'Arang',21.1949,81.9698,75),(13,'Baikunth',21.4923,81.7883,75),(14,'Bhanpuri',21.2957,81.6364,75),(15,'Bhatagaon',21.1576,81.7199,75),(16,'Mowa',21.2766,81.6677,75),(17,'Rajim',20.9632,81.8907,75),(18,'Urla',21.3203,81.607,75),(19,'Kota',21.2584,81.6034,75),(20,'Tatibandh',21.2614,81.5759,75),(21,'Telibandha',21.2378,81.6651,75),(22,'Naya Raipur',21.1611,81.7864,75);
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
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `management_statedata`
--

LOCK TABLES `management_statedata` WRITE;
/*!40000 ALTER TABLE `management_statedata` DISABLE KEYS */;
INSERT INTO `management_statedata` VALUES (3,'Andaman and Nicobar Islands'),(4,'Andhra Pradesh'),(5,'Arunachal Pradesh'),(6,'Assam'),(7,'Bihar'),(8,'Chhattisgarh'),(9,'Delhi'),(10,'Goa'),(11,'Gujarat'),(12,'Haryana'),(13,'Himachal Pradesh'),(14,'Jammu and Kashmir'),(15,'Jharkhand'),(16,'Karnataka');
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
) ENGINE=InnoDB AUTO_INCREMENT=254 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `management_statedata_cities`
--

LOCK TABLES `management_statedata_cities` WRITE;
/*!40000 ALTER TABLE `management_statedata_cities` DISABLE KEYS */;
INSERT INTO `management_statedata_cities` VALUES (4,3,4),(6,3,5),(7,3,6),(8,3,7),(5,3,8),(9,4,9),(10,4,10),(11,4,11),(12,4,12),(13,4,13),(14,4,14),(15,4,15),(16,4,16),(17,4,17),(18,4,18),(19,4,19),(20,4,20),(21,4,21),(22,4,22),(29,5,23),(30,5,24),(31,5,25),(32,5,26),(33,5,27),(34,5,28),(35,5,29),(36,5,30),(37,5,31),(23,5,32),(24,5,33),(25,5,34),(26,5,35),(27,5,36),(28,5,37),(38,6,38),(39,6,39),(40,6,40),(41,6,41),(42,6,42),(43,6,43),(44,6,44),(45,6,45),(46,6,46),(47,7,47),(48,7,48),(49,7,49),(50,7,50),(51,7,51),(52,7,52),(53,7,53),(54,7,54),(55,7,55),(56,7,56),(57,7,57),(58,7,58),(59,7,59),(60,7,60),(61,7,61),(62,7,62),(63,7,63),(64,7,64),(65,7,65),(66,7,66),(67,7,67),(68,7,68),(69,7,69),(70,7,70),(71,7,71),(72,7,72),(73,7,73),(74,7,74),(75,8,75),(76,8,76),(77,8,77),(78,8,78),(79,8,79),(80,8,80),(81,8,81),(82,8,82),(83,8,83),(84,8,84),(85,8,85),(86,8,86),(87,8,87),(88,8,88),(89,8,89),(90,8,90),(91,8,91),(92,8,92),(99,9,93),(100,9,94),(101,9,95),(93,9,96),(94,9,97),(95,9,98),(96,9,99),(97,9,100),(98,9,101),(102,10,102),(103,10,103),(104,10,104),(105,10,105),(106,10,106),(107,10,107),(108,10,108),(109,10,109),(110,10,110),(111,10,111),(112,10,112),(113,10,113),(114,10,114),(115,10,115),(122,11,116),(123,11,117),(124,11,118),(125,11,119),(126,11,120),(127,11,121),(128,11,122),(129,11,123),(130,11,124),(131,11,125),(132,11,126),(116,11,128),(117,11,129),(118,11,130),(119,11,131),(120,11,132),(121,11,133),(134,12,134),(135,12,135),(136,12,136),(137,12,137),(138,12,138),(139,12,139),(140,12,140),(141,12,141),(142,12,142),(143,12,143),(144,12,144),(145,12,145),(146,12,146),(147,12,147),(148,12,148),(149,12,149),(150,12,150),(151,12,151),(152,12,152),(153,12,153),(154,12,154),(155,13,155),(156,13,156),(157,13,157),(158,13,158),(159,13,159),(160,13,160),(161,13,161),(162,13,162),(163,13,163),(164,13,164),(165,13,165),(166,13,166),(167,13,167),(168,13,168),(169,13,169),(170,13,170),(171,13,171),(172,13,172),(173,13,173),(174,13,174),(175,13,175),(176,13,176),(177,13,177),(178,13,178),(179,13,179),(180,13,180),(181,13,181),(182,13,182),(183,13,183),(184,13,184),(185,13,185),(186,13,186),(187,13,187),(188,13,188),(189,13,189),(190,13,190),(191,13,191),(192,13,192),(193,13,193),(194,13,194),(195,13,195),(196,13,196),(197,13,197),(198,13,198),(199,13,199),(200,13,200),(201,13,201),(202,13,202),(203,13,203),(204,13,204),(205,13,205),(206,13,206),(207,13,207),(208,13,208),(209,13,209),(210,13,210),(211,13,211),(212,13,212),(213,14,213),(214,14,214),(215,14,215),(220,15,216),(221,15,217),(222,15,218),(223,15,219),(224,15,220),(225,15,221),(226,15,222),(227,15,223),(216,15,224),(217,15,225),(218,15,226),(219,15,227),(228,16,228),(229,16,229),(230,16,230),(231,16,231),(232,16,232),(233,16,233),(234,16,234),(235,16,235),(236,16,236),(237,16,237),(238,16,238),(239,16,239),(240,16,240),(241,16,241),(242,16,242),(243,16,243),(244,16,244),(245,16,245),(246,16,246),(247,16,247),(248,16,248),(249,16,249),(250,16,250),(251,16,251),(252,16,252),(253,16,253);
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
) ENGINE=InnoDB AUTO_INCREMENT=252 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `management_visitors`
--

LOCK TABLES `management_visitors` WRITE;
/*!40000 ALTER TABLE `management_visitors` DISABLE KEYS */;
INSERT INTO `management_visitors` VALUES (4,26,4),(5,5,5),(6,7,6),(7,5,7),(8,4,8),(9,6,9),(10,3,10),(11,4,11),(12,6,12),(13,4,13),(14,2,14),(15,3,15),(16,4,16),(17,5,17),(18,4,18),(19,2,19),(20,2,20),(21,3,21),(22,3,22),(23,2,23),(24,2,24),(25,3,25),(26,2,26),(27,2,27),(28,2,28),(29,2,29),(30,2,30),(31,2,31),(32,2,32),(33,3,33),(34,2,34),(35,3,35),(36,2,36),(37,2,37),(38,3,38),(39,2,39),(40,2,40),(41,3,41),(42,5,42),(43,4,43),(44,2,44),(45,2,45),(46,2,46),(47,3,47),(48,3,48),(49,2,49),(50,2,50),(51,2,51),(52,2,52),(53,2,53),(54,2,54),(55,2,55),(56,2,56),(57,3,57),(58,2,58),(59,4,59),(60,2,60),(61,2,61),(62,2,62),(63,2,63),(64,2,64),(65,5,65),(66,3,66),(67,3,67),(68,3,68),(69,3,69),(70,4,70),(71,4,71),(72,4,73),(73,4,72),(74,3,74),(75,129,75),(76,3,76),(77,3,77),(78,5,78),(79,3,79),(80,5,80),(81,3,81),(82,3,82),(83,5,83),(84,4,84),(85,3,85),(86,3,86),(87,207,87),(88,3,88),(89,3,89),(90,3,90),(91,3,91),(92,3,92),(93,2,93),(94,3,94),(95,3,95),(96,2,96),(97,3,97),(98,2,98),(99,3,99),(100,2,100),(101,2,101),(102,1,102),(103,2,103),(104,2,104),(105,2,105),(106,2,106),(107,1,107),(108,2,108),(109,2,109),(110,2,110),(111,1,111),(112,1,112),(113,1,113),(114,1,114),(115,2,115),(116,3,116),(117,2,117),(118,2,118),(119,2,119),(120,1,120),(121,3,121),(122,2,122),(123,2,123),(124,1,124),(125,2,125),(126,2,126),(127,1,128),(128,2,129),(129,3,130),(130,2,131),(131,1,132),(132,3,133),(133,2,134),(134,2,135),(135,1,136),(136,1,137),(137,1,138),(138,1,139),(139,0,140),(140,2,141),(141,1,142),(142,2,143),(143,1,144),(144,1,145),(145,1,146),(146,1,147),(147,2,148),(148,1,149),(149,1,150),(150,3,151),(151,2,152),(152,1,153),(153,2,154),(154,1,155),(155,2,156),(156,1,157),(157,1,158),(158,2,159),(159,1,160),(160,2,161),(161,2,162),(162,0,163),(163,2,164),(164,2,165),(165,2,166),(166,1,167),(167,1,168),(168,2,169),(169,2,170),(170,2,171),(171,1,172),(172,1,173),(173,2,174),(174,2,175),(175,1,176),(176,0,177),(177,2,179),(178,1,180),(179,2,181),(180,2,182),(181,2,183),(182,2,184),(183,2,185),(184,1,186),(185,2,187),(186,2,189),(187,2,188),(188,2,190),(189,2,191),(190,1,192),(191,1,193),(192,2,194),(193,1,195),(194,2,196),(195,2,197),(196,2,198),(197,0,199),(198,1,200),(199,1,201),(200,2,202),(201,2,203),(202,2,204),(203,2,205),(204,0,206),(205,1,207),(206,1,208),(207,2,209),(208,1,210),(209,2,211),(210,3,212),(211,2,213),(212,1,214),(213,2,215),(214,1,216),(215,1,217),(216,1,218),(217,2,219),(218,1,220),(219,1,221),(220,1,222),(221,2,223),(222,1,224),(223,2,225),(224,1,226),(225,1,227),(226,2,228),(227,1,229),(228,1,230),(229,2,231),(230,1,232),(231,2,233),(232,2,234),(233,2,235),(234,1,236),(235,1,237),(236,1,238),(237,2,239),(238,1,240),(239,2,241),(240,0,242),(241,1,243),(242,2,244),(243,0,245),(244,1,246),(245,2,247),(246,2,248),(247,3,249),(248,2,250),(249,2,251),(250,1,252),(251,2,253);
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
INSERT INTO `management_webcounter` VALUES (1,124824);
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
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `users_userprofile_user_id_87251ef1_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_userprofile`
--

LOCK TABLES `users_userprofile` WRITE;
/*!40000 ALTER TABLE `users_userprofile` DISABLE KEYS */;
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

-- Dump completed on 2020-10-16 21:52:20
