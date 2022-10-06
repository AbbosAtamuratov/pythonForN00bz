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

print(first, '\n', second)
