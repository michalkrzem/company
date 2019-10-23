from files.imgw_project.imgw import Login, FunkcjaPracownicza, FunkcjaStacji, StacjaMeteorologiczna, Pracownik
import files.imgw_project.imgw
from files.imgw_project.config import host, user, password, db
import pymysql



class ImgwManager:
    def __init__(self, host, user, password, db, charset='utf8'):
        """
        class constructor:
        -) connect to DB
        """
        try:
            self.conn = pymysql.connect(host, user, password, db)
            print("Połączono z bazą danych")
        except:
            print("Problem z połączniem")





class AdministratorManager(ImgwManager):
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











imgw_manager = AdministratorManager(host, user, password, db)

######################################################                  logowanie
# userzy = Login(user, password, 'administrator')
# imgw_manager.add_user_to_logowanie(userzy)

######################################################                  funkcja pracownicza
#funkcja1 = FunkcjaPracownicza('mlodszy specjalista', 2000, 3000)
# funkcja2 = FunkcjaPracownicza('specjalista', 3100, 4000)
# funkcja3 = FunkcjaPracownicza('starszy specjalista', 4100, 5000)
# funkcja4 = FunkcjaPracownicza('expert', 5100, 6000)
# funkcje = [funkcja2, funkcja3, funkcja4]
# for funkcja in funkcje:
#     imgw_manager.add_funkcja_pracownicza(funkcja)
#####################################################################


