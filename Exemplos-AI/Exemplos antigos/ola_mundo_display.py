from machine import Pin, SoftI2C
import ssd1306

# Declaração das variáveis para controle do display OLED.
i2c = SoftI2C(scl=Pin(15), sda=Pin(14))  # Configura o barramento I2C
oled = ssd1306.SSD1306_I2C(128, 64, i2c)  # Usa a instância 'i2c' aqui

# Comandos do display.
oled.fill(0)  # Primeiro, limpa o display.
oled.text("Ola, Mundo!", 20, 28)  # Segundo, escreve "Ola, Mundo!" no centro do display.
oled.show()  # Finalmente, atualiza o display.

