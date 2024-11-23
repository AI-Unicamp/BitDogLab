from machine import Pin, SoftI2C
import neopixel
from ssd1306 import SSD1306_I2C
from utime import sleep

# Configurações iniciais para o OLED
i2c = SoftI2C(scl=Pin(15), sda=Pin(14))  # Pinos I2C
oled = SSD1306_I2C(128, 64, i2c)  # Configuração do OLED (128x64)

# Configurações da matriz de LEDs
NUM_LEDS = 25  # Número total de LEDs na matriz 5x5
PIN = 7  # Pino onde a matriz Neopixel está conectada
np = neopixel.NeoPixel(Pin(PIN), NUM_LEDS)

# Mapeamento da matriz de LEDs com a origem no canto inferior direito
LED_MATRIX = [
    [24, 23, 22, 21, 20],    
    [15, 16, 17, 18, 19],
    [14, 13, 12, 11, 10],
    [5, 6, 7, 8, 9],
    [4, 3, 2, 1, 0]
]

# Função para exibir mensagens no OLED
def exibir_no_oled(mensagem):
    oled.fill(0)  # Limpa o display
    oled.text("BitDogLab:", 0, 0)  # Título fixo
    oled.text(mensagem, 0, 20)  # Mensagem recebida
    oled.show()  # Atualiza o display

# Função para controlar LEDs da matriz
def leds(x, y, r=20, g=20, b=20):
    if 0 <= x <= 4 and 0 <= y <= 4 and r <= 255 and g <= 255 and b <= 255:
        led_index = LED_MATRIX[4-y][x]
        np[led_index] = (r, g, b)
        np.write()
        mensagem = f'LED ({x},{y}) cor ({r},{g},{b})'
        print(mensagem)
        exibir_no_oled(mensagem)  # Mostra no OLED
        return mensagem
    else:
        mensagem = "Valores inválidos!"
        print(mensagem)
        exibir_no_oled(mensagem)  # Mostra erro no OLED
        return mensagem

# Função para apagar todos os LEDs
def apagar():
    np.fill((0, 0, 0))  # Todos os LEDs em preto (desligados)
    np.write()
    mensagem = "Todos os LEDs apagados"
    print(mensagem)
    exibir_no_oled(mensagem)  # Mostra no OLED

# Exemplos de uso:
leds(2, 2, 50, 50, 0)  # Acende o LED central na cor amarela
sleep(2)  # Aguarda 2 segundos
apagar()  # Apaga todos os LEDs
