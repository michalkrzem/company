create database imgw_manager;
use imgw_manager;



-- -----------------------------------------------------
-- Table logowanie		1
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS logowanie (
  id_loginu INT NOT NULL AUTO_INCREMENT,
  login VARCHAR(45) NOT NULL,
  haslo VARCHAR(45) NOT NULL,
  PRIMARY KEY (id_loginu))
;
  
-- -----------------------------------------------------
-- Table funkcja_pacownicza		2
-- -----------------------------------------------------

CREATE TABLE if not exists funkcja_pacownicza (
  id_funk_prac INT NOT NULL AUTO_INCREMENT,
  stanowisko enum('mlodszy specjalista','specjalista','starszy specjalista','expert') NOT NULL,
  max_wynagordzenie INT NOT NULL,
  min_wynagrodzenie INT NOT NULL,
  PRIMARY KEY (id_funk_prac)
  )
;

-- -----------------------------------------------------
-- Table funkcja_stacji		3
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS funkcja_stacji (
  id_funk_stacji INT NOT NULL AUTO_INCREMENT,
  funkcja VARCHAR(45) NULL,
  PRIMARY KEY (id_funk_stacji),
  UNIQUE INDEX funkcja_UNIQUE (funkcja ASC))
;


-- -----------------------------------------------------
-- Table stacja_meteorologiczna		4
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS stacja_meteorologiczna (
  kod_stacji INT NOT NULL AUTO_INCREMENT,
  nazwa_stacji VARCHAR(45) NOT NULL,
  wysokosc_npm INT NULL,
  wojewodztwo VARCHAR(45) NULL,
  powiat VARCHAR(45) NULL,
  gmina VARCHAR(45) NULL,
  funkcja_stacji_id_funk_stacji INT NOT NULL,
  PRIMARY KEY (kod_stacji),
  FOREIGN KEY (funkcja_stacji_id_funk_stacji)
  REFERENCES funkcja_stacji (id_funk_stacji));
  
  
  
-- -----------------------------------------------------
-- Table pracownik		5
-- -----------------------------------------------------
  
  CREATE TABLE IF NOT EXISTS pracownik (
  id_pracownik INT NOT NULL AUTO_INCREMENT,
  imie VARCHAR(45) NOT NULL,
  nazwisko VARCHAR(45) NOT NULL,
  data_urodzenia DATE NULL,
  nfz_rejon VARCHAR(45) NULL,
  pensja decimal(9,2) NULL,
  id_loginu_l INT NOT NULL,
  kod_stacji_p INT NOT NULL,
  id_funk_prac_p INT NOT NULL,
  PRIMARY KEY (id_pracownik),
    FOREIGN KEY (id_loginu_l)
    REFERENCES logowanie (id_loginu),
    
	FOREIGN KEY (kod_stacji_p)
    REFERENCES stacja_meteorologiczna (kod_stacji),
   
    FOREIGN KEY (id_funk_prac_p)
    REFERENCES funkcja_pacownicza (id_funk_prac))
;

-- -----------------------------------------------------
-- Table czujniki	6
-- -----------------------------------------------------


CREATE TABLE IF NOT EXISTS czujniki (
  id_czujnika INT NOT NULL AUTO_INCREMENT,
  nazwa VARCHAR(45) NOT NULL,
  producent VARCHAR(45) NOT NULL,
  rok_produkcji DATE NOT NULL,
  pomiar VARCHAR(45) NOT NULL,
  cena decimal (9,2) NOT NULL,
  PRIMARY KEY (id_czujnika))
;

-- -----------------------------------------------------
-- Table stacja_meteorologiczna_has_czujniki		7
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS stacja_meteorologiczna_has_czujniki (
  id_stacja_meteorologiczna_has_czujniki int primary key not null auto_increment,
  stacja_meteorologiczna_kod_stacji INT NOT NULL,
  czujniki_id_czujnika INT NOT NULL)
;


-- -----------------------------------------------------
-- Table temperatura	8
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS temperatura (
  id_temp int not null auto_increment,
  czas_pomiaru DATETIME NOT NULL,
  termometr DECIMAL(4,2) NULL,
  kod_stacji_t_st INT NOT NULL,
  PRIMARY KEY (id_temp),
    FOREIGN KEY (kod_stacji_t_st)
    REFERENCES stacja_meteorologiczna (kod_stacji))
 ;
 
 
 -- -----------------------------------------------------
-- Table cisnienie		9
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS cisnienie (
  id_cis int primary key not null auto_increment,
  czas_pomiaru datetime not null,
  cisnienie_p_m INT NULL,
  kod_stacji_c_st INT NOT NULL,
     FOREIGN KEY (kod_stacji_c_st)
    REFERENCES stacja_meteorologiczna (kod_stacji))
;

-- -----------------------------------------------------
-- Table wiatr		10
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS wiatr (
  id_wiatr int primary key not null auto_increment,
  czas_pomiaru datetime not null,
  wiatr_2m INT NULL,
  wiatr_10m INT NULL,
  wiatr_20m INT NULL,
  stacja_meteorologiczna_kod_stacji INT NOT NULL,
    FOREIGN KEY (stacja_meteorologiczna_kod_stacji)
    REFERENCES stacja_meteorologiczna (kod_stacji))
;

 - -----------------------------------------------------
-- Table aktynometria		11
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS aktynometria (
  id_aktyn int primary key not null auto_increment,
  czas_pomiaru DATETIME NOT NULL,
  prom_calkowite DECIMAL(2) NULL,
  prom_rozproszone DECIMAL(2) NULL,
  prom_bezposrednie DECIMAL(2) NULL,
  kod_stacji_a_st INT NOT NULL,
    FOREIGN KEY (kod_stacji_a_st)
    REFERENCES stacja_meteorologiczna (kod_stacji))
;






