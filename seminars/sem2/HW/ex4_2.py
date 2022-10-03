# Реализуйте алгоритм перемешивания списка.

import random

spisok=[1,2,3,4,5,6]
for i in range(len(spisok)):
    n=random.randint(0,len(spisok)-1)
    spisok[i], spisok[n] = spisok[n], spisok[i]
print(spisok)