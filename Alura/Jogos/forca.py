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

        print(letras_acertadas)
    
    print("\nFim do jogo!")

if(__name__ == "__main__"):
    jogar()