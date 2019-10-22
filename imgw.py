




class Login:
    def __init__(self, login, haslo):
        self.login = login
        self.haslo = haslo


class Funkcja_pracownicza:
    def __init__(self, stanowisko, max_wynagordzenie, min_wynagrodzenie):
        self.stanowisko = stanowisko
        self.max_wynagrodzenie = max_wynagordzenie
        self.min_wynagrodzenie = min_wynagrodzenie


class Funkcja_stacji:
    def __init__(self, funkcja):
        self.funkcja = funkcja


class Stacja_meteorologiczna:
    def __init__(self, nazwa_stacji, wysokosc_npm, wojewodztwo, powiat, gmina, funkcja_stacji_id_funk_stacji)
        self.nazwa_stacji = nazwa_stacji
        self.wysokosc_npm = wysokosc_npm
        self.wojewodztwo = wojewodztwo
        self.powiat = powiat
        self.gmina = gmina
        self.funkcja_stacji_id_funk_stacji = funkcja_stacji_id_funk_stacji


class Pracownik:
    def __init__(self, imie, nazwisko, data_urodzenia, nfz_rejon, pensja, id_loginu_l, kod_stacji_p, id_funk_prac_p):
        self.imie = imie
        self.nazwisko = nazwisko
        self.data_urodzenia = data_urodzenia
        self.nfz_rejon = nfz_rejon
        self.pensja = pensja
        self.id_loginu_l = id_loginu_l
        self.kod_stacji_p = kod_stacji_p
        self.id_funk_prac_p = id_funk_prac_p

class Czujniki:
    def __init__(self, nazwa, producent, rok_produkcji, pomiar, cena):
        self.nazwa = nazwa
        self.producent = producent
        self.rok_produkcji = rok_produkcji
        self.pomiar = pomiar
        self.cena = cena

