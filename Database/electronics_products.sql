-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 13, 2024 at 02:30 AM
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
-- Database: `electronics_products`
--

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `product_id` int(11) NOT NULL,
  `product_name` varchar(255) NOT NULL,
  `category_id` int(11) DEFAULT NULL,
  `price` decimal(10,2) NOT NULL,
  `stock_quantity` int(11) DEFAULT NULL,
  `description` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`product_id`, `product_name`, `category_id`, `price`, `stock_quantity`, `description`) VALUES
(1, 'USB-C Charging Cable', 1, 11.95, 100, 'High-quality USB-C charging cable.'),
(2, 'Bose SoundSport Headphones', 2, 99.99, 50, 'Comfortable and durable headphones.'),
(3, 'Google Phone', 3, 600.00, 30, 'Latest Google smartphone.'),
(4, 'Wired Headphones', 2, 11.99, 75, 'Affordable wired headphones.'),
(5, 'Macbook Pro Laptop', 4, 1700.00, 20, 'High-performance laptop.'),
(6, 'Lightning Charging Cable', 1, 14.95, 100, 'Durable lightning charging cable.'),
(7, '27in 4K Gaming Monitor', 5, 389.99, 15, 'High-resolution gaming monitor.'),
(8, 'AA Batteries (4-pack)', 6, 3.84, 200, 'Pack of four AA batteries.'),
(9, 'Apple Airpods Headphones', 2, 150.00, 40, 'Wireless earbuds by Apple.'),
(10, 'iPhone', 3, 700.00, 25, 'Latest iPhone model.'),
(11, 'Flatscreen TV', 7, 300.00, 10, 'Modern flatscreen TV.'),
(12, '20in Monitor', 5, 109.99, 30, 'Compact 20-inch monitor.'),
(13, 'LG Dryer', 8, 600.00, 10, 'Efficient LG dryer.'),
(14, 'ThinkPad Laptop', 4, 999.99, 25, 'Reliable ThinkPad laptop.'),
(15, 'Vareebadd Phone', 3, 400.00, 20, 'Affordable Vareebadd smartphone.'),
(16, 'LG Washing Machine', 8, 600.00, 10, 'Durable LG washing machine.'),
(17, '34in Ultrawide Monitor', 5, 379.99, 15, 'Wide 34-inch monitor.'),
(18, '27in FHD Monitor', 5, 149.99, 20, 'Full HD 27-inch monitor.'),
(19, 'AAA Batteries (4-pack)', 6, 2.99, 150, 'Pack of four AAA batteries.');

-- --------------------------------------------------------

--
-- Table structure for table `product_categories`
--

CREATE TABLE `product_categories` (
  `category_id` int(11) NOT NULL,
  `category_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product_categories`
--

INSERT INTO `product_categories` (`category_id`, `category_name`) VALUES
(1, 'Accessories'),
(2, 'Headphones'),
(3, 'Phones'),
(4, 'Laptops'),
(5, 'Monitors'),
(6, 'Batteries'),
(7, 'Televisions'),
(8, 'Appliances');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`product_id`),
  ADD KEY `category_id` (`category_id`);

--
-- Indexes for table `product_categories`
--
ALTER TABLE `product_categories`
  ADD PRIMARY KEY (`category_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `product_categories`
--
ALTER TABLE `product_categories`
  MODIFY `category_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `products`
--
ALTER TABLE `products`
  ADD CONSTRAINT `products_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `product_categories` (`category_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
