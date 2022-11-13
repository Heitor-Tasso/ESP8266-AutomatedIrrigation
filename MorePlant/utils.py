import os
import json

def correct_path(path_filename:str):
    bar_init = '/' if path_filename.startswith('/') else ''
    new_str = []
    for x in path_filename.split('\\'):
        new_str.extend(x.split(r'/'))
    path = [x + '/' for x in new_str[0:-1] if x != '']
    return ''.join([bar_init] + path + [new_str[-1]])

sys_path = correct_path(os.path.split(__file__)[0])

def get_path(local):
    return f'{sys_path}/{local}'

def icon(name, ext='png'):
    return get_path(f'assets/icons/{name}.{ext}')

def image(name, ext='png'):
    return get_path(f'assets/images/{name}.{ext}')

def get_json(name, *args):
    with open(get_path(name), 'r', encoding='utf-8') as file:
        return json.load(file)

def update_json(new_json, name):
    with open(get_path(name), 'w', encoding='utf-8') as file:
        file.write(json.dumps(new_json, indent=4))

