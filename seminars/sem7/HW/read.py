# модуль чтения отображения
# 1. Отобразить весь справочник\n"
# "2. Найти абонента по фамилии\n"
# "3. Найти абонента по номеру телефона\n"
# "4. Добавить абонента в справочник\n"
# "5. Сохранить справочник в текстовом формате\n"
# "6. Закончить работу")
def Help():
    print('showAll - Отобразить весь справочник')
    print('findByName - Найти абонента по фамилии')
    print('findByTel - Найти абонента по номеру телефона')
    print('addContact - Добавить абонента в справочник')
    print('delContact - Удалить абонента из справочника')
    print('save - Сохранить справочник в текстовом формате')
    print('quit - Закончить работу')


def ShowALL(inp_dict):
    for i in inp_dict:
        print(i)


test = [('name', 'tel', 'coment'), ('name1', 'tel1', 'coment1')]
test = enumerate(test, 1)
ShowALL(test)