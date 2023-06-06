import json

def read(path):
    file = open(path)
    data = json.load(file)

    return data