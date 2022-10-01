# Орел и решка

# Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква "О" – соответствует выпадению Орла, а буква 
# "Р" – соответствует выпадению Решки. Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.

# Формат входных данных
# На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".

# Формат выходных данных
# Программа должна вывести наибольшее количество подряд выпавших Решек.

# Примечание. Если выпавших Решек нет, то необходимо вывести число 
# 0
# 0.

# tosses = input('Введите результат подбрасываний: ')
# repeats_headds = 0
# max_repeats = 0
# for i in range(len(tosses)-1):
#     if (tosses[i]=='Р' and tosses[i+1]=='Р'):
#         repeats_headds+=1
#     elif (tosses[i]=='Р' and tosses[i+1]=='О'):
#         if max_repeats<repeats_headds:
#             max_repeats=repeats_headds
#         repeats_headds=0
# print(max_repeats+1)

# text = input("Введите произвольную последовательность букв О и Р: ")
# count = 0
# max_count = 0

# for char in text:
#     if char == "Р":
#         count += 1
#     else:
#         count = 0
#     if max_count < count:
#         max_count = count
# print(max_count)

# n = input("Введите результат выпадения Орла и решки:")
# total = 0
# max = 0
# for i in n:
#     if i == 'Р':
#         total += 1
#         if total > max:
#             max = total
#     else:
#         if total > max:
#             max = total
#         total = 0
# print(max)

s=input()
t=0
while "Р"*(t+1) in s:
    t+=1
if t!=0:
    print(t)
else:
    print(0)
