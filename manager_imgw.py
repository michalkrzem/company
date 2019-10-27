from files.imgw_project.imgw import Login, FunkcjaPracownicza, FunkcjaStacji, StacjaMeteorologiczna, Pracownik, Czujniki, Aktynometria
from files.imgw_project.config import host, user, password, db
import pymysql
import sys


class ImgwManager:
    def __init__(self, host='localhost', user='kvothe', password='dexter', db='imgw_manager', charset='utf8'):
        """
        class constructor:
        -) connect to DB
        """
        try:
            self.conn = pymysql.connect(host, user, password, db)
            print("Połączono z bazą danych")
        except:
            print("Problem z połączniem")


class PracownikManager(ImgwManager):
    def __init__(self, host, user, password, db, charset='utf8'):
        super().__init__(host, user, password, db, charset='utf8')

    def add_aktynometria(self, aktynometria):
        cursor = self.conn.cursor()
        cursor.execute(
            "insert into aktynometria(czas_pomiaru, prom_calkowite, prom_odbite, kod_stacji_a_st) values('%s', %.2f, %.2f, %d);" % (
                aktynometria.czas_pomiaru, aktynometria.prom_calkowite, aktynometria.prom_odbite, aktynometria.kod_stacji_a_st))
        self.conn.commit()


class AdministratorManager(PracownikManager):
    def __init__(self, host, user, password, db, charset='utf8'):
        super().__init__(host, user, password, db, charset='utf8')

    def add_funkcja_pracownicza(self, funkcja):
        cursor = self.conn.cursor()
        cursor.execute(
            "insert into funkcja_pacownicza(stanowisko, max_wynagordzenie , min_wynagrodzenie) values('%s', %d,  %d);" % (
            funkcja.stanowisko, funkcja.min_wynagrodzenie, funkcja.max_wynagrodzenie))
        self.conn.commit()

    def add_user_to_logowanie(self, user):
        cursor = self.conn.cursor()
        cursor.execute(
            "insert into logowanie(login, haslo, uprawnienia) values('%s', '%s',  '%s');" % (
            user.login, user.haslo, user.uprawnienia))
        self.conn.commit()
        return self.get_id_logowania(user)

    def get_id_logowania(self, user):
        cursor = self.conn.cursor()
        cursor.execute(
            "select id_loginu from logowanie where login='%s' and haslo='%s';" % (
                user.login, user.haslo,))
        return cursor.fetchall()

    def add_funkcja_stacji(self, funkcja_stacji):
        cursor = self.conn.cursor()
        cursor.execute(
            "insert into funkcja_stacji(funkcja) values('%s');" % (
                funkcja_stacji.funkcja))
        self.conn.commit()

    def get_id_funk_prac(self, stanowisko):
        cursor = self.conn.cursor()
        cursor.execute(
            "select id_funk_prac from funkcja_pacownicza where stanowisko='%s';" % (
                stanowisko))
        return cursor.fetchall()

    def add_stacja_meteorologiczna(self, stacja_meteo):
        cursor = self.conn.cursor()
        cursor.execute(
            "insert into stacja_meteorologiczna(nazwa_stacji, wojewodztwo, funkcja_stacji_id_funk_stacji) values('%s', '%s',%d);" % (
                                stacja_meteo.nazwa_stacji, stacja_meteo.wojewodztwo, stacja_meteo.funkcja_stacji_id_funk_stacji))
        self.conn.commit()


    def get_id_stacji_meteo(self, nazwa_stacji):
        cursor = self.conn.cursor()
        cursor.execute(
            "select kod_stacji from stacja_meteorologiczna where nazwa_stacji='%s';" % (nazwa_stacji))
        return cursor.fetchall()





    def add_czujniki(self, czujnik):
        cursor = self.conn.cursor()
        cursor.execute(
            "insert into czujniki(producent, pomiar, cena) values('%s', '%s',%d);" % (
                czujnik.producent, czujnik.pomiar, czujnik.cena))
        self.conn.commit()


    def add_stacja_ma_czujniki(self):
        cursor = self.conn.cursor()
        cursor.execute(
            "select * from czujniki;")
        print(cursor.fetchall())
        kod_stacji = int(input("Podaj kod stacji"))
        cursor.execute(
            "select * from stacja_meteorologiczna;")
        print(cursor.fetchall())
        id_czujnika = int(input("Podaj id czujnika"))
        cursor.execute(
            "insert into stacja_meteorologiczna_has_czujniki(stacja_meteorologiczna_kod_stacji, czujniki_id_czujnika) values(%d, %d);" % (
                kod_stacji, id_czujnika))
        self.conn.commit()


    def add_pracownik(self, pracownik):
        cursor = self.conn.cursor()
        cursor.execute(
            "insert into pracownik(imie, nazwisko, pensja, id_loginu_l, kod_stacji_p, id_funk_prac_p) values('%s', '%s', %d, %d, %d, %d) " % (
             pracownik.imie, pracownik.nazwisko, pracownik.pensja, pracownik.id_loginu_l, pracownik.kod_stacji_p,
             pracownik.id_funk_prac_p))
        self.conn.commit()



