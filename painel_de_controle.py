from random import randint

#informacões que vão vim do eletroneuromiografo
gravidade = randint(5, 15)
velocidade_do_salto = randint(20, 50)
altura_maxima = randint(500, 550)

def painel_de_controle(gravidade, velocidade_do_salto, altura_maxima):
    #Variaveis fixas (definidas no inicio)
    velocidade_game = 10
    tempo_game = 10

    return gravidade, velocidade_do_salto, altura_maxima

