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


# 4. Prodavnica beleži prihode od četiri različite kategorije proizvoda
# tokom šest meseci. Redovi predstavljaju kategorije proizvoda, a
# kolone mesece. Potrebno je:

rng2 = np.random.default_rng(seed=73)
array1=rng2.integers(low=100, high=1000, size=24)
matrix1=array1.reshape(4,6)
matrix1
# Napravila sam DataFrame, gde sam spakovala ove podatke, da bih na df primenila agregatne funkcije 
row_names1=['Proizvod1','Proizvod2','Proizvod3','Proizvod4']
col_names1=['Mesec1', 'Mesec2', 'Mesec3', 'Mesec4', 'Mesec5', 'Mesec6']
df1 = pd.DataFrame(matrix1, index=row_names1, columns=col_names1)
print(df1)

# Izračunati ukupan prihod svake kategorije proizvoda.
total_revenue_product=df1.sum(axis=1)
total_revenue_product

# Izračunati ukupan prihod za svaki mesec.
total_revenue_month=df1.sum(axis=0)
total_revenue_month

# Pronaći kategoriju proizvoda sa najvećim ukupnim prihodom.
max_rev=total_revenue_product.max()
max_rev_product=total_revenue_product.idxmax()
print(max_rev_product, max_rev)

# Pronaći mesec sa najvećim ukupnim prihodom.
max_month_sum=total_revenue_month.max()
max_month=total_revenue_month.idxmax()
print(max_month, max_month_sum)

# Izračunati prosečan prihod po kategoriji proizvoda.
avg_revenue_product=round(df1.mean(axis=1),2)
avg_revenue_product

# Izračunati prosečan mesečni prihod svih kategorija.
avg_revenue_month=round(df1.mean(axis=0),2)
avg_revenue_month

# 5. Sistem beleži prosečne dnevne temperature tokom 15 dana. Neki
# podaci nedostaju ili nisu validni.
# Validna temperatura mora biti između -20 i 50 stepeni.
# Potrebno je:

#Ovo je random generisani niz, sa float i NaN vrednostima, duzine 15
rng3=np.random.default_rng(seed=21)
data=rng3.uniform(low=-50, high=70, size=15)
data_with_nan=np.where(rng3.random(15)<0.2, np.nan, data)
s=pd.Series(data_with_nan)
arr=pd.array(data_with_nan, dtype="Float64")
print(s)

# Identifikovati nedostajuće vrednosti.
missing_values=np.isnan(s)
print(f'Nedostaju vrednosti: {missing_values}')

# Identifikovati nevalidne temperature (vrednosti manje od -20 ili
# veće od 50).
invalid=(s<-20) | (s>50)
print(f'Nevalidne temperature su: {invalid}')

# Pronaći indekse nevalidnih vrednosti.
#Zelim da kazem da mi je tek na ovom mestu palo na pamet da otvorim pdf sa casa i sad tek vidim da skoro sve ovo ima tamo, i da nisam morala da pravim ove datafrejmove niti random nizove, ali neka ovo bude umetnicka sloboda. :)
indexes1=np.where(invalid)
print(f'Indeksi nevalidnih vrednosti su: {indexes1[0]}')

# Izračunati broj nedostajućih i nevalidnih vrednosti.
count=sum(missing_values)+sum(invalid)
count

# Izračunati procenat nevalidnih i nedostajućih zapisa zajedno.
percentage=(count/s.size)*100
print("Procenat nevalidnih zapisa:", percentage, "%")

# Kreirati novi niz koji sadrži samo validne temperature.
invalid1=(s<-20) | (s>50) | np.isnan(s)
valid_s = s[~invalid1]
print("Validni niz:", valid_s)

# Izračunati prosečnu temperaturu bez nedostajućih i nevalidnih
# vrednosti.
s_clean=s.astype(float)
s_clean[invalid]=np.nan
average=np.nanmean(s_clean)
print("Prosečna vrednost niza:", round(average,2))