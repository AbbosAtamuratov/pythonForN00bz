# Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. Теперь он использует их в качестве серверов "Пегого дудочника".
#  Помогите владельцу фирмы отыскать все зараженные холодильники.

# Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, 
# и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы, главное наличие последовательности букв), 
# то холодильник заражен и нужно вывести номер холодильника, нумерация начинается с единицы


# Формат входных данных
# В первой строке подаётся число 
# n
# n – количество холодильников. В последующих 
# n
# n строках вводятся строки, содержащие латинские строчные буквы и цифры, в каждой строке от 
# 5
# 5 до 
# 100
# 100 символов.

# Формат выходных данных
# Программа должна вывести номера зараженных холодильников через пробел. Если таких холодильников нет, ничего выводить не нужно.

data = "fridges.txt"
file=open(data,'r')
line=1
for line in file:
    for i in line:
        if 'a' in line[i]: 

# построчный перебор со вложенными условиями на нахождение каждой последущей буквы слова anton в строке