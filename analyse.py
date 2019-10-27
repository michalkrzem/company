import pandas as pd


df = pd.read_csv('2019-10-261.csv', sep=' ')
df['Rok'] = df['Rok'].astype(str)
df['Miesiac'] = df['Miesiac'].astype(str)
df['Dzien'] = df['Dzien'].astype(str)


df['Data_pomiaru'] = df['Rok'] + '-' + df['Miesiac'] + '-' + df['Dzien']

print(df)
