# Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа. 
# Реализовать программу с использованием функции filter. Результат отобразить на экране в виде 
# последовательности оставшихся чисел в одну строчку через пробел.


# sequence = list(map(int, input('Введите список целых чисел в одну строчку через пробел: ').split()))
# isItOk = list(filter((lambda x: True if 9 < x < 100 else False), sequence))
# print(isItOk)

data = [1, 33, 55, 1, 56, 113, 123, 23, 34]
result = list(filter(lambda x: 9 < x < 100, data))
print(*result)

def ser (x):
    if 9 < x < 100: return True

result = filter(ser, data)
print(*list(result))


# print(*list(filter(lambda x: len(str(abs(int(x)))) == 2, input().split())))
