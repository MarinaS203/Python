# 4. Napisati program koji racuna srednju vrednost i standardnu devijaciju liste razlomljenih
# brojeva. Srednja vrednost i standardna devijacija racunaju se po formulama:
import math
from fractions import Fraction

list4=[Fraction(1,3), Fraction(2,5), Fraction(7,8), Fraction(1,2)]
f1=Fraction(10,15)
print(f1)
print(list4)

def mean_value (lista):
    sum=0
    for i in range(0, len(lista)):
        sum+=lista[i]
    return(round(sum/len(lista),2))

print(mean_value(list4))

# def std_dev(lista):
#     n=len(lista)
#     mean=(sum(list))/n
#     variance=0
#     for i in range(0, len(list)):
#         variance+=(lista[i]-mean)**2
#     var=variance/(n-1)
#     return math.sqrt(var)

# print(std_dev(list4))
#Htela sam i ovo da uradim, ali negde ne radi


# 7. Napisati program koji za dati niz karaktera (string) koji se sastoji samo od cifara 0-9
# racuna koliko puta se javlja svaka cifra

niz='05136871552'

list7=[num0:=0,num1:=0,num2:=0,num3:=0,num4:=0,num5:=0,num6:=0,num7:=0,num8:=0,num9:=0]

for char in niz:
    list7[int(char)]+=1

print(list7)

#8.1. Broj krajnjih pozitivnih elemenata liste. Ako poslednji element nije pozitivan, rezultat je
# 0.

lista8=[2,54,-1,8,-11,-6,7,8,3]

def num_of_elements(lista):
    num=0
    if lista[len(lista)-1]<0:
        return 0
    for i in range(len(lista)-1, -1, -1):
        if lista[i]>0:
            num+=1
        else: 
            break
    return num
        
print(num_of_elements(lista8))



# 8. 2. Maksimalni broj uzastopnih jednakih elemenata liste.
lista9=[0,1,1,2,3,4,4,4,6,9]

def max_num(lista):
    num=0
    for i in range(0, len(lista)):
        for j in range(i+1, len(lista)-1):
            if lista[i]==lista[j]:
                num+=1
            else: 
                break
            break
    return num

max_num(lista9)
        
