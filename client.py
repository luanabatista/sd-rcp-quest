from Pyro5.api import Proxy

quizserver = Proxy("PYRONAME:quizserver")

while True:
    menu = int(input("\nMENU\n1) Corrigir questão\n2) Finalizar\n\nSelecione uma opção: "))
    if menu == 1:
        answer = input("Insira sua resposta: ")
        print(quizserver.correctQuestion(answer)) 
    
    elif menu == 2:
        exit(0)

    else:
        exit(0)