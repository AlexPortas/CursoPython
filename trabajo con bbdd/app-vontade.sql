-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 20-08-2022 a las 18:40:51
-- Versión del servidor: 10.4.14-MariaDB
-- Versión de PHP: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `app-vontade`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users_aplicacion`
--

CREATE TABLE `users_aplicacion` (
  `id_user_aplicacion` int(11) NOT NULL,
  `nick` varchar(50) NOT NULL,
  `pwd` varchar(50) NOT NULL,
  `tipo_user` int(3) NOT NULL,
  `nombre` varchar(150) NOT NULL,
  `correo` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `users_aplicacion`
--

INSERT INTO `users_aplicacion` (`id_user_aplicacion`, `nick`, `pwd`, `tipo_user`, `nombre`, `correo`) VALUES
(1, 'admin', '21232f297a57a5a743894a0e4a801fc3', 1, 'Alejandro Alonso Portas', '+alex@gmail.com'),
(2, 'Alex', 'PASSWORD', 2, 'Prueba', 'info@gmail.com');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `users_aplicacion`
--
ALTER TABLE `users_aplicacion`
  ADD PRIMARY KEY (`id_user_aplicacion`),
  ADD UNIQUE KEY `correo` (`correo`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `users_aplicacion`
--
ALTER TABLE `users_aplicacion`
  MODIFY `id_user_aplicacion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
