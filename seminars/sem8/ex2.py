# Читаем Джейсона

import json

def Read_json ():
    with open('database02.json', 'r', encoding='utf-8') as dbj:
        for i in dbj:
            temp = json.loads(i)
            print(temp)

Read_json()