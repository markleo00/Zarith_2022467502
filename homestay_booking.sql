-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 03, 2024 at 10:02 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `homestay_booking`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer_information`
--

CREATE TABLE `customer_information` (
  `Title_Label` varchar(4) NOT NULL,
  `Name_label` varchar(100) NOT NULL,
  `Phone_Label` varchar(11) NOT NULL,
  `Date_label` varchar(10) NOT NULL,
  `Out_label` varchar(10) NOT NULL,
  `Homestay_quantity` int(1) NOT NULL,
  `Breakfast_quantity` int(2) NOT NULL,
  `Total` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customer_information`
--

INSERT INTO `customer_information` (`Title_Label`, `Name_label`, `Phone_Label`, `Date_label`, `Out_label`, `Homestay_quantity`, `Breakfast_quantity`, `Total`) VALUES
('Mr.', 'Jeong Jaehyun', '01139136756', '1/12/24', '1/14/24', 1, 9, 268),
('Miss', 'Felicia Landosi', '01488762340', '1/24/24', '1/25/24', 1, 0, 155),
('Mrs.', 'Sairah Sakinah', '01278923456', '1/29/24', '1/31/24', 1, 2, 195),
('Mr.', 'Saifuddin Rahman', '01177610864', '2/7/24', '2/8/24', 2, 14, 472);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
