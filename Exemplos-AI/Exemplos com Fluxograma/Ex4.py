from machine import Pin
import time
# Definir o botão A no GPIO 5
botao_A = Pin(5, Pin.IN, Pin.PULL_DOWN)
# Definir o LED RGB nos pinos correspondentes (exemplo para LED RGB comum)
led_red = Pin(18, Pin.OUT) # Defina o pino correto do seu LED
led_green = Pin(19, Pin.OUT)
led_blue = Pin(20, Pin.OUT)
# Função para apagar o LED RGB
def apagar_led():
led_red.off()
led_green.off()
led_blue.off()
# Função para acender o LED RGB (definido para acender o vermelho como exemplo)
def acender_led_rgb():
led_red.on()
led_green.off()
led_blue.off()
# Loop principal
while True:
# Verifica se o botão A foi pressionado

if botao_A.value() == 1:
# Se o botão foi pressionado, acende o LED RGB
acender_led_rgb()
else:
# Caso contrário, apaga o LED RGB
apagar_led()
# Pequena pausa para evitar múltiplas leituras rápidas
time.sleep(0.1)
