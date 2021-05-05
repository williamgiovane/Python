def jogar():
    print("\n*********************************")
    print("Bem vindo ao jogo de Forca!")
    print("*********************************")

    palavra_secreta = "Banana"
    enforcou = False
    acertou = False

    while((enforcou != True) and (acertou != True)):
        chute = input("Qual letra?\n").lower().strip()

        index = 0
        for letra in palavra_secreta:
            if(chute == letra.lower()):
                print("Encontrei a letra {} na posição {}".format(letra, index))
            
            index = index + 1
    
    print("\nFim do jogo!")

if(__name__ == "__main__"):
    jogar()