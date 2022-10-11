#  Дан список, вывести отдельно буквы и цифры.


# inp_string = list(map(str, input('Введите строку: ').split()))
# result_digits = [i for i in inp_string if i.isdigit()==True]
# result_letters = [i for i in inp_string if i.isdigit()==False]
# print(result_digits, '\n', result_letters)

a = ( "a", 'b', '2', '3' ,'c')
b = ( 'a' , 'b' , 'c')
c = ( '1', '2', '3')
 

b= filter(str.isalpha, a)
c= filter(str.isdigit, a)

print(*b)
print(*c)
