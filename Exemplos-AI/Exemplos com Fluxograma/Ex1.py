from machine import Pin
import utime

# Configuração dos pinos
led_azul = Pin(12, Pin.OUT)  # LED azul conectado ao GPIO11
botao_a = Pin(5, Pin.IN, Pin.PULL_UP)  # Botão A conectado ao GPIO5, com pull-up

# Função principal
while True:
    if botao_a.value() == 0:  # Se o botão A for pressionado (estado LOW)
        led_azul.value(1)  # Acender o LED azul
    else:
        led_azul.value(0)  # Apagar o LED azul
   
    utime.sleep(0.1)  # Pequeno atraso para evitar leituras rápidas demais
