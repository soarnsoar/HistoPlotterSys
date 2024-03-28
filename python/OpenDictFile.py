def OpenDictFile(_path):
    ret={}
    try:
    
        with open(_path, "r") as _file:
            file_content = _file.read()
            exec(file_content, {}, ret)
            return ret
    except IOError:
        print("Error: Unable to open file or file does not exist.")
    except SyntaxError:
        print("Error: Invalid syntax in file.")


