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
            with open(file_name, 'r') as f:
                    return json.load(f)
        except Exception:
             return {'categories': [], 'expenses': []}