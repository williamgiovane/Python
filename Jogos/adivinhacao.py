import random

print("\n*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

#Resposta
numero_secreto = random.randrange(1, 101)

#Tentativas
nivel = int(input("Qual o niv1el de dificuldade? \n(1) Facil (2) Medio (3)Dificil\n"))

if(nivel == 1):
    total_tentativas = 20
elif(nivel == 2):
    total_tentativas = 10
else:
    total_tentativas = 5

for rodada in range (1, total_tentativas + 1):
    print("\nTentativa: ", rodada, " de ", total_tentativas)

    #Pergunta para o usuario
    chute = int(input("Digite o seu número entre 1 e 100: "))
    print("Você digitou: ", chute)

    if((chute < 1) or (chute > 100)):
        print("\nVocê deve digitar um número entre 1 e 100")
        continue

    #Condições para o if
    acertou = chute == numero_secreto 
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    #Testas condições
    if (acertou):
        print("\nVocê acertou!")
        break
    elif (maior):
        print ("\nVocê errou, o seu chute foi maior que o numero secreto")
    elif (menor):
        print ("\nVocê errou, o seu chute foi menor que o numero secreto")

print("\nFim do jogo, o numero secreto era: ", numero_secreto)
