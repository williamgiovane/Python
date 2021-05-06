import random

def jogar():
    abertura_jogo()

    palavra_secreta = carrega_palavra()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

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

def abertura_jogo():
    print("\n*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carrega_palavra():
    arquivo = open("palavras.txt", "r")
    palavras = []

    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)   

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].lower()

    return palavra_secreta

def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]

if(__name__ == "__main__"):
    jogar()