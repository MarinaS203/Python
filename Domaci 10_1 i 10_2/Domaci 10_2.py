import numpy as np
import pandas as pd

# 1. Sistem beleži broj aktivnih korisnika tokom 12 uzastopnih sati.

#Htela sam da se random generise niz od 12 celih nenegativnih brojeva, sa aktivnim korisnicima. 
#Posto hocu da nakon generisanja niz bude fiksan, stavljam proizvodljnu vrednost za seed.

rng = np.random.default_rng(seed=203)
ints = rng.integers(low=1, high=100, size=12)

active_users=np.array(ints)
print(active_users)

# Prikazati broj korisnika za peti sat.
active_users[4]

# Prikazati broj korisnika za poslednja četiri sata.
active_users[-4:]

# Izračunati ukupan broj aktivnih korisnika kroz svih 12 sati.
sum_active=active_users.sum()
sum_active

# Izračunati prosečan broj korisnika po satu.
avg_active=round(active_users.mean(),2)
avg_active

# Pronaći sat sa najvećim brojem korisnika.
max_users=active_users.max()
max_users


# 2. Sistem beleži CPU, RAM i disk usage za pet različitih servera.
# Redovi predstavljaju servere, a kolone CPU, RAM i disk usage.
# Potrebno je:

# Pronaći server sa najvećom prosečnom potrošnjom resursa.
matrix=np.arange(1,16).reshape(5,3)

# Prikazati dimenzije matrice.
matrix.shape

# Napravila sam DataFrame, gde sam spakovala ove podatke, da bih na df primenila agregatne funkcije 
row_names = ['Server1','Server2','Server3','Server4','Server5']
col_names = ['CPU', 'RAM', 'Disk']
df = pd.DataFrame(matrix, index=row_names, columns=col_names)
print(df)

# Prikazati broj servera i broj metrika.
rows, cols = df.shape
print(f'Broj servera: {rows}, Broj metrika: {cols}')

# Izračunati prosečnu vrednost svake metrike.
avg_usage=df.mean()  #ovde je podrazumevana vrednost axis=0, racuna prosek po kolonama
avg_usage

# Izračunati prosečnu potrošnju resursa za svaki server.
avg_usage_of_resource=df.mean(axis=1)  #racuna prosek po redovima
avg_usage_of_resource

# Pronaći server sa najvećom prosečnom potrošnjom resursa. 
max_usage=avg_usage_of_resource.max()
max_server=df.loc[avg_usage_of_resource.idxmax()]
max_server
# print(f'Server sa najvecom potrosnjom resursa je: {max_server}, potrosnja: {max_usage}')


# 3. Sistem beleži vreme izvršavanja 15 različitih procesa u
# sekundama. Potrebno je:

rng1 = np.random.default_rng(seed=35)
seconds = np.array(rng1.integers(low=1, high=200, size=15))
seconds

# Pronaći sve procese koji su trajali duže od 100 sekundi.
print(seconds)
print(seconds[seconds>100])

# Pronaći procese koji su trajali između 40 i 100 sekundi.
print(seconds[(seconds>40) & (seconds<100)])

# Izbrojati procese koji su trajali kraće od 50 sekundi.
num_of_processes=np.sum(seconds<50)
num_of_processes

# Pronaći indekse procesa koji su trajali duže od 100 sekundi.
indexes = np.where(seconds>100)
indexes

# Izračunati prosečno vreme izvršavanja svih procesa.
avg_duration=np.mean(seconds)
avg_duration