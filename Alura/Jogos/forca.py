def jogar():
    print("\n*********************************")
    print("Bem vindo ao jogo de Forca!")
    print("*********************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    while((enforcou != True) and (acertou != True)):
        chute = input("Qual letra?\n")

        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                print("Encontrei a letra {} na posição {}".format(letra, index))
            
            index = index + 1
    
    print("\nFim do jogo!")

if(__name__ == "__main__"):
    jogar()