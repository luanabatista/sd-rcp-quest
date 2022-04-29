from Pyro5.api import expose, behavior
from question import Question
import Pyro5.api

# Marca a classe (ou método) que vai ser exposta em chamadas remotas
@expose
# Especifica o comportamento do server
# Uma única instância será criada e usada para para todas as chamadas de método ("single")
@behavior(instance_mode="single")


class QuizServer(object):

    # Define o gabarito das questões
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

            # Tranforma a entrada do usuário em um array e atribui os valores do array as variaveis
            message = message.split(";")
            number = int(message[0]) 
            alternatives = int(message[1])
            answer = message[2]

            # Para cada questão do gabarito, compara se o número da questão inserida corresponde a alguma questão
            for question in self.answers:
                counter = 0
                sucesses = 0
                errors = 0    
                if question.number == number:
                    # Caso a questão tenha sido encontrada
                    for alternative in question.answer:
                        # Compara a resposta com o gabarito
                        if alternative == answer[counter]: # Se for correta incrementa a variável sucesses
                            sucesses += 1

                        # Se for incorreta incrementa a variável errors
                        else:
                            errors += 1
                        counter += 1      
                    return f'\nQuestão: {number}; Acertos: {sucesses}; Erros:{errors}'
                    
        except:
            return f"Erro ao processar requisição {message}"

# Programa principal
# Cria um daemon
daemon = Pyro5.server.Daemon()

#Encontra o Name Server
''' 
Name Server é uma ferramenta para ajudar a manter o controle dos obejtos na rede.
Ela da nomes lógicos aos objetos ao invés de ter que saber sempre o nome e localização exatas
'''
ns = Pyro5.api.locate_ns()

# Registra o QuizServer como um objeto pyro
uri = daemon.register(QuizServer)

# Registra o objeto no Name Server
ns.register("quizserver", uri)

print("Ready.")
daemon.requestLoop()   
