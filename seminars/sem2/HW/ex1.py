# Напишите программу, которая принимает вещественное число и считает сумму его цифр

chislo = list(map(int, input('Введите вещественное: ').split('.')))

def DigitSum (list chislo)
    sum = 0
    for i in chislo:
        while chislo[i]==0:
            sum=+chislo[i]%10
            chislo[i]=chislo[i]//10
return sum
