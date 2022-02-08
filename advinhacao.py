import os
import time
import random


def jogar():

    numero_secreto = random.randint(0, 10)
    acertou = False
    tentativa = 1
    tentativas_dificuldade = " "
    pontos = 1000

    os.system('cls')  # Limpa o terminal.
    print("\n\n\tBem vindo ao jogo de advinhação!")
    print("\n      Neste jogo, você tem algumas chances\n\tpara advinhar o numero correto."
          "\n\tEsse numero está entre 0 a 10.")
    input("\n\tAperte enter para continuar...")
    os.system('cls')

    while isinstance(tentativas_dificuldade, str):
        # Verifica se a variável tentativas_dificuldade é uma instância tipo string, se for, entra no looping.

        print("\n\n\n\tA dificuldade do jogo é relacionada\n      a quantidade de tentativas disponíveis"
              "\n\t  para acertar o número correto.\n\n\tDigite fácil para 6 tentativas.\n\t"
              "Digite normal para 4 tentativas.\n\tDigite difícil para 2 tentativas.")
        tentativas_dificuldade = input("\n\tDigite a dificuldade desejada: ")

        if tentativas_dificuldade.lower() == "fácil" or tentativas_dificuldade.lower() == "facil":
            tentativas_dificuldade = 6
        elif tentativas_dificuldade.lower() == "normal":
            tentativas_dificuldade = 4
        elif tentativas_dificuldade.lower() == "difícil" or tentativas_dificuldade.lower() == "dificil":
            tentativas_dificuldade = 2
        else:
            print("\n\t  Por favor, siga as intruções\n      e digite corretamente a dificuldade.")
            time.sleep(3)

        os.system('cls')

    while tentativa <= tentativas_dificuldade:

        try:
            chute = int(input("\n\n\n\n\tTentativa numero {} de {}\n"
                              "     Digite um numero entre 0 a 10: ".format(tentativa, tentativas_dificuldade)))
            # Formata a string, alterando a quantidade de tentativas e mostrando a quantidade máxima de chutes.

        except ValueError:
            print("\n\n\n  Por favor, siga as intruções corretamente!")
            time.sleep(3)
            os.system('cls')
            continue

        if chute not in range(0, 11):
            print("\n\t Por favor, digite um numero\n\tmaior que zero e menor que 10")
            time.sleep(3)
            os.system('cls')
            continue

        elif chute is not numero_secreto:
            pontos -= (abs(numero_secreto - chute) * 25)

            if chute > numero_secreto:
                print("\n\n\tEsse não é o numero correto!\n\n      O seu chute foi acima do número.\n")
            else:
                print("\n\n\tEsse não é o numero correto!\n\n      O seu chute foi abaixo do número.\n")

        else:
            os.system('cls')
            print("\n\n\n      Parabéns, você acertou o numero!")
            acertou = True
            break

        input("\n       Aperte enter para continuar...")
        tentativa += 1
        os.system('cls')

    if not acertou:
        print("\n\n\n\n\n\tVocê não acertou o numero!")

    print("\n\n\tPontuação final: {} pontos.\n\t      Fim do jogo!".format(pontos))
    time.sleep(5)  # Faz o terminal esperar 5 segundos.
    os.system('cls')
