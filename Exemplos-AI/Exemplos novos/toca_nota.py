from machine import Pin, PWM
from utime import sleep

def tocar_nota(pino, frequencia, duracao):
    """
    Faz o buzzer tocar uma nota.

    Parâmetros:
    pino (int): GPIO do buzzer.
    frequencia (int): Frequência da nota (Hz).
    duracao (float): Duração da nota (segundos).
    """
    buzzer = PWM(Pin(pino))
    buzzer.freq(frequencia)
    buzzer.duty_u16(1000)  # Define a intensidade
    sleep(duracao)
    buzzer.deinit()

# Uso:
tocar_nota(21, 440, 0.5)  # Toca a nota Lá (440 Hz) por 0.5 segundos
