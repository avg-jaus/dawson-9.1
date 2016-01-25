# Игры
# Демонстрирует создание модуля

class Player(object):
    """ Участник игры. """
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score

    def __str__(self):
        rep = self.name + ":\t" + str(self.score)
        return rep

def ask_yes_no(question):
    """ Задает вопрос с ответом 'д' или 'н'. """
    response = None
    while response not in ("д", "н"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    """ Просит ввести число из заданного диапазона. """
    response = None
    while response not in range(low, high+1):
        response = int(input(question))
    return response

  
if __name__ == "__main__":
    print("Bы запустили этот модуль напрямую. а не импортировали его.")
    input("\n\nНажмите Enter... для выхода.")


