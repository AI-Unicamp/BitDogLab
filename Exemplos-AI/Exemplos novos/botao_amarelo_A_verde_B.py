
from machine import Pin
import utime

# Configuração dos pinos
botao_a = Pin(5, Pin.IN, Pin.PULL_UP)  # Configura o botão A com pull-up interno
botao_b = Pin(6, Pin.IN, Pin.PULL_UP)  # Configura o botão B com pull-up interno

led_vermelho = Pin(13, Pin.OUT)  # Canal vermelho do LED RGB
led_verde = Pin(11, Pin.OUT)     # Canal verde do LED RGB
led_azul = Pin(12, Pin.OUT)      # Canal azul do LED RGB

while True:
    # Lê o estado dos botões
    estado_a = botao_a.value()
    estado_b = botao_b.value()
    
    # Verifica a condição para acender o LED nas cores desejadas
    if estado_a == 0 and estado_b == 0:      # Ambos os botões pressionados
        led_vermelho.value(0)
        led_verde.value(0)
        led_azul.value(1)                    # Acende o LED azul
    elif estado_a == 0:                      # Apenas o botão A pressionado
        led_vermelho.value(1)
        led_verde.value(1)
        led_azul.value(0)                    # Acende o LED amarelo (vermelho + verde)
    elif estado_b == 0:                      # Apenas o botão B pressionado
        led_vermelho.value(0)
        led_verde.value(1)
        led_azul.value(0)                    # Acende o LED verde
    else:
        led_vermelho.value(0)
        led_verde.value(0)
        led_azul.value(0)                    # Desliga o LED quando nenhum botão é pressionado
    
    utime.sleep(0.1)  # Delay para evitar leituras muito rápidas