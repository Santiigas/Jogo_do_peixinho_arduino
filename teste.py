import serial

arduino = serial.Serial('COM4', 9600)

while True:
    linha = arduino.readline().decode().strip()
    valor_altura_maxima = int(linha) 
    esta_pulando = False
    
    if valor_altura_maxima >= 200:  
        print(valor_altura_maxima )
