from machine import Pin, ADC, PWM
import time

# Configuração dos pinos do microfone e LEDs RGB
mic = ADC(Pin(28))
led_r = PWM(Pin(13))
led_g = PWM(Pin(11))
led_b = PWM(Pin(12))

led_r.freq(1000)
led_g.freq(1000)
led_b.freq(1000)

def led(r, g, b):
    led_r.duty_u16(int(r * 65535 / 255))
    led_g.duty_u16(int(g * 65535 / 255))
    led_b.duty_u16(int(b * 65535 / 255))

def sound_to_light():
    while True:
        mic_value = mic.read_u16()
        brightness = min(255, mic_value // 256)  # Converte o valor do microfone para brilho (0-255)
        led(brightness, brightness, brightness)  # Define a cor do LED
        time.sleep(0.1)

# Chama a função para criar o efeito luminoso comandado por som
sound_to_light()
