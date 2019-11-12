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
        answer[key] = dict_[key]
    return answer

class MonoCard:
    def __init__(self, json):
        self.__dict__ = snakeize_dict( json)

class ClientInfo:
    def __init__(self, json):
        self.__dict__ = snakeize_dict( json)

class StatementItem:
    def __init__(self, json):
        self.__dict__ = snakeize_dict( json)