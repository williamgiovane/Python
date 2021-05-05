def jogar():
    print("\n*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "Banana".lower()
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    print("\nA palavra contem {} letras".format(len(letras_acertadas)))

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

            if(letras_restantes == 0):
                print("Parabéns você acertou a palavra!")
                acertou = True
            else:
                print("\nAinda faltam acertar {} letras".format(letras_restantes))
        else:
            if(tentivas == 6):
                enforcou = True
            else:
                tentivas += 1

    print("\nFim do jogo!")

if(__name__ == "__main__"):
    jogar()