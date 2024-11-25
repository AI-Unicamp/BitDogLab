# Código para desligar todos os componentes da BitDogLab

from machine import Pin, PWM, SoftI2C
import neopixel
from ssd1306 import SSD1306_I2C

# Configurações gerais
# Número de LEDs na matriz de LEDs
NUM_LEDS = 25

# Inicializar os componentes da BitDogLab
# Matriz de LEDs (NeoPixel)
np = neopixel.NeoPixel(Pin(7), NUM_LEDS)

# LEDs RGB principais
led_red = PWM(Pin(13))
led_green = PWM(Pin(11))
led_blue = PWM(Pin(12))

# Buzzer A e B
buzzer_a = PWM(Pin(21))
buzzer_b = PWM(Pin(10))

# Display OLED
i2c_oled = SoftI2C(scl=Pin(15), sda=Pin(14))
oled = SSD1306_I2C(128, 64, i2c_oled)

# Funções para desligar os componentes
def apagar_matriz_leds():
    for i in range(NUM_LEDS):
        np[i] = (0, 0, 0)  # Apagar todos os LEDs (preto)
    np.write()

def desligar_leds_rgb():
    led_red.duty_u16(0)
    led_green.duty_u16(0)
    led_blue.duty_u16(0)

def apagar_oled():
    oled.fill(0)  # Preencher a tela com "preto"
    oled.show()   # Atualizar o display

def desligar_buzzers():
    buzzer_a.duty_u16(0)  # Desligar o PWM do Buzzer A
    buzzer_a.deinit()     # Desativar o PWM
    buzzer_b.duty_u16(0)  # Desligar o PWM do Buzzer B
    buzzer_b.deinit()     # Desativar o PWM

# Desligar todos os componentes
def desligar_tudo():
    apagar_matriz_leds()
    desligar_leds_rgb()
    apagar_oled()
    desligar_buzzers()
    print("Todos os componentes foram desligados!")

# Chamar a função principal
desligar_tudo()
