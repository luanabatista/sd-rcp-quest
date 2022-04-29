from Pyro5.api import expose, behavior
from question import Question
import Pyro5.api

@expose
@behavior(instance_mode="single")
class QuizServer(object):

    def __init__(self):
        self.requests = []
        self.answers = [
            Question(1, 4, 'VVVF'),
            Question(2, 4, 'VFVF'),
            Question(3, 4, 'FFVV'),
            Question(4, 4, 'VFVV')
        ]

    def correctQuestion(self, message):
        
        try:
            message = message.split(";")
            number = int(message[0]) 
            alternatives = int(message[1])
            answer = message[2]

            for question in self.answers:
                counter = 0
                sucesses = 0
                errors = 0    
                if question.number == number:
                    for alternative in question.answer:
                        # Compara a resposta com o gabarito
                        if alternative == answer[counter]: # Se for correta incrementa a variável sucesses
                            sucesses += 1

                        else: # Se for incorreta incrementa a variável errors
                            errors += 1
                        counter += 1      
                    return f'\nQuestão: {number}; Acertos: {sucesses}; Erros:{errors}'
                    
        except:
            return f"Erro ao processar requisição {message}"

# main program
daemon = Pyro5.server.Daemon()         # make a Pyro daemon
ns = Pyro5.api.locate_ns()             # find the name server
uri = daemon.register(QuizServer)   # register the CounterServer as a Pyro object
ns.register("quizserver", uri)      # register the object with a name in the name server

print("Ready.")
daemon.requestLoop()   