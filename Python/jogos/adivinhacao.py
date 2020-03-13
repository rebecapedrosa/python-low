import random

def jogar():
    print("*************")
    print("Bem vindo ao jogo de Adivinhação")
    print("*************")
    #----------------------------------

    #função que define um intervalo preciso
    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000
    #a função input retorna uma string
    #------------------------------------

    print("Qual nível de dificuldade deseja?", end="\n")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Defina a opção: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5



    for rodada in range(1,total_de_tentativas+1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um numero de 1 a 100: ")
        chute = int(chute_str)
        print("Voce digitou : ", chute_str)
        
        if(chute<0 or chute>100):
            print("Voce deve digitar um valor no intervalo pedido!")
            continue

        #arrumando as variaveis de maneira semantica
        acertou = chute == numero_secreto
        maior = chute>numero_secreto
        menor = chute<numero_secreto
        #------------------------------------------

        if(acertou) :
            print("Ae arrombado do caralho, pega porra!!")
            print(" Fez {} pontos".format(pontos))
            break
        else:
            if(maior):
                print("Seu chute foi maior que o número secreto")
            elif(menor):
                print("Seu chute foi menor que o número secreto", end="\n")
                pontos_perdidos = abs(pontos - chute)
                pontos = pontos - pontos_perdidos


    print("O numero secreto era: ", numero_secreto)


    #FUNCOES built-in -> Funções embutidas no python 
    #----------------------------------------------
    #módulo do python -> precisa ser importado
        #[random] é um módulo
        #import random 
    #----------------------------------------------
    #funções de arredondamento [round]
        #numero_random = random.random() * 100
        #numero_random = 18.89003343
        #int(numero_random)
        #numero_random = 18
        #round(numero_random)
        #19
    #----------------------------------------------
    #seed - entrada para gerar números diferentes no
    #random
        #geralmente usa as horas

    #divisão com duas barras
        #->devolve inteiro(3//2)
#-------------------
#quando o arquivo é importado = name vazio
#quando o arquivo é executado = name = main
if(__name__ == "__main__"):
        jogar()