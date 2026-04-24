#сделать структуру с ипсользованием json +
#сделать лёгкий интерфейс +
#написать фнукции, для красоты -
#сделать всё модульно -

import sys 
import os
import json
file_name ='expenses.json'

def load_data():
    if not os.path.exists(file_name):
        return {'categories': [], 'expenses': []}
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return {'categories': [], 'expenses': []}

def save_data(data):
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    with open(file_name, 'w', encoding='utf-8')as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

def format_cost(cost):
     if cost == int(cost):
        return int(cost)
     return cost 

def error_exit(msg):
    print(f"Ошибка: {msg}")
    sys.exit(1)

def main():
    if len(sys.argv) < 2:
        error_exit("Не указана команда Доступы: add, add-category, list, total")

    cmd = sys.argv[1].lower()
    data = load_data()

    if cmd == "add-category":
        if len(sys.argv) < 3:
            error_exit("Не указано название категории")

        cat_name = ''.join(sys.argv[2:]).lower()
        error_exit("Такая категория уже есть")

        data['categories'].append(cat_name)
        save_data(data)
        print('Категория добвалена')
    elif cmd == "add":
        if len(sys.argv) < 5:
            error_exit("Неверный формат Использование: add <сумма> <категория> <название>")

