# модуль работы с данными запись/поиск

def add_one(inp_list):
    item = {"name": '', "surname": '', "tel": '', "assignment": '', "wage": ''}
    item["name"] = input('Введите имя сотрудника: ')
    item["surname"] = input('Введите фамилию сотрудника: ')
    item["tel"] = input('Введите номер телефона сотрудника: ')
    item["assignment"] = input('Введите должность сотрудника: ')
    item["wage"] = input('Введите зарплату сотрудника: ')
    inp_list.append(item)


def find_name(inp_list, inp_string) -> int:
    res = -1
    for i in range(len(inp_list)):
        if inp_string == inp_list[i]["name"]:
            res = i
            break
    return res


def find_tel(inp_list, inp_tel) -> int:
    res = -1
    for i in range(len(inp_list)):
        if inp_tel == inp_list[i]["tel"]:
            res = i
            break
    return res

def find_assignment(inp_list, inp_assignment) -> int:
    res = -1
    for i in range(len(inp_list)):
        if inp_assignment == inp_list[i]["assignment"]:
            res = i
            break
    return res

def selection_salary (inp_list, inp_query) -> list:
    sel_sal = []
    for i in inp_list:
        if i["wage"] == inp_query:
            sel_sal.append(i)
    return sel_sal