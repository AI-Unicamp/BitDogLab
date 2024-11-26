# Pisca LED central na cor azul a cada 1 segundo
from machine import Pin
import utime

# Configurar o pino GPIO12 como saída
led = Pin(12, Pin.OUT)

while True:
    led.value(1)  # Acender o LED
    utime.sleep(1)  # Esperar por 1 segundo
    led.value(0)  # Apagar o LED
    utime.sleep(1)  # Esperar por 1 segundo
