import random

def jogar():
    print("\n*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)    

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].lower()

    letras_acertadas = ["_" for letra in palavra_secreta]

    print("\nA palavra contem {} letras".format(len(palavra_secreta)))

    enforcou = False
    acertou = False
    tentivas = 1

    while((enforcou != True) and (acertou != True)):
        chute = input("\nQual letra?\n").lower().strip()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra

                index += 1

            print("\nPalavra:", letras_acertadas)

            letras_restantes = int(letras_acertadas.count('_'))
            tentivas_restantes = len(palavra_secreta) - tentivas
            tentivas += 1

            if(letras_restantes == 0):
                print("\nParabéns você acertou a palavra!")
                acertou = True
            else:
                print("\nAinda faltam acertar {} letras e você tem {} tentativas".format(letras_restantes, tentivas_restantes))
        else:
            if(tentivas == len(palavra_secreta)):
                print("\nVocê não acertou a palavra!")
                enforcou = True
            else:
                letras_restantes = int(letras_acertadas.count('_'))
                tentivas_restantes = len(palavra_secreta) - tentivas
                tentivas += 1
                print("\nPalavra:", letras_acertadas)
                print("\nAinda faltam acertar {} letras e você tem {} tentativas".format(letras_restantes, tentivas_restantes))

    print("\nFim do jogo!")

if(__name__ == "__main__"):
    jogar()