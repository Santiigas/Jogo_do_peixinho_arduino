from painel_de_controle import painel_de_controle
from random import randint


def evento_botao_espaco():

    gravidade, velocidade_do_salto, altura_maxima = painel_de_controle()

    print("Valores atualizados:")
    print("Gravidade:", gravidade)
    print("Velocidade do Salto:", velocidade_do_salto)
    print("Altura Maxima:", altura_maxima)

evento_botao_espaco()

#teste2