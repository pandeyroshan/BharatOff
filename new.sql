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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$180000$dqvZkOr1MQDU$dcvNeAR9HUtm2xBj9SEPyIQeMFYZJ9N2NQpkOabbAdI=','2020-10-12 18:27:15.432355',1,'admin','','','admin@gmail.com',1,1,'2020-10-03 12:50:59.959571'),(3,'pbkdf2_sha256$180000$f6aaIH2jqEnX$wb6PaGT9M9eXJX1U+2NjaVNKvxW9t0bBNkvgpUdmaQc=','2020-10-12 15:28:59.679012',0,'staff1','','','',1,1,'2020-10-03 13:01:15.000000'),(4,'pbkdf2_sha256$180000$5snde5LtxH5p$90qTGYy97P7X80GSiRgfQtqxLtmIWdDC6onLB4buiuk=','2020-10-03 13:57:58.310453',0,'staff2','','','',1,1,'2020-10-03 13:57:00.000000');
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
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2020-10-03 12:52:34.944823','1','Bhopal',1,'[{\"added\": {}}]',7,1),(2,'2020-10-03 12:52:38.457831','1','Madhya Pradesh',1,'[{\"added\": {}}]',10,1),(3,'2020-10-03 12:54:31.855916','1','Bhopal',2,'[{\"added\": {\"name\": \"Mini Locations\", \"object\": \"Upper lake\"}}]',7,1),(4,'2020-10-03 12:55:07.755054','1','Bhopal',2,'[{\"added\": {\"name\": \"Mini Locations\", \"object\": \"Moti Masjid\"}}]',7,1),(5,'2020-10-03 12:55:20.377788','1','Counter',1,'[{\"added\": {}}]',14,1),(6,'2020-10-03 12:55:28.891314','1','Click to change',1,'[{\"added\": {}}]',16,1),(7,'2020-10-03 12:55:49.921240','1','Bhopal',1,'[{\"added\": {}}]',13,1),(8,'2020-10-03 12:56:35.940792','2','Indore',1,'[{\"added\": {}}]',7,1),(9,'2020-10-03 12:57:30.684038','2','staff1',1,'[{\"added\": {}}]',4,1),(10,'2020-10-03 12:57:48.893685','1','Fashion',1,'[{\"added\": {}}]',8,1),(11,'2020-10-03 13:01:01.008503','2','staff1',3,'',4,1),(12,'2020-10-03 13:01:15.779763','3','staff1',1,'[{\"added\": {}}]',4,1),(13,'2020-10-03 13:01:22.775428','3','staff1',2,'[{\"changed\": {\"fields\": [\"Staff status\"]}}]',4,1),(14,'2020-10-03 13:03:03.162306','2','Fashion Sale 101',1,'[{\"added\": {}}]',11,1),(15,'2020-10-03 13:03:55.330235','1','Address and Detail',1,'[{\"added\": {}}]',12,1),(16,'2020-10-03 13:05:35.330692','1','Madhya Pradesh',2,'[{\"changed\": {\"fields\": [\"Cities\"]}}]',10,1),(17,'2020-10-03 13:45:10.469396','2','Indore',1,'[{\"added\": {}}]',13,1),(18,'2020-10-03 13:57:01.085424','4','staff2',1,'[{\"added\": {}}]',4,1),(19,'2020-10-03 13:57:28.873635','4','staff2',2,'[{\"changed\": {\"fields\": [\"Staff status\"]}}]',4,1),(20,'2020-10-09 14:49:48.649856','2','Indore',2,'[{\"added\": {\"name\": \"Mini Locations\", \"object\": \"Tilak Nagar\"}}]',7,1),(21,'2020-10-09 14:50:18.318324','2','Indore',2,'[{\"added\": {\"name\": \"Mini Locations\", \"object\": \"Vijay Nagar\"}}]',7,1),(22,'2020-10-09 15:01:54.467329','3','Raipur',1,'[{\"added\": {}}]',7,1),(23,'2020-10-09 15:01:57.762443','2','Chattisgarh',1,'[{\"added\": {}}]',10,1),(24,'2020-10-12 15:18:38.579468','2','Fashion Sale 101',2,'[]',11,1),(25,'2020-10-12 15:22:44.342635','3','FASHION POINT',1,'[{\"added\": {}}]',11,1),(26,'2020-10-12 18:27:23.707062','3','FASHION POINT',2,'[]',11,1),(27,'2020-10-12 18:27:32.720120','2','Fashion Sale 101',2,'[{\"changed\": {\"fields\": [\"City\"]}}]',11,1),(28,'2020-10-12 18:27:38.005642','3','FASHION POINT',2,'[]',11,1),(29,'2020-10-12 18:28:14.675801','3','Raipur',1,'[{\"added\": {}}]',13,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-09-30 13:55:55.364400'),(2,'auth','0001_initial','2020-09-30 13:55:55.541065'),(3,'admin','0001_initial','2020-09-30 13:55:55.920919'),(4,'admin','0002_logentry_remove_auto_add','2020-09-30 13:55:56.023055'),(5,'admin','0003_logentry_add_action_flag_choices','2020-09-30 13:55:56.044572'),(6,'contenttypes','0002_remove_content_type_name','2020-09-30 13:55:56.138645'),(7,'auth','0002_alter_permission_name_max_length','2020-09-30 13:55:56.159250'),(8,'auth','0003_alter_user_email_max_length','2020-09-30 13:55:56.181960'),(9,'auth','0004_alter_user_username_opts','2020-09-30 13:55:56.191101'),(10,'auth','0005_alter_user_last_login_null','2020-09-30 13:55:56.228002'),(11,'auth','0006_require_contenttypes_0002','2020-09-30 13:55:56.233620'),(12,'auth','0007_alter_validators_add_error_messages','2020-09-30 13:55:56.266038'),(13,'auth','0008_alter_user_username_max_length','2020-09-30 13:55:56.283957'),(14,'auth','0009_alter_user_last_name_max_length','2020-09-30 13:55:56.297665'),(15,'auth','0010_alter_group_name_max_length','2020-09-30 13:55:56.311569'),(16,'auth','0011_update_proxy_permissions','2020-09-30 13:55:56.321493'),(17,'sessions','0001_initial','2020-09-30 13:55:56.339637'),(18,'management','0001_initial','2020-09-30 14:16:56.427611'),(19,'users','0001_initial','2020-09-30 14:17:45.408845'),(20,'management','0002_files_minilocation','2020-09-30 17:29:24.417034'),(21,'management','0003_files_user','2020-09-30 17:30:27.586157'),(22,'management','0004_auto_20200930_2313','2020-09-30 17:43:11.395689'),(23,'management','0005_auto_20201003_1748','2020-10-03 12:18:32.171069'),(24,'management','0006_auto_20201003_1816','2020-10-03 12:46:51.840954'),(25,'management','0007_files_activated_till','2020-10-12 19:21:25.553552');
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
INSERT INTO `django_session` VALUES ('225ltqqv38nixawhj28r8et3eg0ewb47','ZjllZmJiNzdmNWUyY2E2OWIwZGZkYzJhMWQzYjAwZTM3ZjA2ZjIyMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0MzNlNjIwYjJjMGZiZTNlNjJhYTk2ZjM2OTZhZjZlYjQ5YWY0OGU3In0=','2020-10-26 18:27:15.435228'),('ln1iyyd2l0cgc8q5evy52ilgjbn3xu96','ZmNiMjc4NjExNmQ1YTBkNWVlMGE0NWVhZTZlMDc3Njg5ODE3NjhlMDp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5NjlmODAxMmJlNjU3NTZmMTkzOGM3MDU1ZDIyN2EwYWMzODJmYmQzIn0=','2020-10-26 15:28:59.682666'),('vq73dk8orx9sbyncohh9t3rqt7nfn5vv','ZjllZmJiNzdmNWUyY2E2OWIwZGZkYzJhMWQzYjAwZTM3ZjA2ZjIyMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0MzNlNjIwYjJjMGZiZTNlNjJhYTk2ZjM2OTZhZjZlYjQ5YWY0OGU3In0=','2020-10-17 15:33:16.969170');
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
INSERT INTO `management_address` VALUES (1,'Insappa layout Sister’s Convent road behind charles school Kamanahalli main road Bangalore-560048 - INDIA','contact@bharatoff.com','+91 7477012700');
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `management_citydata`
--

LOCK TABLES `management_citydata` WRITE;
/*!40000 ALTER TABLE `management_citydata` DISABLE KEYS */;
INSERT INTO `management_citydata` VALUES (1,'Bhopal',23.2599,77.4126),(2,'Indore',22.7196,75.8577),(3,'Raipur',21.2514,81.6296);
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `management_files`
--

LOCK TABLES `management_files` WRITE;
/*!40000 ALTER TABLE `management_files` DISABLE KEYS */;
INSERT INTO `management_files` VALUES (2,'Fashion Sale 101','9752315423','https://wa.me/919752315423','img/hvsv_ysfhjEl.jpg',0,1,3,'https://goo.gl/maps/zSBzuzgndq1wo5FGA','Nyka Collection','2020-10-03','2020-10-13'),(3,'FASHION POINT','9752315423','https://wa.me/919752315423','img/Screenshot_from_2020-10-10_00-33-57.png',1,1,3,'https://wa.me/919752315423','Next SALE','2020-10-12','2020-10-13');
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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `management_files_MiniLocation`
--

LOCK TABLES `management_files_MiniLocation` WRITE;
/*!40000 ALTER TABLE `management_files_MiniLocation` DISABLE KEYS */;
INSERT INTO `management_files_MiniLocation` VALUES (2,2,1),(3,3,3),(4,3,4);
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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `management_files_city`
--

LOCK TABLES `management_files_city` WRITE;
/*!40000 ALTER TABLE `management_files_city` DISABLE KEYS */;
INSERT INTO `management_files_city` VALUES (6,2,3),(5,3,2);
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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `management_minilocation`
--

LOCK TABLES `management_minilocation` WRITE;
/*!40000 ALTER TABLE `management_minilocation` DISABLE KEYS */;
INSERT INTO `management_minilocation` VALUES (1,'Upper lake',23.2532,77.3382,1),(2,'Moti Masjid',23.2556,77.399,1),(3,'Tilak Nagar',22.719,75.8972,2),(4,'Vijay Nagar',22.7533,75.8937,2);
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `management_statedata`
--

LOCK TABLES `management_statedata` WRITE;
/*!40000 ALTER TABLE `management_statedata` DISABLE KEYS */;
INSERT INTO `management_statedata` VALUES (1,'Madhya Pradesh'),(2,'Chattisgarh');
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `management_statedata_cities`
--

LOCK TABLES `management_statedata_cities` WRITE;
/*!40000 ALTER TABLE `management_statedata_cities` DISABLE KEYS */;
INSERT INTO `management_statedata_cities` VALUES (1,1,1),(2,1,2),(3,2,3);
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `management_visitors`
--

LOCK TABLES `management_visitors` WRITE;
/*!40000 ALTER TABLE `management_visitors` DISABLE KEYS */;
INSERT INTO `management_visitors` VALUES (1,129,1),(2,3,2),(3,0,3);
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
INSERT INTO `management_webcounter` VALUES (1,306);
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

-- Dump completed on 2020-10-13  0:52:11
