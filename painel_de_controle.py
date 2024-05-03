from random import randint
import serial

arduino = serial.Serial('COM6', 9600)
while True:
    linha = str(arduino.readline())
    print(linha[2:-5])
arduino.close()
 
#informacões que vão vim do eletroneuromiografo
gravidade = randint(5, 15)
velocidade_do_salto = randint(20, 50)
altura_maxima = randint(500, 550)
pular = True
#possiveis esparmos 

def painel_de_controle(gravidade, velocidade_do_salto, altura_maxima, pular):
    #Variaveis fixas (definidas no inicio)
    velocidade_game = 10
    tempo_game = 10

    return gravidade, velocidade_do_salto, altura_maxima, pular

