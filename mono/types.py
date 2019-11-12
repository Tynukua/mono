def snakeize_s(string):
    answer = ''
    for char in str(string):
        if char.isupper():
            answer += f'_{char.lower()}'
        else:
            answer += char
    return answer

def snakeize_dict(dict_):
    answer = {}
    for key in dict_:
        nkey = snakeize_s(key)
        answer[nkey] = dict_[key]
    return answer

class MonoCard:
    def __init__(self, json):
        self.__dict__ = snakeize_dict( json)
    
    def as_dict(self):
        return self.__dict__.copy()

class ClientInfo:
    def __init__(self, json):
        self.__dict__ = snakeize_dict( json)
    
    def as_dict(self):
        dict_ = self.__dict__.copy()
        for key in dict_:
            try:
                dict_[key] = dict_[key].as_json()
            except Exception:
                pass

class StatementItem:
    def __init__(self, json):
        self.__dict__ = snakeize_dict( json)

    def as_dict(self):
        return self.__dict__.copy()