# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным

day = int(input('Введите число от 1 до 7: '))-1
week = ['понедельник','вторник','среда','четверг','пятница','суббота','воскресенье', 'Некорректный ввод попробуйте ещё раз.']
while day>=7 or day<0:
    print(week[7])
    day = int(input('Введите число от 1 до 7: '))-1
else:
    print(week[day])