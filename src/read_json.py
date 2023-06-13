import json

def read(path):
    """
    :param path: json path to write to
    :return: json data in the form of a list or dict
    """

    file = open(path)
    data = json.load(file)

    return data