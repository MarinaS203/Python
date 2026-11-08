#Domaci od 5. novembra - list, set, tuple, dictionary

# 1. Napisati funkciju get_even_positions(data: tuple) -> tuple koja
# vraća elemente torke koji se nalaze na parnim indeksima (0, 2, 4...).
# Input: (10, 20, 30, 40, 50, 60)
# Output: (10, 30, 50)

def get_even_positions(data: tuple) -> tuple:
    even_indexes=list()
    list_of_data=list(data)
    for i in range(0, len(list_of_data),2):
        even_indexes.append(list_of_data[i])
    return tuple(even_indexes)  

get_even_positions((10, 20, 30, 40, 50, 60))
        
# 2. Napisati funkciju find_exclusive_students(group1: set, group2:set) -> set koja vraća studente koji se nalaze u prvoj grupi, ali ne i u drugoj.
# Input: {'Ana','Marko','Jovan','Milica'}, {'Marko','Milica','Petar'} 
# Output: {'Ana','Jovan'}

def find_exclusive_students(group1: set, group2:set) -> set:
    return group1-group2

find_exclusive_students({'Ana','Marko','Jovan','Milica'}, {'Marko','Milica','Petar'})

# 3. Napisati funkciju clean_tags(text: str) -> str koja obrađuje tekst sa tagovima.
# Potrebno je:
# Razdvojiti tagove koji su odvojeni karakterom |
# Ukloniti početne i krajnje razmake svakog taga
# Sva slova pretvoriti u mala slova
# Spojiti tagove karakterom -

def clean_tags(text: str) -> str:
    clean=text.lower().split('|')
    # print(clean)
    new=list()
    for c in clean:
        new.append(c.strip())
    # print(new)
    clean_string=''
    for i in range(len(new)):
        if i!=len(new)-1:
            clean_string+=new[i]+'-'
        else:
            clean_string+=new[i]
            
    return(clean_string)

clean_tags(' Apple | orangE | CheRRy ')

# 4. Napisati funkciju count_products(csv_lines: list) -> dict koja analizira porudžbine iz CSV podataka i vraća ukupan broj naručenih proizvoda. Svaki red sadrži ime kupca, naziv proizvoda i količinu, razdvojene zarezom. Prvi red predstavlja zaglavlje i treba ga zanemariti. Ako se isti proizvod pojavljuje u više redova, sabrati njegove količine.
# Input: ['customer,product,quantity',
# 'Alice,laptop,2',
# 'Bob,mouse,3',
# 'Alice,laptop,1',
# 'Charlie,keyboard,2',
# 'Bob,mouse,1'
# ]
# Output: {'laptop': 3,
#          'mouse': 4,
#          'keyboard': 2
# }

def count_products(csv_lines: list) -> dict:
    new_dict={}
    new_list=[]
    for l in csv_lines[1:]:
        new_list.append(l.split(','))
    # print(new_list)
    for l in new_list:
        if l[1] in new_dict:
            new_dict[l[1]]+=int(l[2])
        else:
            new_dict[l[1]]=int(l[2])
    print(new_dict)
    
count_products(['customer,product,quantity',
'Alice,laptop,2',
'Bob,mouse,3',
'Alice,laptop,1',
'Charlie,keyboard,2',
'Bob,mouse,1'
])
