# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

q = int(input('Введите номер четверти: '))-1
ranges = ['x>0 и y>0','x<0 и y>0','x<0 и y<0','x>0 и y<0','Некорректный ввод попробуйте ещё раз.']

while q>=4 or q<0:
    print('Некорректный ввод. Попробуйте ещё раз')
    q = int(input('Введите номер четверти: '))-1
else:
    print(ranges[q])