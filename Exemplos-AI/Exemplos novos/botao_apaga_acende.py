'''
Pressionar alternadamente o botão A liga e desliga o LED central.
A cada vez que o LED é ligado, ele troca de cor entre vermelho, azul e verde
'''
from machine import Pin
import neopixel
import utime

# Configuração do NeoPixel
NUM_LEDS = 25
np = neopixel.NeoPixel(Pin(7), NUM_LEDS)

# Configuração do Botão
button_a = Pin(5, Pin.IN, Pin.PULL_UP)

# LED central (índice 12 na matriz 5x5)
LED_CENTRAL = 12

# Cores
CORES = [(255, 0, 0), (0, 0, 255), (0, 255, 0)]  # Vermelho, Azul, Verde
estado_led = False  # LED apagado inicialmente
cor_atual = 0  # Índice da cor atual

def alternar_led():
    """Alterna o estado e a cor do LED central."""
    global estado_led, cor_atual
    
    if estado_led:  # Se o LED está ligado, apaga
        np[LED_CENTRAL] = (0, 0, 0)
        estado_led = False
        print("LED apagado")
    else:  # Se o LED está apagado, liga com a próxima cor
        np[LED_CENTRAL] = CORES[cor_atual]
        cor_atual = (cor_atual + 1) % len(CORES)  # Avança para a próxima cor
        estado_led = True
        print(f"LED aceso: {CORES[cor_atual]}")
    
    np.write()

# Loop principal
while True:
    if not button_a.value():  # Botão A pressionado
        alternar_led()
        utime.sleep(0.2)  # Debounce para evitar leituras duplicadas
