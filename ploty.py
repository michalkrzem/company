import matplotlib.pyplot as plt
import pandas as pd
from files.imgw_project.analyse import dane_pomiarowe

df = dane_pomiarowe()

print(df)


fig, ax = plt.subplots()
ax.plot(df['Data_pomiaru'], df[['Calkowite_CNR[mV]', 'Odbite_CNR[mV]']])

ax.grid(True, linestyle='-.')
ax.tick_params(labelcolor='r', labelsize='medium', width=3)

plt.show()
