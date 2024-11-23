'''Condicional para ambos os botões:
if button_a.value() == 0 and button_b.value() == 0: Verifica se ambos os botões A e B estão pressionados simultaneamente. Se sim, exibe a mensagem "Botão A e B pressionados!".
Condicionais individuais para cada botão:
elif button_a.value() == 0: Caso apenas o Botão A esteja pressionado, exibe "Botão A pressionado!".
elif button_b.value() == 0: Caso apenas o Botão B esteja pressionado, exibe "Botão B pressionado!".
Mensagem padrão:
else: Se nenhum dos botões estiver pressionado, exibe "Aguardando ação...". '''

from machine import SoftI2C, Pin
from ssd1306 import SSD1306_I2C
import time

# Configuração do display OLED
i2c_oled = SoftI2C(scl=Pin(15), sda=Pin(14))  # SDA e SCL conectados aos GPIO14 e GPIO15
oled = SSD1306_I2C(128, 64, i2c_oled)         # Resolução do OLED 128x64

# Configuração dos botões
button_a = Pin(5, Pin.IN, Pin.PULL_UP)  # Botão A no GPIO5
button_b = Pin(6, Pin.IN, Pin.PULL_UP)  # Botão B no GPIO6

def display_message(message):
    """Mostra uma mensagem no display OLED."""
    oled.fill(0)           # Limpa o display
    oled.text(message, 0, 25)  # Exibe a mensagem no centro da tela
    oled.show()

try:
    while True:
        if button_a.value() == 0 and button_b.value() == 0:  # Ambos os botões pressionados
            display_message("Botão A e B pressionados!")
        elif button_a.value() == 0:  # Apenas Botão A pressionado
            display_message("Botão A pressionado!")
        elif button_b.value() == 0:  # Apenas Botão B pressionado
            display_message("Botão B pressionado!")
        else:
            display_message("Aguardando ação...")  # Nenhum botão pressionado

        time.sleep(0.1)  # Pequeno atraso para evitar leituras rápidas demais
except KeyboardInterrupt:
    oled.fill(0)  # Limpa o display ao finalizar o programa
    oled.show()
