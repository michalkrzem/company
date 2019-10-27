




class Login:
    def __init__(self, login, haslo, uprawnienia):
        self.login = login
        self.haslo = haslo
        self.uprawnienia = uprawnienia


class FunkcjaPracownicza:
    def __init__(self, stanowisko, max_wynagordzenie, min_wynagrodzenie):
        self.stanowisko = stanowisko
        self.max_wynagrodzenie = max_wynagordzenie
        self.min_wynagrodzenie = min_wynagrodzenie


class FunkcjaStacji:
    def __init__(self, funkcja):
        self.funkcja = funkcja


class StacjaMeteorologiczna:
    def __init__(self, nazwa_stacji, wojewodztwo, funkcja_stacji_id_funk_stacji):
        self.nazwa_stacji = nazwa_stacji
        self.wojewodztwo = wojewodztwo
        self.funkcja_stacji_id_funk_stacji = funkcja_stacji_id_funk_stacji


class Pracownik:
    def __init__(self, imie, nazwisko, pensja, id_loginu_l, kod_stacji_p, id_funk_prac_p):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja
        self.id_loginu_l = id_loginu_l
        self.kod_stacji_p = kod_stacji_p
        self.id_funk_prac_p = id_funk_prac_p

class Czujniki:
    def __init__(self, producent, pomiar, cena):
        self.producent = producent
        self.pomiar = pomiar
        self.cena = cena


class StacjaMaCzujniki:
    def __init__(self, stacja_meteorologiczna_kod_stacji, czujniki_id_czujnika):
        self.stacja_meteorologiczna_kod_stacji = stacja_meteorologiczna_kod_stacji
        self.czujniki_id_czujnika = czujniki_id_czujnika


class Temperatura:
    def __init__(self, ):
        self.czas_pomiaru = czas_pomiaru
        self.termometr = termometr
        self.kod_stacji_t_st = kod_stacji_t_st


class Cisnienie:
    def __init__(self):
        self.czas_pomiaru = czas_pomiaru
        self.cisnienie_p_m = cisnienie_p_m
        self.kod_stacji_c_st = kod_stacji_c_st


class Aktynometria:
    def __init__(self, czas_pomiaru, prom_calkowite, prom_odbite, kod_stacji_a_st):
        self.czas_pomiaru = czas_pomiaru
        self.prom_calkowite = prom_calkowite
        self.prom_odbite = prom_odbite
        self.kod_stacji_a_st = kod_stacji_a_st













