# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

poly1='C:\\Users\\МSI\\Desktop\\Python for n00bz\\seminars\\sem4\\HW\\Poly1.txt'
poly2='C:\\Users\\МSI\\Desktop\\Python for n00bz\\seminars\\sem4\\HW\\Poly2.txt'

with open(poly1,'r') as p1:
    for i in p1:    
        first=list(map(str,i.split('+')))

with open(poly2,'r') as p1:
    for i in p1:    
        second=list(map(str,i.split('+')))
 
# def MaxPower (poly1, poly2):
#     f1, f2 = poly1[0], poly2[0]
#     if int(f1[-1]) > int(f2[-1]):
#         return 1
#     elif int(f1[-1]) == int(f2[-1]):
#         return 0
#     else:
#         return 2

# def GeneralizePolys (poly1, poly2):
#     f1, f2 = poly1[0], poly2[0]
#     pow1, pow2 = int(f1[-1]), int(f2[-1])
#     route = MaxPower(poly1, poly2)
#     if route == 1:
#         delta = pow1-pow2
#         while delta >0:
#             delta = delta - 1
#             poly2.insert(0,f'0x^{pow1-delta}')
#     elif route == 2:
#         while delta >0:
#             delta = delta - 1
#             poly1.insert(0,f'0x^{pow1-delta}')
#     pp1 = CutPowers(poly1)
#     pp2 = CutPowers(poly2)

def StripPoly (poly):
    res = []
    for i in poly:
        if i[-1]=='x':
            res.append((int(i[:-1]), 1))
        elif  i[-1]=='0':
            res.append((int(i[:-2]), 0))
        else:    
            res.append((int(i[:-3]),int(i[-1])))
    return res

def SumPolys (poly1, poly2):
    res = poly1+poly2
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
# printPoly (a)

