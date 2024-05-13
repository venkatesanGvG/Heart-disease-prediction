-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Feb 16, 2023 at 12:49 PM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `python_heart_disease_prediction`
--

-- --------------------------------------------------------

--
-- Table structure for table `user_data`
--

CREATE TABLE `user_data` (
  `id` int(100) NOT NULL,
  `age` varchar(100) NOT NULL,
  `sex` varchar(100) NOT NULL,
  `chol` varchar(100) NOT NULL,
  `oldp` varchar(100) NOT NULL,
  `thala` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `report` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_data`
--


-- --------------------------------------------------------

--
-- Table structure for table `user_details`
--

CREATE TABLE `user_details` (
  `id` int(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `fname` varchar(100) NOT NULL,
  `contact` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `pincode` varchar(100) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `report` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_details`
--

