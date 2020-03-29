import random 


def imprimeMensagem():
    print("************")
    print("Jogo da Forca")
    print("*************")
#---------------------------------------------
def carregaPalavraSecreta():
    arquivo = open("palavras.txt","r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta
#----------------------------------------------

def inicializaLetras(palavra):
        return ["_" for letra in palavra]

#-----------------------------------------------
def pedeChute():
        chute = input("Qual a letra -> ")
        #funcao strip -> retorna string sem espaços em branco
        chute = chute.strip().upper()

        return chute


#----------------------------------------------
def desenhandoAForca(erros):
    print("  _______     ")
    print(" |/      |    ")
    if(erros==1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
    if(erros==2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ") 
    if(erros==3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")
    if(erros==4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")
    if(erros==5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")
    if(erros==6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")
    if(erros==7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")
    print(" |            ")
    print("_|___         ")
    print()


#----------------------------------------------

def imprimeVencedor():
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
def imprimePerdedor(palavra_secreta):
        print("Puxa, você foi enforcado!")
        print("A palavra era {}".format(palavra_secreta))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")




#-----------------------------------------------
def marcaChute(chute, letras_acertadas, palavra_secreta):
        posicao = 0
        for letra in palavra_secreta:
        #funcao upper -> retorna tudo em maiusculo
            if(chute.upper() == letra.upper()):
                letras_acertadas[posicao] = chute
            posicao = posicao + 1

#--------------------------------------------

def jogar():
    imprimeMensagem()
    palavra_secreta = carregaPalavraSecreta()
    acertou = False
    enforcou = False
    erros = 0
    #-->compressao de lista:
        #um laço na lista
    letras_acertadas = inicializaLetras(palavra_secreta)
    letras_faltando = str(letras_acertadas.count("_"))
    print(letras_acertadas)
    while(not acertou and not enforcou):
        chute = pedeChute()
        #--------------------------------
        #Iterando um laço para encontrar
        #letras semelhantes
        if(chute in palavra_secreta):
            marcaChute(chute,letras_acertadas,palavra_secreta)
        else:
            erros = erros + 1
            print("Voce tem {} erros".format(str(erros)))
            desenhandoAForca(erros)

            
        enforcou = erros == 7
        acertou = "_" not in letras_acertadas

        
        print(letras_acertadas)
        print("Faltam {} letras".format(letras_faltando))
                    

                

        print("Jogando...........")
       

    if(acertou):
     imprimeVencedor()
    else:
     imprimePerdedor(palavra_secreta)

print("Fim de jogo ;D")









if(__name__ == "__main__"):
    jogar()


#funcao capitalize - > retorna a string com a 
# primeira letra em maisculo e o restante minusculo
#--------------------------------------------------
#funcao lower - > retorna tudo em minusculo
#funcao upperr -> retorna tudo em maiusculo
#funcao strip -> retorna string sem espaços em branco
#str -> impossivel alterar
#funcao para encontrar a posicao
#de uma letra numa string
#....find() -> retorna a posição,
#uma unica vez