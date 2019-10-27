from bs4 import BeautifulSoup
import requests
import time


page = requests.get("http://www.igf.fuw.edu.pl/~kmark/stacja/pracownia/Adam.dat")
html = BeautifulSoup(page.content, 'html.parser')

date_before = time.localtime()
date = date_before.tm_year, date_before.tm_mon, date_before.tm_mday - 1

naglowek = "Dzien Miesiac Rok Godzina Minuta Sekunda Calkowite_CNR[mV] Odbite_CNR[mV] Dl_atmosfery_CNR[mV] Dl_ziemi_CNR[mV] Temperatura"


file = open(str(date).strip('()').replace(', ', '-') + '.csv', 'w')


file.write(naglowek + '\n')

file.write(str(html))
