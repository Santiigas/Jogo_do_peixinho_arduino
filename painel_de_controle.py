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


