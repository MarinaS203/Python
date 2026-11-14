import pandas as pd

R = '/Volumes/bootcamp/northern_star/raw_2025_26/'
m=pd.read_parquet(R+'matches_2025_26.parquet')

# 1. Analiza rezultata utakmica
# 1.Pronaći sve utakmice u kojima su oba tima postigla bar po
# jedan gol.

m.loc[(m['home_goals']>=1) & (m['away_goals']>=1)] #178 utakmica

# 2.Pronaći sve utakmice u kojima je domaćin pobedio sa tačno
# jednim golom razlike.

m.loc[(m['home_goals']-m['away_goals'])==1] #105 utakmica

# 3.Koliko utakmica je završeno rezultatom 0:0?

m.loc[(m['home_goals']==0) & (m['away_goals']==0)] #26 utakmica

# 4.Prikazati 10 utakmica sa najviše ukupno postignutih golova.

m['total_goals']=m['home_goals']+m['away_goals']
m['total_goals'].nlargest(10)
#47    9
164    8
290    7
27     6
87     6
200    6
245    6
269    6
364    6
45     5



# 2. Analiza jednog tima
# Za tim po izboru:
m['home_team'] 
team='BRU' #Tim je 'BRU'
# 1.Prikazati sve utakmice u kojima je učestvovao.

m.loc[(m['home_team']==team) | (m['away_team']==team)] #38 utakmica

# 2.Koliko je puta pobedio, izgubio i odigrao nerešeno?

m['goal_diff']=m['home_goals']-m['away_goals']
# m['goal_diff']
m['result']='D'
# m['result']
m.loc[m['goal_diff'] <0, 'result'] ='A'
m.loc[m['goal_diff'] >0, 'result'] ='H'

len(m[((m['result']=='H') & (m['home_team']==team)) | ((m['result']=='A') & (m['away_team']==team))]) 
# #ukupno 10 pobeda, kod kuce i u gostima

len(m[((m['result']=='A') & (m['home_team']==team)) | ((m['result']=='H') & (m['away_team']==team))]) 
#ukupno 16 poraza, kod kuce i u gostima

len(m[(m['result']=='D') & ((m['home_team']==team) | (m['away_team']==team))]) 
#12 neresenih utakmica, kod kuce i u gostima


# 3.Koliko je golova postigao kao domaćin, a koliko kao gost?

m.loc[m['home_team'] == 'BRU', 'home_goals'].sum() #23 gola kao domacin
m.loc[m['away_team'] == 'BRU', 'away_goals'].sum() #16 golova kao gost


# 4.Pronaći utakmicu u kojoj je postigao najviše golova.

# home=(m.loc[m['home_team'] == team, 'home_goals']).max()
# home 
# away=(m.loc[m['away_team'] == team, 'away_goals']).max()
# away
# total_max=max([home, away])
# total_max
# max([(m.loc[m['home_team'] == team, 'home_goals']).max(), (m.loc[m['away_team'] == team, 'away_goals']).max()]) #vraca max vrednost, ali ne vraca ceo red
#Ovo bi bez novih funkcija moglo da se uradi tako sto trazim kada je tim bio home_team ili away_team, i kada je broj golova bio 4. Nasla sam ovu varijantu, sa idxmax(), koja vraca ceo red.

as_home_team = m[m['home_team'] == team]
as_away_team = m[m['away_team'] == team]

home_max_goals = m.loc[(as_home_team['home_goals']).idxmax()]
away_max_goals = m.loc[(as_away_team['away_goals']).idxmax()]

if (as_home_team['home_goals']).max() > (as_away_team['away_goals']).max():
    print(home_max_goals)
else:
    print(away_max_goals)


    # 3. Analiza stadiona

# 1.Prikazati sve različite stadione na kojima su odigrane
# utakmice.

m['stadium'].unique()

# 2.Pronaći stadion na kojem je odigrano najviše utakmica.

m['stadium'].value_counts() #Na svim je odigrano po 19 utakmica.

# 3.Za svaki stadion izračunati prosečnu posećenost.

avg_att = round(m.groupby('stadium')['attendance'].mean(),2) 
#nisam umela da uradim iskljucivo preko metoda koje su radjene na casu, trazila sam group by sintaksu za pandas 
avg_att

# 4.Prikazati pet stadiona sa najvećom prosečnom
# posećenošću.
avg_att.nlargest(5)