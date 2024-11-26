from machine import Pin
import time

# Configuração dos pinos
led_vermelho = Pin(12, Pin.OUT)  # Pino do LED vermelho (GPIO12)
led_verde = Pin(13, Pin.OUT)     # Pino do LED verde (GPIO13)
led_azul = Pin(11, Pin.OUT)      # Pino do LED azul (GPIO11)
botao_a = Pin(5, Pin.IN, Pin.PULL_UP)  # Botão A com pull-up no GPIO5

# Função para desligar o LED RGB
def apagar_rgb():
    led_vermelho.off()
    led_verde.off()
    led_azul.off()

# Função para acender o LED RGB (cor azul)
def acender_rgb_azul():
    led_vermelho.off()
    led_verde.off()
    led_azul.on()

# Função principal
while True:
    if botao_a.value() == 0:  # Se o botão A está pressionado (PULL-UP ativo = valor 0)
        acender_rgb_azul()  # Acende o LED RGB (cor azul)
    else:
        apagar_rgb()  # Apaga o LED RGB
   
    time.sleep(0.1)  # Pequeno atraso para evitar leituras rápidas demais
