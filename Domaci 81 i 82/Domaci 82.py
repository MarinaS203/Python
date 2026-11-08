# 19. Написати функцију get_header(path: str) -> list која враћа заглавље CSV фајла
# Користити csv.reader и next()
# Input: 'data/raw/teams.csv'
# Output: ['team', 'city', 'points']
import csv
def get_header(path: str) -> list:
    with open(path) as f:
        reader=csv.reader(f)
        return next(reader)

get_header('/Workspace/Users/tosic.marina203@gmail.com/Python/data/raw/teams.csv')

# 20. Написати функцију read_rows(path: str) -> list која враћа све редове CSV фајла без
# заглавља, као листу листи
# Користити csv.reader
# Input: 'data/raw/teams.csv'
# Output: [['FK Jedinstvo', 'Bela Palanka', '34'], ['FK Radnički', 'Niš', '41'],
# ['FK Rakovica', 'Beograd, Rakovica', '28'], ['FK Sloga', 'Kraljevo', '19']]
import csv
def read_rows(path: str) -> list:
    with open(path) as f:
        reader=csv.reader(f)
        header=next(reader)
        new_list=[]
        for r in reader:
            new_list.append(r)
        return new_list
    
read_rows('/Workspace/Users/tosic.marina203@gmail.com/Python/data/raw/teams.csv')

# 21. Написати функцију total_points(path: str) -> int која враћа збир бодова свих тимова
# Користити csv.DictReader
# Input: 'data/raw/teams.csv'
# Output: 122
import csv
def total_points(path: str) -> int:
    with open(path) as f:
        teams=list(csv.DictReader(f))
        sum=0
        for t in teams:
            sum+=int(t['points'])
        return sum

total_points('/Workspace/Users/tosic.marina203@gmail.com/Python/data/raw/teams.csv')

# 22. Написати функцију write_rows(path: str, rows: list) -> None која листу листи уписује у CSV
# фајл
# Input: 'data/processed/people.csv', [['name', 'age'], ['Ana', 20], ['Marko', 22]]
# Садржај фајла након позива:

import csv
def write_rows(path: str, rows: list) -> None:
    with open(path, mode='w', newline='') as f:
        writer=csv.writer(f)
        writer.writerows(rows)
write_rows('path', [['name', 'age'], ['Ana', 20], ['Marko', 22]] )

# 23. Написати функцију write_dicts(path: str, rows: list) -> None која листу речника уписује у
# CSV фајл
# Користити csv.DictWriter; заглавља су кључеви првог речника
# Input: 'data/processed/people.csv', [{'name': 'Ana', 'age': 20}, {'name':
# 'Marko', 'age': 22}]

import csv
def write_dicts(path: str, rows: list) -> None:
    with open(path, mode='w', newline='') as f: 
        header=list(rows[0].keys()) #vraca listu ovako, inace vraca dict_keys type, 
        #a fieldnames ocekuje listu stringova
        # print(header)
        # print(type(header))
        writer=csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(rows)

write_dicts(path, [{'name': 'Ana', 'age': 20}, {'name': 'Marko', 'age': 22}])