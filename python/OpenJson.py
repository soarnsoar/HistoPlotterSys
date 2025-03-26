import json
def OpenJson(_path):
    print(_path)
    ret= {}
    with open(_path, "r") as json_file:
        ret= json.load(json_file)
    return ret
