#сделать структуру с ипсользованием json +
#сделать лёгкий интерфейс +
#написать фнукции, для красоты +
#сделать всё модульно +

import sys
import os
import json

data_file = "expenses.json"

def load_data():
    if not os.path.exists(data_file):
        return {"categories": [], "expenses": []}
    with open(data_file, "r", encoding="utf-8") as f:
           return json.load(f)

def save_data(data):
    with open(data_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def error_exit(message):
    print(f"Ошибка: {message}")
    sys.exit(1)

def find_category(data, name):
    for cat in data["categories"]:
        if cat.lower() == name.lower():
            return cat
    return None

def format_cost(n):
    return int(n) if n == int(n) else n

def cmd_add_category(data, args):
    if not args:
        error_exit("Укажите название категории")

    cat = " ".join(args).strip()

    if cat == "":
        error_exit("Название не может быть пустым")

    if find_category(data, cat) is not None:
        error_exit("Категория уже существует")

    data["categories"].append(cat)
    save_data(data)
    print(f"Категория '{cat}' добавлена")

def cmd_add(data, args):
    if len(args) < 3:
        error_exit("Укажите стоимость, категорию и название")

    try:
        cost = float(args[0])
    except ValueError:
       error_exit("Стоимсоть должна быть числом")

    cat_input = args[1].strip()
    expense_name = " ".join(args[2:]).strip()

    if not expense_name:
        error_exit("Название расхода не может быть пустым")

    found = find_category(data, cat_input)
    if found is None:
        error_exit(f"Категория '{cat_input}' не найдена, сначала добавьте её через add-category")

    data["expenses"].append({
        "cost": cost,
        "category": found,
        "name": expense_name
    })
    save_data(data)
    print(f"Расход добавлен: {format_cost(cost)} | {found} | {expense_name}")

def cmd_list(data, args):
    if len(args) >= 1:
        cat_input = " ".join(args)
        found = find_category(data, cat_input)
        if found is None:
            error_exit(f"Категория '{cat_input}' не найдена")
        expenses = [e for e in data["expenses"] if e["category"] == found]
    else:
        expenses = data["expenses"]

    if len(expenses) == 0:
        print("0 трат")
        return

    for e in expenses:
        print(f"{format_cost(e['cost'])} | {e['category']} | {e['name']}")

def cmd_total(data, args):
    if len(args) >= 1:
        cat_input = " ".join(args)
        found = find_category(data, cat_input)
        if found is None:
            error_exit(f"категория '{cat_input}' не найдена")
        expenses = [e for e in data["expenses"] if e["category"] == found]
    else:
        expenses = data["expenses"]

    if len(expenses) == 0:
        print("0 трат")
        return

    print(format_cost(sum(e["cost"]for e in expenses)))

def main():
    if len(sys.argv) < 2:
        error_exit("Укажите команду (add, add-category, list, total)")

    command = sys.argv[1]
    args = sys.argv[2:]

    data = load_data()

    if command == "add-category":
        cmd_add_category(data, args)
    elif command == "add":
        cmd_add(data, args)
    elif command == "list":
        cmd_list(data, args)
    elif command == "total":
        cmd_total(data, args)
    else:
        error_exit(f"Неизвестная команда '{command}'. Доступны: add, add-category, list, total")

if __name__ == "__main__":
    main()