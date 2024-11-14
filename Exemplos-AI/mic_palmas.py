from machine import Pin, ADC
import time

mic = ADC(Pin(28))
led = Pin(13, Pin.OUT)  # Configuração do pino do LED

def detect_clap():
    threshold = 45000  # Limite para detectar a palma
    led_state = False

    while True:
        mic_value = mic.read_u16()
        if mic_value > threshold:
            led_state = not led_state  # Alterna o estado do LED
            led.value(led_state)
            time.sleep(0.5)  # Debounce para evitar múltiplas detecções rápidas
        time.sleep(0.01)

# Chama a função para detectar palmas
detect_clap()