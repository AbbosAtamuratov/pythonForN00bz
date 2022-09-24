#Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x=False
y=False
z=False
leftside = not(x and y and z)
rightside = (not x) and (not y) and (not z)  
print(leftside == rightside)