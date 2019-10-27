import pandas as pd
import numpy as np

def dane_pomiarowe():
    # with open('2019-10-26.csv', 'r') as f:
    #     licz = 0
    #     for line in f:
    #         if licz % 2 == 0:
    #             line = line.rstrip()
    #             file = open('output.csv', 'a')
    #             file.write(line)
    #             file.write('\n')
    #         licz += 1

    df1 = pd.read_csv('output.csv',  sep=' ', header=0,  low_memory=False, error_bad_lines=False)

    df = pd.DataFrame(df1)

    df['Rok'] = df['Rok'].astype(str)
    df['Miesiac'] = df['Miesiac'].astype(str)
    df['Dzien'] = df['Dzien'].astype(str)
    df['Godzina'] = df['Godzina'].astype(str)
    df['Minuta'] = df['Minuta'].astype(str)
    df['Sekunda'] = df['Sekunda'].astype(str)


    print(df.dtypes)

    df['Data_pomiaru'] = df['Rok'] + '-' + df['Miesiac'] + '-' + df['Dzien']+ ' ' + df['Godzina']+ ':' + df['Minuta'] + ':'+df['Sekunda']

    return df

columns=['Dzien', 'Miesiac', 'Rok', 'Godzina', 'Minuta', 'Sekunda', 'Calkowite_CNR[mV]', 'Odbite_CNR[mV]', 'Dl_atmosfery_CNR[mV]', 'Dl_ziemi_CNR[mV]', 'Temperatura']

if __name__ == '__main__':
    print(dane_pomiarowe())

