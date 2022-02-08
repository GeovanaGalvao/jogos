import os
import time
import advinhacao
import forca


def temporizador_de_tres_segundos():
    time.sleep(3)  # Faz o terminal esperar 5 segundos.
    os.system('cls')


def selecao_do_jogo():
    print("\n       Você pode escolher entre uma dessas opções:"
          "\n\n\t\t1.Jogo de advinhação\n\t\t2.Jogo da forca\n\t\t3.Sair")
    return executa_opcao_escolhida(input("\n\tPor favor escolha uma das opções acima:").strip())
    # Verifica a opção escolhida pelo usuário e passa essa informação para a execução da decisão.


def executa_opcao_escolhida(escolha):
    if escolha == "1":
        return advinhacao.jogar()
    elif escolha == "2":
        return forca.jogar()
    elif escolha == "3":
        return escolha
    else:
        print("\n\tPor favor digite a opção corretamente.\n")
        temporizador_de_tres_segundos()


def mensagem_do_final_do_programa():
    print("\n\t\tObrigada por jogar!\n")
    temporizador_de_tres_segundos()


def menu_principal():
    os.system('cls')  # Limpa o terminal.
    print("\n\t\tBem vindo a lista de jogos!\n")
    escolha = selecao_do_jogo()
    while escolha != "3":
        escolha = selecao_do_jogo()
    mensagem_do_final_do_programa()


if __name__ == "__main__":
    # Se o arquivo for executado diretamente, ele inicia normalmente o jogo.
    menu_principal()
