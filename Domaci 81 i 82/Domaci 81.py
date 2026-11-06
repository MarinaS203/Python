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

#treba da dodam 4. zadatak