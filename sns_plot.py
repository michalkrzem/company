import matplotlib.pyplot as plt
from files.imgw_project.analyse import dane_pomiarowe
import random
df = dane_pomiarowe()



def ploty():

    plt.figure()
    plt.subplot(211)
    plt.plot(range(1,2429), df['Calkowite_CNR[mV]'], color='blue', marker='.')
    plt.plot(range(1,2429), df['Odbite_CNR[mV]'], color='red')
    plt.xlabel("Data pomiaru")
    plt.ylabel("mV")
    plt.title("Promieniowanie calkowite i odbite [mv]")
    plt.tight_layout()



    plt.subplot(212)
    plt.plot(range(1,2429), df['Temperatura'], color='tab:orange', linestyle='-')
    plt.xlabel("Data pomiaru")
    plt.title("Temperatura")
    plt.title("mV")
    plt.tight_layout()

    plt.show()

if __name__ == '__main__':
    print(ploty())