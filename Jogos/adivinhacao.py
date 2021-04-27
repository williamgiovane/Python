print("\n*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute = int(input("\nDigite o seu número: "))
print("\nVocê digitou: ", chute)

#Condições para o if
acertou = chute == numero_secreto 
maior = chute > numero_secreto
menor = chute < numero_secreto

if (acertou):
    print("\nVocê acertou!")
else:
    if (maior):
        print ("\nVocê errou, o seu chute foi maior que o numero secreto")
    elif (menor):
        print ("\nVocê errou, o seu chute foi menor que o numero secreto")

print("\nFim do jogo")