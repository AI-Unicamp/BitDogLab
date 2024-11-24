from machine import Pin, I2C
import neopixel
from utime import sleep
import ssd1306

# Configurações da matriz de LEDs
NUM_LEDS = 25  # Total de LEDs na matriz 5x5
PIN = 7  # Pino onde a matriz Neopixel está conectada
np = neopixel.NeoPixel(Pin(PIN), NUM_LEDS)

# Mapeamento da matriz de LEDs com a origem no canto superior esquerdo
LED_MATRIX = [
    [0, 1, 2, 3, 4],
    [5, 6, 7, 8, 9],
    [10, 11, 12, 13, 14],
    [15, 16, 17, 18, 19],
    [20, 21, 22, 23, 24]
]

# Configuração dos botões
botao_a = Pin(11, Pin.IN, Pin.PULL_UP)  # Botão A (com pull-up interno)
botao_b = Pin(12, Pin.IN, Pin.PULL_UP)  # Botão B (com pull-up interno)

# Configuração da tela OLED
i2c = I2C(0, scl=Pin(22), sda=Pin(21))  # I2C nos pinos 22 (SCL) e 21 (SDA)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)  # Tela OLED com resolução de 128x64

# Variável para controlar o índice atual na matriz
led_index = 0

# Função para apagar todos os LEDs e limpar a tela OLED
def apagar():
    np.fill((0, 0, 0))  # Todos os LEDs desligados
    np.write()
    oled.fill(0)  # Limpa a tela OLED
    oled.text("Todos apagados", 0, 0)
    oled.show()
    sleep(1)
    oled.fill(0)
    oled.show()

# Função para acender o próximo LED e exibir na tela OLED
def acender_proximo(cor, cor_nome):
    global led_index
    if led_index < NUM_LEDS:
        np[led_index] = cor  # Define a cor do LED atual
        np.write()
        # Exibe na tela OLED
        oled.fill(0)  # Limpa a tela OLED
        oled.text(f"LED {led_index+1}/{NUM_LEDS}", 0, 0)
        oled.text(f"Cor: {cor_nome}", 0, 20)
        oled.show()
        led_index += 1  # Avança para o próximo LED
    else:
        led_index = 0  # Reseta a contagem
        apagar()  # Apaga todos os LEDs e limpa a tela OLED

# Programa principal
print("Pressione Botão A para vermelho, Botão B para azul.")

while True:
    if not botao_a.value():  # Botão A pressionado
        acender_proximo((255, 0, 0), "Vermelho")  # LED vermelho
        sleep(0.2)  # Debounce para evitar múltiplos cliques rápidos

    if not botao_b.value():  # Botão B pressionado
        acender_proximo((0, 0, 255), "Azul")  # LED azul
        sleep(0.2) 
