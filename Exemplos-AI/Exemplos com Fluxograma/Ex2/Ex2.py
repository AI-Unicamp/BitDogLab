from machine import Pin, PWM
import time

# Configurações do LED azul e do botão
led_blue = PWM(Pin(11))  # LED azul conectado no GPIO 11
led_blue.freq(1000)  # Configura a frequência do PWM para o LED

button_a = Pin(5, Pin.IN, Pin.PULL_UP)  # Botão A conectado ao GPIO 5 com pull-up

def acender_led(led):
    led.duty_u16(65535)  # Define o brilho máximo para acender o LED

def apagar_led(led):
    led.duty_u16(0)  # Define o brilho como zero para apagar o LED

def piscar_led(led, vezes, intervalo):
    for _ in range(vezes):
        acender_led(led)
        time.sleep(intervalo)
        apagar_led(led)
        time.sleep(intervalo)

def verificar_botao_pressionado(botao):
    return not botao.value()  # Retorna True se o botão foi pressionado (nível baixo)

# Loop principal
while True:
    if verificar_botao_pressionado(button_a):
        # Acende o LED azul
        acender_led(led_blue)
       
        # Inicia o ciclo de piscar 10 vezes
        contador_pisca = 0
        while contador_pisca < 10:
            piscar_led(led_blue, 1, 0.5)  # Pisca uma vez com intervalo de 0.5 segundos
            contador_pisca += 1

        # Apaga o LED após o ciclo de 10 piscadas
        apagar_led(led_blue)
    else:
        # Se o botão não estiver pressionado, mantém o LED apagado
        apagar_led(led_blue)

    time.sleep(0.1)  # Pequeno delay para evitar múltiplas leituras rápidas do botão

