from random import randint
import serial

arduino = serial.Serial('COM6', 9600)

while True:
    linha = arduino.readline().decode().strip()
    valor = int(linha) 
    pulo = False
    
    if valor > 200:  
        print(valor)
        pulo = True


arduino.close()



#informacões que vão vim do eletroneuromiografo
gravidade = randint(5, 15)
velocidade_do_salto = randint(20, 50)
altura_maxima = randint(500, 550)
#possiveis esparmos 

def painel_de_controle():

    print(gravidade,velocidade_do_salto, altura_maxima)

painel_de_controle()

teste = 123
print(teste)
