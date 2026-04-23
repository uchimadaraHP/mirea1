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