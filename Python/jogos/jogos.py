import jogoDaForca
import adivinhacao

def escolhe_jogo():

    print("Bem vindo ao Menu de Jogos ;D")
    print("------Escolha um jogo!--------")
    print("(1) Jogo da forca (2) adivinhção")
    n = int(input("Digite uma opção > "))

    if( n == 1):
        print("Jogando o jogo da Forca")
        jogoDaForca.jogar();
    elif (n==2):
        print("Jogando adivinhação")
        adivinhacao.jogar()

if(__name__=="__main__"):
    escolhe_jogo()