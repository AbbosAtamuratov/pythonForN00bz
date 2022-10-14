# На вход программы поступает список наименований рек, записанных в одну строчку через пробел.
# Необходимо отсортировать этот список в порядке убывания длин названий.
# Результат вывести в одну строчку через пробел.
#
# Sample Input:
# Лена Енисей Волга Дон
# Sample Output:
# Енисей Волга Лена Дон

# rivers = input('Введите список рек через пробел: ')
# rivs = list(rivers.split())
# len_riv=[]
# for i in rivs:
#     len_riv.append(len(i))
# result = list(zip(rivs, len_riv))
# result.sort(key=lambda x: x[1], reverse=True)
# print(result)

s=sorted(input().split(), key=lambda x: len(x))[::-1]
print(*s)
