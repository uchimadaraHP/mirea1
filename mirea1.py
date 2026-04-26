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

def error_exit(message, is_interactive=False):
    print(f"Ошибка: {message}")
    if not is_interactive:
        sys.exit(1)

def find_category(data, name):
    for cat in data["categories"]:
        if cat.lower() == name.lower():
            return cat
    return None

def format_cost(n):
    return int(n) if n == int(n) else n

def cmd_add_category(data, args, is_interactive=False):
    if not args:
        return error_exit("Укажите название категории", is_interactive)
    cat = " ".join(args).strip()
    if cat == "":
        return error_exit("Название не может быть пустым", is_interactive)
    if find_category(data, cat) is not None:
        return error_exit("Категория уже существует", is_interactive)

    data["categories"].append(cat)
    save_data(data)
    print(f"Категория '{cat}' добавлена")

def cmd_add(data, args, is_interactive=False):
    if len(args) < 3:
        return error_exit("Укажите стоимость, категорию и название", is_interactive)
    try:
        cost = float(args[0])
    except ValueError:
       return error_exit("Стоимость должна быть числом", is_interactive)

    cat_input = args[1].strip()
    expense_name = " ".join(args[2:]).strip()
    if not expense_name:
        return error_exit("Название расхода не может быть пустым", is_interactive)

    found = find_category(data, cat_input)
    if found is None:
        return error_exit(f"Категория '{cat_input}' не найдена", is_interactive)

    data["expenses"].append({"cost": cost, "category": found, "name": expense_name})
    save_data(data)
    print(f"Расход добавлен: {format_cost(cost)} | {found} | {expense_name}")

def cmd_list(data, args, is_interactive=False):
    expenses = data["expenses"]
    if len(args) >= 1:
        cat_input = " ".join(args)
        found = find_category(data, cat_input)
        if found is None:
            return error_exit(f"Категория '{cat_input}' не найдена", is_interactive)
        expenses = [e for e in expenses if e["category"] == found]

    if not expenses:
        print("0 трат")
    else:
        for e in expenses:
            print(f"{format_cost(e['cost'])} | {e['category']} | {e['name']}")

def cmd_total(data, args, is_interactive=False):
    expenses = data["expenses"]
    if len(args) >= 1:
        cat_input = " ".join(args)
        found = find_category(data, cat_input)
        if found is None:
            return error_exit(f"Категория '{cat_input}' не найдена", is_interactive)
        expenses = [e for e in expenses if e["category"] == found]

    if not expenses:
        print("0 трат")
    else:
        print(format_cost(sum(e["cost"] for e in expenses)))

def run_interactive(data):
    print("--- Интерактивный режим (введите 'exit' для выхода) ---")
    commands = {
        "add": cmd_add,
        "add-category": cmd_add_category,
        "list": cmd_list,
        "total": cmd_total
    }
    
    while True:
        try:
            line = input("» ").strip()
            if not line: continue
            if line.lower() in ["exit", "quit", "выход"]: break
            
            parts = line.split()
            cmd, args = parts[0], parts[1:]
            
            if cmd in commands:
                commands[cmd](data, args, is_interactive=True)
            else:
                print(f"Неизвестная команда '{cmd}'")
        except EOFError:
            break

def main():
    data = load_data()
    
   
    if len(sys.argv) < 2:
        run_interactive(data)
        return

    command = sys.argv[1]
    args = sys.argv[2:]

    if command == "add-category":
        cmd_add_category(data, args)
    elif command == "add":
        cmd_add(data, args)
    elif command == "list":
        cmd_list(data, args)
    elif command == "total":
        cmd_total(data, args)
    else:
        error_exit(f"Неизвестная команда '{command}'")

if __name__ == "__main__":
    main()