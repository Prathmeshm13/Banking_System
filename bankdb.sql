CREATE DATABASE `bankdb` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT=0;
START TRANSACTION;
SET time_zone="+00:00";
DROP TABLE IF EXISTS `customer`;
CREATE TABLE IF NOT EXISTS `customer`(
  `Account_No,` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(45) DEFAULT NULL,
  `Address` varchar(100) DEFAULT NULL,
  `Phone No.` varchar(15) DEFAULT NULL,
  `Email ID` varchar(80) DEFAULT NULL,
  `Aadhar No.` varchar(20) DEFAULT NULL,
  `Account_type` varchar(20) DEFAULT NULL,
  `Status` char(15) DEFAULT NULL,
  `Balance` float(15,2) DEFAULT NULL,
  PRIMARY KEY (`Account_No,`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `bankdb`.`customer` (`Account_No,`, `Name`, `Address`, `Phone No.`, `Email ID`, `Aadhar No.`, `Account_type`, `Status`, `Balance`) VALUES ('1', 'Prathmesh', 'Amravati, MAharashtra', '9689182477', 'prathmeshmahakal@gmail.com', '121212121121212', 'Saving', 'Active', '150000.00');
INSERT INTO `bankdb`.`customer` (`Account_No,`, `Name`, `Address`, `Phone No.`, `Email ID`, `Aadhar No.`, `Account_type`, `Status`, `Balance`) VALUES ('2', 'Rashmi', 'Mumbai,Maharashtra', '9898989895', 'rashmi@gamil.com', '152369748565236', 'Current', 'Active', '120000.00');
INSERT INTO `bankdb`.`customer` (`Account_No,`, `Name`, `Address`, `Phone No.`, `Email ID`, `Aadhar No.`, `Account_type`, `Status`, `Balance`) VALUES ('3', 'Abhishek', 'Chennai, TamilNadu', '9898932556', 'abhishek@gmail.com', '147852369874125', 'Current', 'Active', '20000.00');

DROP TABLE IF EXISTS `transaction`;
CREATE TABLE IF NOT EXISTS `transaction`(
  `TransactionID` int NOT NULL AUTO_INCREMENT,
  `Date_Of_Transaction` date DEFAULT NULL,
  `Amount` int DEFAULT NULL,
  `Transaction_Type` varchar(45) DEFAULT 'null',
  `Account_No` int DEFAULT NULL,
  PRIMARY KEY (`TransactionID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO `bankdb`.`transaction` (`TransactionID`, `Date_Of_Transaction`, `Amount`, `Transaction_Type`, `Account_No`) VALUES ('1', '2022-12-05', '10000', 'deposit', '1');
INSERT INTO `bankdb`.`transaction` (`TransactionID`, `Date_Of_Transaction`, `Amount`, `Transaction_Type`, `Account_No`) VALUES ('2', '2023-01-23', '15000', 'withdraw', '2');
INSERT INTO `bankdb`.`transaction` (`TransactionID`, `Date_Of_Transaction`, `Amount`, `Transaction_Type`, `Account_No`) VALUES ('3', '2022-02-22', '20000', 'deposit', '1');
