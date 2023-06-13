import json

def write(path, content):
    with open(path, 'w') as f:
        json.dump(content, f)