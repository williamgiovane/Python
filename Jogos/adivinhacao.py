print("\n*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute = int(input("\nDigite o seu número: "))
print("\nVocê digitou: ", chute)

if (numero_secreto == chute):
    print("\nVocê acertou!")
else:
    print("\nVocê errou!")

print("\nFim do jogo")