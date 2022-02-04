import os
import time
import random


def jogar():

    introducao()
    palavra_secreta = gera_palavra_secreta()
    advinhando_palavra = ["_" for letra in palavra_secreta]  # Inicializa a lista "oculta" do tamanho da palavra secreta
    letras_usadas = []
    erros = 0
    acertou = False

    while erros in range(0, 7) and not acertou:

        os.system('cls')
        imprime_informacoes_da_partida(advinhando_palavra, letras_usadas, erros)
        chute = obtem_chute_usuario()

        if not valida_letra_do_usuario(chute):
            print("\n\n\t  Por favor siga as instruções\n\te digite apenas uma letra válida.")
            time.sleep(4)
            continue

        if letra_ja_utilizada(chute, letras_usadas):
            print("\n\tPor favor não utilize a mesma\t\n  mais de uma vez!")
            time.sleep(4)
            continue

        letras_usadas.append(chute)
        if not verifica_chute_em_palavra_secreta(chute, palavra_secreta):
            erros += 1
            desenha_forca(erros)
            print("\n\tVocê errou o seu chute!")
            time.sleep(3)
            continue

        preenche_advinhando_palavra(advinhando_palavra, palavra_secreta, chute)
        acertou = "_" not in advinhando_palavra
        # Se o _ não for encontrado no status palavra, isso significa
        # que a palavra foi advinhada! Então acertou se torna true.

    os.system('cls')
    imprime_resultado_final(acertou, palavra_secreta, erros)
    time.sleep(8)
    os.system('cls')


def introducao():
    os.system('cls')
    print("\n\n\t   Bem vindo ao jogo da forca!\n")
    desenha_forca()
    time.sleep(3)
    os.system('cls')
    print("\n\n\n\tNeste jogo , você tem que advinhar\n\t a palavra secreta. Deve-se"
          " tomar\n\t  cuidado pois se errar muitas\n\t letras você irá perder o jogo.")
    input("\n\tAperte enter para continuar...")
    os.system('cls')


def imprime_informacoes_da_partida(advinhando_palavra, letras_usadas, erros):
    print("\n\tO estado atual da palavra é\n\t{}".format(advinhando_palavra))

    if len(letras_usadas) > 0:
        print("\n\tAs letras chutadas foram\n\t{}".format(letras_usadas, sep=", "))
        print("\tVocê errou {} chutes!".format(erros))


def desenha_forca(erros=0):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 0:
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    elif erros == 2:
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")

    elif erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    elif erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    elif erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    elif erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    elif erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")


def imprime_mensagem_vencedor(palavra_secreta):
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
    print("\nParabens! Você acertou a palavra {}!".format(palavra_secreta))


def imprime_mensagem_perdedor(palavra_secreta):
    time.sleep(2)
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
    time.sleep(2)
    print("\n\tInfelizmente você não conseguiu\n\tacertar a palavra correta!\n\tA palavra era {}."
          .format(palavra_secreta))


def imprime_resultado_final(acertou, palavra_secreta, erros):
    if acertou:
        imprime_mensagem_vencedor(palavra_secreta)

    else:
        imprime_mensagem_perdedor(palavra_secreta)

    time.sleep(5)
    if erros in range(0):
        print("\n\tVocê não errou nem uma letra!\n\t      Fim do jogo!")
    elif erros in range(1):
        print("\n\t   Você errou 1 letra!\n\t      Fim do jogo!")
    else:
        print("\n\t   Você errou {} letras!\n\t      Fim do jogo!".format(erros))
    time.sleep(3)


def obtem_chute_usuario():
    return input("\n\n\tDigite uma letra: ").lower().strip()


def gera_palavra_secreta(nome_arquivo="palavras_do_jogo_da_forca.txt"):
    # Quando o arquivo não é especificado, ele inicia com o bloco de texto palavras.txt
    palavras = []

    with open("{}".format(nome_arquivo)) as arquivo:
        for linha in arquivo:
            palavras.append(linha.lower().strip())  # O strip também remove o \n no final da palavra.
            # Cada indice dentro da lista é uma palavra dentro do arquivo de texto.

        return palavras[random.randrange(0, len(palavras))]
        # Escolhe um número aleatóriamente com base na quantidade de linhas do arquivo de texto. Cada
        # linha corresponde a uma palavra específica encontrada no arquivo, gerando assim a palavra secreta.


def preenche_advinhando_palavra(advinhando_palavra, palavra_secreta, chute):
    index = 0

    for letra in palavra_secreta:
        if chute == letra:
            advinhando_palavra[index] = letra  # Eu estou substituindo o espaço vazio pela letra
            # que o usuario chutou caso ela pertença a palavra. Para isso, eu obtenho o index
            # atual em que o for se encontra, e substituo o espaço vazio pela letra advinhada.

        index += 1


def letra_ja_utilizada(chute, advinhando_palavra):
    if chute in advinhando_palavra:
        return True


def valida_letra_do_usuario(chute):
    if len(chute) == 1 and chute.isalpha():  # Validando se o que o usuario digitou é apenas uma letra do alfabeto.
        return True


def verifica_chute_em_palavra_secreta(chute, palavra_secreta):
    if chute in palavra_secreta:
        print("\n\tVocê acertou a letra {}".format(chute))
        time.sleep(3)
        return True


if __name__ == "__main__":
    # Se o arquivo for executado diretamente, ele inicia normalmente o jogo.
    jogar()
