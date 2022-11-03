-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema bd_veterinaria
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema bd_veterinaria
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `bd_veterinaria` DEFAULT CHARACTER SET utf8 ;
USE `bd_veterinaria` ;

-- -----------------------------------------------------
-- Table `bd_veterinaria`.`Usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bd_veterinaria`.`Usuarios` (
  `identificacion` INT NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `apellido_p` VARCHAR(45) NOT NULL,
  `apellido_m` VARCHAR(45) NULL,
  `telefono` VARCHAR(45) NULL,
  `mail` VARCHAR(45) NOT NULL,
  `contraseña` VARCHAR(100) NULL,
  `tipo_usuario` TINYINT NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` VARCHAR(45) NULL,
  PRIMARY KEY (`identificacion`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bd_veterinaria`.`Mascotas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bd_veterinaria`.`Mascotas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `tipo_mascota` VARCHAR(45) NOT NULL,
  `sexo` VARCHAR(45) NULL,
  `raza` VARCHAR(45) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `dueño` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Mascotas_Dueños_idx` (`dueño` ASC) VISIBLE,
  CONSTRAINT `fk_Mascotas_Dueños`
    FOREIGN KEY (`dueño`)
    REFERENCES `bd_veterinaria`.`Usuarios` (`identificacion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bd_veterinaria`.`Peso`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bd_veterinaria`.`Peso` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `peso` VARCHAR(45) NULL,
  `fecha` DATETIME NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bd_veterinaria`.`Atencion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bd_veterinaria`.`Atencion` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `tratamiento` VARCHAR(200) NULL,
  `fecha` DATETIME NULL,
  `created_At` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `peso` INT NOT NULL,
  `veterinario` INT NOT NULL,
  `mascota` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Atencion_Mascotas1_idx` (`mascota` ASC) VISIBLE,
  INDEX `fk_Atencion_Peso1_idx` (`peso` ASC) VISIBLE,
  INDEX `fk_Atencion_Usuarios1_idx` (`veterinario` ASC) VISIBLE,
  CONSTRAINT `fk_Atencion_Mascotas1`
    FOREIGN KEY (`mascota`)
    REFERENCES `bd_veterinaria`.`Mascotas` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Atencion_Peso1`
    FOREIGN KEY (`peso`)
    REFERENCES `bd_veterinaria`.`Peso` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Atencion_Usuarios1`
    FOREIGN KEY (`veterinario`)
    REFERENCES `bd_veterinaria`.`Usuarios` (`identificacion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bd_veterinaria`.`Medicamentos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bd_veterinaria`.`Medicamentos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(45) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bd_veterinaria`.`medicamentosAtencion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bd_veterinaria`.`medicamentosAtencion` (
  `medicamento` INT NOT NULL,
  `atencion` INT NOT NULL,
  INDEX `fk_medicamentosAtencion_Medicamentos1_idx` (`medicamento` ASC) VISIBLE,
  INDEX `fk_medicamentosAtencion_Atencion1_idx` (`atencion` ASC) VISIBLE,
  CONSTRAINT `fk_medicamentosAtencion_Medicamentos1`
    FOREIGN KEY (`medicamento`)
    REFERENCES `bd_veterinaria`.`Medicamentos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_medicamentosAtencion_Atencion1`
    FOREIGN KEY (`atencion`)
    REFERENCES `bd_veterinaria`.`Atencion` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
