import sys 
import os
import json
file_name ='expenses.json'

def load_data():
    if not os.path.exists(file_name):