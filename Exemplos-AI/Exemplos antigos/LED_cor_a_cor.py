# Troca entre 7 cores: Branco, Vermelho, Amarelo, Verde, Ciano, Azul, Magenta
from machine import Pin
import utime

# Configuração dos pinos para os LEDs RGB
green = Pin(11, Pin.OUT)
blue = Pin(12, Pin.OUT)
red = Pin(13, Pin.OUT)

while True:
    # Branco (todas as cores ligadas)
    red.value(1)
    green.value(1)
    blue.value(1)
    utime.sleep(1)
    
    # Vermelho (somente o vermelho ligado)
    red.value(1)
    green.value(0)
    blue.value(0)
    utime.sleep(1)
    
    # Amarelo (vermelho + verde)
    red.value(1)
    green.value(1)
    blue.value(0)
    utime.sleep(1)
    
    # Verde (somente o verde ligado)
    red.value(0)
    green.value(1)
    blue.value(0)
    utime.sleep(1)
    
    # Ciano (verde + azul)
    red.value(0)
    green.value(1)
    blue.value(1)
    utime.sleep(1)

    # Azul (somente o azul ligado)
    red.value(0)
    green.value(0)
    blue.value(1)
    utime.sleep(1)
    
    # Magenta (vermelho + azul)
    red.value(1)
    green.value(0)
    blue.value(1)
    utime.sleep(1)
    
    # Apagado (todas as cores desligadas)
    red.value(0)
    green.value(0)
    blue.value(0)
    utime.sleep(1)
