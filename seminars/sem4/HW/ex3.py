# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

from copy import copy


poly1='C:\\Users\\МSI\\Desktop\\Python for n00bz\\seminars\\sem4\\HW\\Poly1.txt'
poly2='C:\\Users\\МSI\\Desktop\\Python for n00bz\\seminars\\sem4\\HW\\Poly2.txt'

with open(poly1,'r') as p1:
    for i in p1:    
        first=list(map(str,i.split('+')))

with open(poly2,'r') as p1:
    for i in p1:    
        second=list(map(str,i.split('+')))
 
def StripPoly (poly): # превращает многочлен в список кортежей (коэффицент, степень)
    res = []
    for i in poly:
        if i[-1]=='x':
            res.append((int(i[:-1]), 1))
        elif  i[-1]=='0':
            res.append((int(i[:-2]), 0))
        else:    
            res.append((int(i[:-3]),int(i[-1])))
    return res

def MinimizePolys(poly1, poly2): # На основе входных многочленов возвращает новый список кортежей,
                                 # с вырезанными членами со степенью встречающейся в обоих многочленах
    res=[]
    mid=[]
    powers1 = [i[1] for i in poly1]
    powers2 = [i[1] for i in poly2]
    if len(powers1)>len(powers2):
        while len(powers1)>len(powers2):
            powers2.append(0)
    elif len(powers1)<len(powers2):
        while len(powers2)>len(powers1):
            powers1.append(0)
    for i in range(len(powers1)):
        if powers1[i] not in powers2:
            mid.append(powers1[i])
        if powers2[i] not in powers1:
            mid.append(powers2[i])
    for i in poly1:
        if i[1] in mid:
            res.append(i)
    for i in poly2:
        if i[1] in mid:
            res.append(i)
    return res

def SumPolys (poly1, poly2): # сначала суммирует члены с одинаковой степенью потом дописывает оставшиеся
    res = []
    mid = poly1+poly2
    for i in range(len(mid)-1):
        for j in range(i+1, len(mid)):
            selected = mid[i]
            compared = mid[j]
            if selected[1] == compared[1]:
                res.append((selected[0]+compared[0], selected[1]))
    res = res+ MinimizePolys(poly1, poly2)
    res.sort(key=lambda x: x[1], reverse=True)
    return res

def printPoly (inp_list):
    for i in inp_list:
        if i[1] > 1:
            print(f'{i[0]}x^{i[1]}', end='+')
        elif i[1] == 1:
            print(f'{i[0]}x', end='+')
        elif i[1] == 0:
            print(f'{i[0]}=0')


a, b = StripPoly(first), StripPoly(second)
printPoly (SumPolys(a,b))


