from Pyro5.api import expose

# Marca a classe (ou método) que vai ser exposta em chamadas remotas
@expose

# Classe que define um objeto do tipo Question
class Question(object):
    def __init__(self, number, alternatives, answer):
        self.number = number
        self.alternatives = alternatives
        self.answer = answer