from machine import Pin
import utime

# Configuração dos pinos
botao_a = Pin(5, Pin.IN, Pin.PULL_UP)  # Configura o botão A com pull-up interno
led_verde = Pin(11, Pin.OUT)  # Configura o canal verde do LED RGB como saída

while True:
    # Verifica se o botão A está pressionado
    if botao_a.value() == 0:  # O estado será LOW (0) quando o botão for pressionado
        led_verde.value(1)    # Acende o LED verde
    else:
        led_verde.value(0)    # Apaga o LED verde quando o botão não está pressionado
    
    utime.sleep(0.1)  # Pequeno delay para evitar leitura muito rápida