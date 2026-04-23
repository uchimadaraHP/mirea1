#сделать структуру с ипсользованием json +
#сделать лёгкий интерфейс +
#написать фнукции, для красоты -
#сделать всё модульно -

import sys 
import os
import json
file_name ='expenses.json'

def load_data():
    if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
        with open(file_name, 'r', encoding='utf-8') as f:
             content = f.read()
        if content.strip():
            return json.loads(content)  
        else:
            return {'categories': [], 'expenses': []}
        else:
        return {'categories': [], 'expenses': []}
def save_data(data):
     with open(file_name, 'w', encoding='utf-8')as f:
            json.dump(data, f, ensure_ascii=False, indent=)