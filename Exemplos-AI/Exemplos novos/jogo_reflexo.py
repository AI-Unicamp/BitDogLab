from machine import Pin
import random
from utime import sleep
from ssd1306 import SSD1306_I2C

# Configuração do LED e do botão
LED_PIN = 15  # GPIO onde o LED está conectado
BOTAO_PIN = 14  # GPIO onde o botão está conectado
led = Pin(LED_PIN, Pin.OUT)
botao = Pin(BOTAO_PIN, Pin.IN, Pin.PULL_UP)  # Botão com pull-up

# Configuração da tela OLED
i2c = I2C(0, scl=Pin(17), sda=Pin(16))  # Configuração do I2C para a tela
oled = SSD1306_I2C(128, 64, i2c)  # Inicialização da tela OLED

# Inicializa o contador de pontos
pontos = 0

# Função para mostrar os pontos na tela OLED
def mostrar_pontos(pontos):
    oled.fill(0)  # Limpa a tela
    oled.text('Pontos: ' + str(pontos), 0, 0)  # Exibe os pontos
    oled.show()

# Função principal do jogo
def jogo():
    global pontos
    
    while True:
        # Acende o LED por um tempo aleatório entre 0.5 e 3 segundos
        tempo_led = random.uniform(0.5, 3.0)
        led.on()
        sleep(tempo_led)

        # Verifica se o botão foi pressionado antes de 1 segundo após o LED acender
        if not botao.value() and tempo_led <= 1:
            pontos += 1  # Adiciona um ponto
            mostrar_pontos(pontos)  # Mostra os pontos na tela

        # Apaga o LED
        led.off()
        sleep(0.5)  # Aguarda um pouco antes de acender o LED novamente

# Programa principal
print("Jogo de Reação! Pressione o botão antes que o LED apague.")
jogo()
