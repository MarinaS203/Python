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
m['home_team'] #Tim je 'BRU'

# 1.Prikazati sve utakmice u kojima je učestvovao.

m.loc[(m['home_team']=='BRU') | (m['away_team']=='BRU')] #38 utakmica

# 2.Koliko je puta pobedio, izgubio i odigrao nerešeno?

m['goal_diff']=m['home_goals']-m['away_goals']
# m['goal_diff']
m['result']='D'
# m['result']
m.loc[m['goal_diff'] <0, 'result'] ='A'
m.loc[m['goal_diff'] >0, 'result'] ='H'

# len(m[((m['result']=='H') & (m['home_team']=='BRU')) | ((m['result']=='A') & (m['away_team']=='BRU'))]) 
# #ukupno 10 pobeda, kod kuce i u gostima

# len(m[((m['result']=='A') & (m['home_team']=='BRU')) | ((m['result']=='H') & (m['away_team']=='BRU'))]) 
# #ukupno 16 poraza, kod kuce i u gostima

# len(m[(m['result']=='D') & ((m['home_team']=='BRU') | (m['away_team']=='BRU'))]) 
# #12 neresenih utakmica, kod kuce i u gostima


# # 3.Koliko je golova postigao kao domaćin, a koliko kao gost?

# m.loc[m['home_team'] == 'BRU', 'home_goals'].sum() #23 gola kao domacin
# m.loc[m['away_team'] == 'BRU', 'away_goals'].sum() #16 golova kao gost


# 4.Pronaći utakmicu u kojoj je postigao najviše golova.

home=m.loc[m['home_team'] == 'BRU', 'home_goals']
away=m.loc[m['away_team'] == 'BRU', 'away_goals']
home.max()
#ovo treba da doradim
