#  Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.

n=int(input('Введите число: '))
for i in range (n):
    print(f'{(-3)**i} ', end=' ')