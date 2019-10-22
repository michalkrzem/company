create database imgw_manager;
use imgw_manager;


CREATE TABLE IF NOT EXISTS logowanie (
  id_loginu INT NOT NULL AUTO_INCREMENT,
  login VARCHAR(45) NOT NULL,
  haslo VARCHAR(45) NOT NULL,
  PRIMARY KEY (id_loginu))
;
-- -----------------------------------------------------
-- Table logowanie		1
-- -----------------------------------------------------


