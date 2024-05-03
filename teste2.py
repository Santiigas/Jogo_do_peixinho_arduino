import serial

arduino = serial.Serial('COM3', 9600)
while True:
    linha = str(arduino.readline())
    print(linha[2:-5])
arduino.close()
