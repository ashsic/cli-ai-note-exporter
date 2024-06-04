import json
import os

def get_file_path():
    return os.getcwd() + '/CLAInotes.json'

def read_json_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return []

def write_json_file(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def append_to_json_file(file_path, new_data):
    data = read_json_file(file_path)
    data.append(new_data)
    write_json_file(file_path, data)
