# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

def PrintList (spisok):
    for i in range(len(spisok)):
        print(f'{i+1}: {spisok[i]}', end='    ')

n=int(input('Введите число: '))
spisok=[]

for i in range (1,n+1):
    spisok.append(3*i+1) 

PrintList(spisok)




