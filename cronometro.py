import time

def cronometro(minutos):
    segundos = minutos * 60
    while segundos > 0:
        time.sleep(1)
        segundos -= 1
    return True