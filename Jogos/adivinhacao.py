print("\n*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

#Resposta
numero_secreto = 42
total_tentativas = 1
chute = 0

while ((chute != numero_secreto) and (total_tentativas <= 3)):
    print("\nTentativa: ", total_tentativas, " de 3")

    #Pergunta para o usuario
    chute = int(input("Digite o seu número: "))
    print("Você digitou: ", chute)

    #Condições para o if
    acertou = chute == numero_secreto 
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    #Testas condições
    if (acertou):
        print("\nVocê acertou!")
    else:
        if (maior):
            print ("\nVocê errou, o seu chute foi maior que o numero secreto")
        elif (menor):
            print ("\nVocê errou, o seu chute foi menor que o numero secreto")

    total_tentativas = total_tentativas + 1

print("\nFim do jogo")