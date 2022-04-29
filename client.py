from Pyro5.api import Proxy

# Cria proxy
# Proxy do pyro para objetos remotos
# Intercepts method calls and dispatches them to the remote object.
# Intercepta chamadas de metodos e as envia para o objeto remoto
quizserver = Proxy("PYRONAME:quizserver")

# Cria um loop que fica recebendo valores do usuário
while True:

    # Cria menu que apresenta as ações que o usuário pode executar
    menu = int(input("\nMENU\n1) Corrigir questão\n2) Finalizar\n\nSelecione uma opção: "))
    
    # Recebe a resposta do usuário e retorna corrigida
    if menu == 1:
        answer = input("Insira sua resposta: ")
        print(quizserver.correctQuestion(answer)) 
    
    # Finaliza o programa
    elif menu == 2:
        exit(0)

    # Número que não são 1 ou 2 finalizando o programa
    else:
        exit(0)