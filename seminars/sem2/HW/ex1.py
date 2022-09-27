# Напишите программу, которая принимает вещественное число и считает сумму его цифр

def DigitSum (chislo_list):
    sum = 0
    for i in range(len(chislo_list)):
        while chislo_list[i]>0:
            sum+=chislo_list[i]%10
            chislo_list[i]=chislo_list[i]//10
    return sum

chislo = list(map(int, input('Введите вещественное: ').split('.')))
print(DigitSum(chislo))