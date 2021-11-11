-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.5.8-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             10.1.0.5464
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for project_expenses
CREATE DATABASE IF NOT EXISTS `project_expenses` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `project_expenses`;

-- Dumping structure for table project_expenses.category
CREATE TABLE IF NOT EXISTS `category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

-- Dumping data for table project_expenses.category: ~7 rows (approximately)
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` (`id`, `name`) VALUES
	(1, 'Production'),
	(2, 'Operation'),
	(3, 'Financial'),
	(4, 'Vendor'),
	(5, 'Manpower'),
	(6, 'Software'),
	(7, 'Hardware');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;

-- Dumping structure for table project_expenses.expense
CREATE TABLE IF NOT EXISTS `expense` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) NOT NULL,
  `category_id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `description` varchar(255) NOT NULL,
  `amount` float NOT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  `created_by` varchar(50) DEFAULT NULL,
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `updated_by` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_expense_project` (`project_id`),
  KEY `FK_expense_category` (`category_id`),
  CONSTRAINT `FK_expense_category` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`),
  CONSTRAINT `FK_expense_project` FOREIGN KEY (`project_id`) REFERENCES `project` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

-- Dumping data for table project_expenses.expense: ~2 rows (approximately)
/*!40000 ALTER TABLE `expense` DISABLE KEYS */;
INSERT INTO `expense` (`id`, `project_id`, `category_id`, `name`, `description`, `amount`, `created_at`, `created_by`, `updated_at`, `updated_by`) VALUES
	(1, 2, 2, 'Server Maintenance', 'Server maintenance and upgrading work to incorporate BC plans', 30000, '2021-11-04 16:00:00', 'Jacky', '2021-11-06 16:00:00', 'Jacky'),
	(2, 3, 4, 'Consultant', 'Consultancy services for integration work', 10000, '2021-11-06 16:00:00', 'Helen', '2021-11-07 16:00:00', 'Helen');
/*!40000 ALTER TABLE `expense` ENABLE KEYS */;

-- Dumping structure for table project_expenses.project
CREATE TABLE IF NOT EXISTS `project` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `description` varchar(50) NOT NULL,
  `budget` float NOT NULL DEFAULT 1000000,
  PRIMARY KEY (`id`),
  KEY `FK_project_user` (`user_id`),
  CONSTRAINT `FK_project_user` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- Dumping data for table project_expenses.project: ~3 rows (approximately)
/*!40000 ALTER TABLE `project` DISABLE KEYS */;
INSERT INTO `project` (`id`, `user_id`, `name`, `description`, `budget`) VALUES
	(1, 4, 'RTF', 'Realtime Face Recognition', 12000),
	(2, 1, 'SWT', 'Smart Watch Tracker', 80000),
	(3, 2, 'ULS', 'Upgrade Legacy System', 11000);
/*!40000 ALTER TABLE `project` ENABLE KEYS */;

-- Dumping structure for table project_expenses.user
CREATE TABLE IF NOT EXISTS `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `appointment` varchar(50) NOT NULL DEFAULT 'Project Manager',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

-- Dumping data for table project_expenses.user: ~5 rows (approximately)
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` (`id`, `username`, `password`, `name`, `appointment`) VALUES
	(1, 'user101', '123456', 'Jacky', 'Project Lead'),
	(2, 'user102', '123456', 'Tommy', 'Project Manager'),
	(3, 'user103', '123456', 'Tom', 'Project Manager'),
	(4, 'user104', '123456', 'Helen', 'Project Manager'),
	(5, 'user105', '123456', 'Mark', 'Senior Project Manager');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
