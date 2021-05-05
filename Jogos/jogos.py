import adivinhacao
import forca

print("\n*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************")

jogo = int(input("Qual jogo você quer jogar? \n(1) Forca (2) Adivinhação\n"))

if(jogo == 1):
    forca.jogar()
elif(jogo == 2):
    adivinhacao.jogar()