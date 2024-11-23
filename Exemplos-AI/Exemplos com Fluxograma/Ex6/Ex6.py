from machine import Pin
import utime

# Configuração do LED (GPIO12) e do Botão A (GPIO5)
led = Pin(12, Pin.OUT)  # Configura o LED como saída
botao_a = Pin(5, Pin.IN, Pin.PULL_UP)  # Configura o botão como entrada com pull-up interno

while True:
    if botao_a.value() == 0:  # Botão pressionado (nível lógico baixo)
        led.value(1)  # Acende o LED
    else:
        led.value(0)  # Apaga o LED
    utime.sleep(0.1)  # Pequeno delay para evitar leitura excessiva
