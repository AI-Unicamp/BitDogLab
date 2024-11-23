from machine import Pin
import time
# Definir o botão A no GPIO 5 com resistor pull-up interno
botao_A = Pin(5, Pin.IN, Pin.PULL_UP)
# Definir os LEDs RGB conectados aos GPIOs com resistores
led_red = Pin(13, Pin.OUT) # Pino do LED vermelho no GPIO 13
led_green = Pin(11, Pin.OUT) # Pino do LED verde no GPIO 11
led_blue = Pin(12, Pin.OUT) # Pino do LED azul no GPIO 12
# Função para desligar o LED RGB
def apagar_led():
led_red.off()
led_green.off()
led_blue.off()
# Função para acender o LED RGB (por exemplo, vermelho aceso)
def acender_led_rgb():
led_red.on() # Liga o LED vermelho
led_green.off() # Desliga o LED verde
led_blue.off() # Desliga o LED azul
# Função para piscar o LED RGB 10 vezes
def piscar_led_rgb():
for _ in range(10):
acender_led_rgb() # Acende o LED RGB
time.sleep(0.5) # Espera 0,5 segundos
apagar_led() # Apaga o LED RGB
time.sleep(0.5) # Espera 0,5 segundos

# Loop principal
while True:
# Verifica se o botão A foi pressionado
if botao_A.value() == 0: # O valor é 0 quando o botão é pressionado
# Se o botão foi pressionado, acende o LED RGB
acender_led_rgb()
else:
# Se o botão não foi pressionado, apaga o LED RGB
apagar_led()
# Pisca o LED RGB 10 vezes

piscar_led_rgb()
# Pequena pausa para evitar leituras muito rápidas
time.sleep(0.1)
