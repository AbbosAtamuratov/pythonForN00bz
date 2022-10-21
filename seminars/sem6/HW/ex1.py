# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением
# дробной части элементов.

chisla = list(map(str, input('Введите вещественное числа через пробел: ').split()))
sep_floats= lambda x: list(map(str, x.split('.')))
numbers = [sep_floats(i) for i in chisla]
for i in numbers:
    i[1] = 10**(-len(i[1]))*int(i[1])
numbers.sort(key=lambda x: x[1], reverse=True)
print(numbers[0][1]-numbers[-1][1])

# lis1 = [1.1,2.2,3.001,4.4]
# lis2 = [round(lis1[n] - round(lis1[n]),10) for n in range(0,len(lis1))]
# print('Задание 2: ', max(lis2)-min(lis2))

# numbers = [2, 3, 4, 7, 6, 7, 9]
# diff = list([a*b for a, b in zip(numbers, numbers[:(len(numbers)//2) - 1: -1])])
# print(diff)
