# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число

from pdb import line_prefix


n = int(input('Введите число: '))
numbers = list(range(-n,n+1))
sum=0
pos = []
file='C:\\Users\\МSI\\Desktop\\Python for n00bz\\seminars\\sem2\\HW\\positions.txt'
with open(file,'r') as data:
    for line in data:
        pos.append(int(line))
    print (numbers, '\n', pos)
    for i in range(len(pos)):
        index=pos[i]
        sum+=numbers[index]
    print (sum)