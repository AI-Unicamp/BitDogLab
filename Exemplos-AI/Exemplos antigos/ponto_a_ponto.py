# Programa que simula um pulso cárdiaco no buzzer
from machine import PWM, Pin
import neopixel
import time

# Configuração do NeoPixel
NUM_LEDS = 25
np = neopixel.NeoPixel(Pin(7), NUM_LEDS)

# Configuração do Buzzer
buzzer = PWM(Pin(21))
buzzer_freq = 1000  # Frequência para o beep

def beep(duration=0.1):
    ''' Toca um beep com a duração especificada '''
    buzzer.freq(buzzer_freq)
    buzzer.duty_u16(5000)  # Intensidade média
    time.sleep(duration)
    buzzer.duty_u16(0)  # Desliga o buzzer

def dim_leds(led_sequence, current_index):
    dim_factor = 255 // len(led_sequence)
    for idx in range(current_index):
        r, g, b = np[led_sequence[idx]]
        r = max(r - dim_factor, 0)
        g = max(g - dim_factor, 0)
        b = max(b - dim_factor, 0)
        np[led_sequence[idx]] = (r, g, b)

def heartbeat_effect():
    # Limpa todos os LEDs
    for i in range(NUM_LEDS):
        np[i] = (0, 0, 0)
    np.write()
    
    # Sequência de LEDs para simular o pulso cardíaco
    sequence = [14, 6, 12, 21, 10]
    delay_time = 0.2  # Ajuste para a duração do efeito
    
    for idx, led in enumerate(sequence):
        np[led] = (255, 0, 0)  # Acende o LED vermelho
        dim_leds(sequence, idx)  # Diminui o brilho dos LEDs na sequência
        np.write()
        time.sleep(delay_time)

    # Certifique-se de que todos os LEDs estão apagados ao final da animação
    for led in sequence:
        np[led] = (0, 0, 0)
    np.write()
    
    # Toca o beep no buzzer
    beep()

# Loop infinito para repetir o efeito
while True:
    heartbeat_effect()
    time.sleep(1)  # Tempo entre os batimentos