###########################             PANEL LOGOWANIA             #############################
imgw_manager = ImgwManager(host, user, password, db)
imgw_manager.cursor = imgw_manager.conn.cursor()
print("PANEL LOGOWANIA")
login = input("Podaj login ")
haslo = input("Podaj haslo ")

while True:
    try:
        imgw_manager.cursor.execute(
            "select p.imie, p.nazwisko, l.uprawnienia from logowanie l join pracownik p on l.id_loginu = p.id_loginu_l where '%s' = 'kvothe' and '%s' = 'dexter';" %
            (login, haslo))

        powitanie = imgw_manager.cursor.fetchall()

    except IndexError:
        print("Bledne dane logowania, zle haslo lub login")
        login = input("Podaj login ")
        haslo = input("Podaj haslo ")

    finally:
        print("Witaj %s %s (%s IMGW)" % (powitanie[0][0], powitanie[0][1], powitanie[0][2]))

        if powitanie[0][2] == 'administrator':
            imgw_manager = AdministratorManager(host, user, password, db)

            print("Jako amdinistrator możesz modyfikować dane w bazie danych. Wybierz działania:")
            dzialanie = input("Wprowadz nowego pracownika d \n")
            if dzialanie == 'd':
                imie = input("Podaj imie: ")
                nazwisko = input("Podaj nazwisko: ")
                pensja = int(input("Podaj wynagrodzenie brutto: "))
                login_u = input("Podaj login: ")
                haslo_u = input("Podaj haslo: ")
                uprawnienia = input("Podaj uprawnienia: ")
                nazwa_stacji = input("Podaj nazwe stacji: ")
                stanowisko = input("Podaj stanowisko: ")

                user = Login(login_u, haslo_u, uprawnienia)
                pracownik = Pracownik(imie, nazwisko, pensja,
                                      imgw_manager.add_user_to_logowanie(user)[0][0],
                                      imgw_manager.get_id_stacji_meteo(nazwa_stacji)[0][0],
                                      imgw_manager.get_id_funk_prac(stanowisko)[0][0])
                imgw_manager.add_pracownik(pracownik)
            break
        else:
            print("cos nie tak")


#################################################################################################
#################################################################################################
# imgw_manager = AdministratorManager(host, user, password, db)
# aktynometria = Aktynometria('2018-02-01', 232, 240, 1)
# imgw_manager.add_aktynometria(aktynometria)

# imgw_manager = AdministratorManager(host, user, password, db)
######################################################                  logowanie
# userzy = Login(user, password, 'administrator')
# imgw_manager.add_user_to_logowanie(userzy)

######################################################                  funkcja pracownicza
# funkcja1 = FunkcjaPracownicza('mlodszy specjalista', 2000, 3000)
# funkcja2 = FunkcjaPracownicza('specjalista', 3100, 4000)
# funkcja3 = FunkcjaPracownicza('starszy specjalista', 4100, 5000)
# funkcja4 = FunkcjaPracownicza('expert', 5100, 6000)
# funkcje = [funkcja2, funkcja3, funkcja4]
# for funkcja in funkcje:
#     imgw_manager.add_funkcja_pracownicza(funkcja)
########################################################################################################
# funkcja_stacji = FunkcjaStacji('Klimat')
# imgw_manager.add_funkcja_stacji(funkcja_stacji)
# ######################################################################################################
# stacja_meteo = StacjaMeteorologiczna('Warszawa', 'mazowieckie', 1)
# imgw_manager.add_stacja_meteorologiczna(stacja_meteo)
# ######################################################################################################
# czujnik = Czujniki('Kipp', 'promieniowanie', 6000)
# imgw_manager.add_czujniki(czujnik)
# ######################################################################################################
# imgw_manager.add_stacja_ma_czujniki()
# ######################################################################################################
# pracownik = Pracownik("Michal", "Krzeminski", 3000, 1, 1, 1)
# imgw_manager.add_pracownik(pracownik)
# ######################################################################################################
# pracownik_manager = PracownikManager(host, user, password, db)
# aktynometria = Aktynometria('2018-01-01', 23.92, 24.72, 1)
# pracownik_manager.add_aktynometria(aktynometria)
#########################################################################################################
#########################################################################################################
