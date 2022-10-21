import impex as i
import read as rd
import RWDcont as rwd

booted = True
book = []

while booted:
    inp_cmd = input('Введите команду или help')
    if inp_cmd == 'quit':
        booted = False
    elif inp_cmd == 'help':
        rd.Help()
    elif inp_cmd == 'showAll':
        rd.showAll(book)
    elif inp_cmd == 'findByName':

    elif inp_cmd == 'findByTel':

    elif inp_cmd == 'addContact':

    elif inp_cmd == 'delContact':

    elif inp_cmd == 'saveTXT':

    else:
        print('Некорректный ввод. Попробуйте ещё раз.')