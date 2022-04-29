from Pyro5.api import expose

@expose
class Question(object):
    def __init__(self, number, alternatives, answer):
        self.number = number
        self.alternatives = alternatives
        self.answer = answer