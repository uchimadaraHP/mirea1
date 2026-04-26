#сделать структуру с ипсользованием json +
#сделать лёгкий интерфейс +
#написать фнукции, для красоты +
#сделать всё модульно +

import sys
import os
import json

DATA_FILE = "expenses.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"categories": [], "expenses": []}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def error(msg):
    print(f"Ошибка: {msg}")


def find_cat(data, name):
    for c in data["categories"]:
        if c.lower() == name.lower():
            return c
    return None

def fmt(n):
    return int(n) if n == int(n) else n

def add_category(data, args):
    if not args: 
        print("Ошибка: укажите название")
        return
    name = " ".join(args).strip()
    if find_cat(data, name): 
        print("Ошибка: категория уже существует")
        return
    
    data["categories"].append(name)
    save_data(data)
    print(f"Категория '{name}' добавлена")

def add_expense(data, args):
    if len(args) < 3: 
        print("Ошибка: мало аргументов")
        return
    try:
        cost = float(args[0])
    except ValueError:
        print("Ошибка: цена должна быть числом")
        return

    cat_name, title = args[1], " ".join(args[2:])
    real_cat = find_cat(data, cat_name)
    
    if not real_cat: 
        print(f"Ошибка: категория '{cat_name}' не найдена")
        return

    data["expenses"].append({"cost": cost, "category": real_cat, "name": title})
    save_data(data)
    print(f"Добавлено: {fmt(cost)} | {real_cat} | {title}")

def list_expenses(data, args):
    expenses = data["expenses"]
    if args:
        cat = find_cat(data, " ".join(args))
        if not cat:
            print("Ошибка: категория не найдена")
            return
        expenses = [e for e in expenses if e["category"] == cat]

    if not expenses:
        print("0 трат")
        return

    for e in expenses:
        print(f"{fmt(e['cost'])} | {e['category']} | {e['name']}")

def total_expenses(data, args):
    expenses = data["expenses"]
    if args:
        cat = find_cat(data, " ".join(args))
        if not cat:
            print("Ошибка: категория не найдена")
            return
        expenses = [e for e in expenses if e["category"] == cat]

    if not expenses:
        print("0 трат")
        return

    print(fmt(sum(e["cost"] for e in expenses)))

def interactive_mode(data, commands):
    print("--- Интерактивный режим (введите 'exit' для выхода) ---")
    while True:
        try:
            user_input = input("» ").strip()
            if not user_input: continue
            
            parts = user_input.split()
            cmd = parts[0]
            args = parts[1:]

            if cmd in ["exit", "quit", "выход"]:
                print("Завершение работы.")
                break
            
            if cmd in commands:
                commands[cmd](data, args)
            else:
                print(f"Неизвестная команда: {cmd}")
        except EOFError:
            break

def main():
    data = load_data()
    commands = {
        "add": add_expense,
        "add-category": add_category,
        "list": list_expenses,
        "total": total_expenses
    }

    if len(sys.argv) < 2:
        interactive_mode(data, commands)
    else:
        cmd, args = sys.argv[1], sys.argv[2:]
        if cmd in commands:
            commands[cmd](data, args)
        else:
            print(f"Ошибка: неизвестная команда '{cmd}'")
            sys.exit(1)

if __name__ == "__main__":
    main()