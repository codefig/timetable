-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jun 05, 2019 at 03:23 PM
-- Server version: 10.1.37-MariaDB
-- PHP Version: 7.3.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `timetable_funaab`
--

-- --------------------------------------------------------

--
-- Table structure for table `courses_cbt`
--

CREATE TABLE `courses_cbt` (
  `id` int(11) NOT NULL,
  `code` varchar(255) NOT NULL,
  `title` text,
  `no_of_students` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `courses_cbt`
--

INSERT INTO `courses_cbt` (`id`, `code`, `title`, `no_of_students`) VALUES
(1, 'CSC 300', '180', 0),
(2, 'CSC 401', 'Another', 129),
(4, '405', 'Nothing', 120),
(5, 'CPE 300', '', 120),
(6, 'CVE 300', 'Introduction to Civil Engineering Design', 120),
(7, 'WAO300', 'kdkdk', 200),
(8, 'phe', 'kdkd', 600),
(9, 'WAP350', 'kdkdk', 300),
(10, 'phe', 'kdkd', 200),
(11, 'YOU200', NULL, 1000),
(12, 'ME350', NULL, 700),
(13, 'Y250', NULL, 900),
(14, 'MEP30', NULL, 800),
(15, 'Y50', NULL, 400),
(16, 'ME530', NULL, 300),
(17, 'ZF0', NULL, 700),
(18, 'MSE300', NULL, 360),
(19, 'phy200', NULL, 350),
(20, 'PYG300', NULL, 750),
(21, 'ZSC101', NULL, 330),
(22, 'NUT250', NULL, 800),
(23, 'p200', NULL, 350),
(24, 'PPC300', NULL, 900),
(26, 'NUT300', NULL, 800),
(27, 'NNA200', NULL, 300),
(28, 'MEE 200', 'GHJK', 180);

-- --------------------------------------------------------

--
-- Table structure for table `courses_written`
--

CREATE TABLE `courses_written` (
  `id` int(11) NOT NULL,
  `code` varchar(255) NOT NULL,
  `no_of_students` int(11) NOT NULL,
  `title` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `courses_written`
--

INSERT INTO `courses_written` (`id`, `code`, `no_of_students`, `title`) VALUES
(1, 'CSC 300', 180, 'something'),
(2, 'csc 415', 120, 'Opearting System'),
(3, 'CPE 209', 10, 'Another Practical');

-- --------------------------------------------------------

--
-- Table structure for table `halls_cbt`
--

CREATE TABLE `halls_cbt` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `capacity` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `halls_cbt`
--

INSERT INTO `halls_cbt` (`id`, `name`, `capacity`) VALUES
(1, 'COMPLAB ', '500'),
(4, 'MPB', '250');

-- --------------------------------------------------------

--
-- Table structure for table `halls_written`
--

CREATE TABLE `halls_written` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `capOne` int(11) NOT NULL,
  `capTwo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `halls_written`
--

INSERT INTO `halls_written` (`id`, `name`, `capOne`, `capTwo`) VALUES
(2, 'what', 200, 200),
(3, 'Hallaam', 300, 150),
(4, 'Another', 90, 180);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `courses_cbt`
--
ALTER TABLE `courses_cbt`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `courses_written`
--
ALTER TABLE `courses_written`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `halls_cbt`
--
ALTER TABLE `halls_cbt`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `halls_written`
--
ALTER TABLE `halls_written`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `courses_cbt`
--
ALTER TABLE `courses_cbt`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `courses_written`
--
ALTER TABLE `courses_written`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `halls_cbt`
--
ALTER TABLE `halls_cbt`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `halls_written`
--
ALTER TABLE `halls_written`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
