# .1. Napisati program kojim se prevodi temperatura iz Celzijusove skale u Farenhajtovu skalu,
# ako je odgovaraju´ca formula oblika T [◦F] = T [◦C] · 1.80 + 32. Na ulazu se unosi vrednost
# temperature u stepenima Celzijusa (realan broj) a ispisuje se vrednost temperature u stepenima
# Farenhajta.

c=15
def c_to_f (celsius):
    print (round(celsius*1.80 +32,2))

c_to_f(c)

# 2. Napisati program koji za uneti redni broj dana u nedelji (od 1 do 7) ispisuje naziv tog
# dana (ponedeljak - nedelja). Ukoliko je unet broj koji nije izmed¯u 1 i 7, ispisati Pogresan
# unos.

days=['Ponedeljak', 'Utorak', 'Sreda', 'Cetvrtak', 'Petak', 'Subota', 'Nedelja']

day=2

def day_of_week(day):
    if day not in range(1,8):
        print('Pogresan unos!')
    else:
        print(f'{days[day-1]}')

day_of_week(day)

# 3. Napisati program koji racuna najveci negativni element u listi.

list=[1,5,-7,-3,25,-98]

def minimum (list):
    min=-99999999
    for i in range (0, len(list)):
        if list[i]<0:
            if list[i]>min:
                min=list[i]
    return min

minimum(list)

# 5. Napisati program koji racuna broj parnih elemenata date liste.

list1=[1,4,6,7,9,12,22,24,28]

def count (list):
    sum=0
    for i in range(0, len(list)):
        if list[i]%2==0:
            sum+=1
    return sum

count(list1)

# 6. Napisati program koji racuna sume elemenata liste celih brojeva koji su deljivi sa 2 odnosno
# sa 3

lista2=[1,2,3,6,9,12,18,21]

def sum (list):
    suma=0
    for i in range(0, len(list)):
        if list[i]%2==0 and list[i]%3==0: #moglo je i samo list[i]%6==0
            suma+=list[i]
    return suma

sum(lista2)