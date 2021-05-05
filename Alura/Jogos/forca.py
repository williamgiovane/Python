def jogar():
    print("\n*********************************")
    print("Bem vindo ao jogo de Forca!")
    print("*********************************")

    palavra_secreta = "Banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    print("\nA palavra contem {} letras".format(len(letras_acertadas)))

    enforcou = False
    acertou = False

    while((enforcou != True) and (acertou != True)):
        chute = input("\nQual letra?\n").lower().strip()

        index = 0
        for letra in palavra_secreta:
            if(chute == letra.lower()):
                letras_acertadas[index] = letra

            index = index + 1

        print("\nPalavra:", letras_acertadas)

        letras_restantes = int(letras_acertadas.count('_'))

        if(letras_restantes != 0):
            print("\nAinda faltam acertar {} letras".format(letras_restantes))
        else:
            print("Parabéns você acertou a palavra!")
            acertou = True

    print("\nFim do jogo!")

if(__name__ == "__main__"):
    jogar()