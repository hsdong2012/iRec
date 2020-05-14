/*
SQLyog Ultimate v12.08 (64 bit)
MySQL - 5.5.27 : Database - attend
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`attend` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `attend`;

/*Table structure for table `tab_attend` */

DROP TABLE IF EXISTS `tab_attend`;

CREATE TABLE `tab_attend` (
  `meetingid` varchar(32) NOT NULL,
  `empid` varchar(12) NOT NULL,
  `arrivaltime` datetime DEFAULT NULL,
  `islate` char(4) DEFAULT NULL,
  PRIMARY KEY (`meetingid`,`empid`),
  KEY `attend_empid_fk` (`empid`),
  CONSTRAINT `attend_meetingid_fk` FOREIGN KEY (`meetingid`) REFERENCES `tab_meeting` (`meetingid`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `attend_empid_fk` FOREIGN KEY (`empid`) REFERENCES `tab_emp` (`empid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `tab_attend` */

/*Table structure for table `tab_dept` */

DROP TABLE IF EXISTS `tab_dept`;

CREATE TABLE `tab_dept` (
  `deptid` int(11) NOT NULL AUTO_INCREMENT,
  `deptname` varchar(20) NOT NULL,
  `deptintro` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`deptid`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

/*Data for the table `tab_dept` */

insert  into `tab_dept`(`deptid`,`deptname`,`deptintro`) values (1,'软件教研室','信息技术学院教研室,负责软件技术专业的课程教学任务'),(2,'物联网教研室','信息技术学院教研室,负责物联网技术专业的课程教学任务'),(3,'计应教研室','信息技术学院教研室,负责计算机应用技术专业的课程教学任务'),(4,'网络教研室','信息技术学院教研室,负责大网络技术专业的课程教学任务'),(5,'大数据教研室','信息技术学院大数据教研室,负责大数据专业的课程教学任务'),(6,'计算机基础课程组','信息技术学院计算机基础课程组,负责苏州经贸学院计算机应用基础课程的教学任务'),(7,'分团委、辅导员办公室','信息技术学院分团委、辅导员办公室,负责学院学生管理'),(8,'学院行政办公室','信息技术学院行政办公室,负责学院日常行政及教务事务管理安排'),(9,'机房管理办公室','信息技术学院机房管理办公室,负责机房维护、资产管理与机房教学安排');

/*Table structure for table `tab_emp` */

DROP TABLE IF EXISTS `tab_emp`;

CREATE TABLE `tab_emp` (
  `empid` varchar(12) NOT NULL,
  `NAME` varchar(20) NOT NULL,
  `PASSWORD` varchar(32) NOT NULL,
  `gender` char(2) NOT NULL,
  `phone` char(18) DEFAULT NULL,
  `deptid` int(11) DEFAULT NULL,
  `postid` int(11) DEFAULT NULL,
  `syslevel` int(2) NOT NULL,
  PRIMARY KEY (`empid`),
  KEY `emp_deptid_fk` (`deptid`),
  KEY `emp_postid_fk` (`postid`),
  CONSTRAINT `emp_deptid_fk` FOREIGN KEY (`deptid`) REFERENCES `tab_dept` (`deptid`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `emp_postid_fk` FOREIGN KEY (`postid`) REFERENCES `tab_post` (`postid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `tab_emp` */

insert  into `tab_emp`(`empid`,`NAME`,`PASSWORD`,`gender`,`phone`,`deptid`,`postid`,`syslevel`) values ('2006022501','admin','202cb962ac59075b964b07152d234b70','男','13333333333',1,1,1),('2006022504','董虎胜','8888','男','18914066046',1,1,1),('2006022505','翟高粤','8888','男',NULL,1,1,0),('2006022506','田英','8888','女',NULL,1,1,0),('2006022507','吴健','8888','男',NULL,9,2,0),('2006022508','廖宇','8888','男',NULL,8,3,0),('2006022509','陆庆生','8888','男',NULL,8,7,0),('2006022510','李冬','8888','男',NULL,8,8,0),('2006022511','李林燕','8888','女',NULL,3,1,0),('2006022512','戴锐青','8888','男',NULL,6,1,0),('2006022513','冯蓉珍','8888','女',NULL,2,1,0),('2006022514','蔡达君','8888','男',NULL,8,7,0),('2006022515','冯雁','8888','女',NULL,8,8,0),('2006022526','陆萍','8888','女',NULL,3,1,1);

/*Table structure for table `tab_meeting` */

DROP TABLE IF EXISTS `tab_meeting`;

CREATE TABLE `tab_meeting` (
  `meetingid` varchar(32) NOT NULL,
  `starttime` datetime NOT NULL,
  `place` varchar(32) NOT NULL,
  `chairman` varchar(20) NOT NULL,
  `topic` varchar(100) NOT NULL,
  `attenders` varchar(100) NOT NULL,
  `remarks` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`meetingid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `tab_meeting` */

insert  into `tab_meeting`(`meetingid`,`starttime`,`place`,`chairman`,`topic`,`attenders`,`remarks`) values ('20191208130000','2019-12-08 13:00:00','3318会议室','李冬','讨论下学期培养方案与课程设置','冯雁, 董虎胜, 宋志强, 施连敏, 方武','会议时间约1小时, 会议提前15分钟签到, 请准时参会!'),('20191209100000','2019-12-09 10:00:00','3318会议室','陆庆生','安排近期党务工作与民主评议','蔡达君, 柳青, 张香宁, 董虎胜, 宋志强, 施连敏','会议时间约0.5小时, 会议提前15分钟签到, 请准时参会!');

/*Table structure for table `tab_post` */

DROP TABLE IF EXISTS `tab_post`;

CREATE TABLE `tab_post` (
  `postid` int(11) NOT NULL AUTO_INCREMENT,
  `postname` varchar(20) NOT NULL,
  `postintro` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`postid`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

/*Data for the table `tab_post` */

insert  into `tab_post`(`postid`,`postname`,`postintro`) values (1,'教师','负责专业及基础课程的教学、毕业设计, 指导学生竞赛, 承担班主任等工作'),(2,'实验员','负责资产及设备管理,机房维护,机房教学安排等工作'),(3,'办公室主任','负责学院日学行政事务安排等工作'),(4,'教学秘书','负责教师调课、材料收集下发、教学工作量登记等学院日学教学事务安排工作'),(5,'辅导员','负责学生思想教育、评优评先、宿舍管理等学生管理安排工作'),(6,'分团委书记','负责学生党建、思想教育、评优评先、宿舍管理等学生管理安排工作'),(7,'书记','负责教师与学生党建、指导学院整体发展与日常管理工作'),(8,'院长','负责学院整体发展、学院人员安排、专业设置、资产管理等工作');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
