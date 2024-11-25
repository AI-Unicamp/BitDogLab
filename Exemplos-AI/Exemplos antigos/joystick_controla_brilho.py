# Controla Brilho do LED central com o joystick

from machine import Pin, ADC, PWM
import time

# Configuração dos pinos do joystick
vrx = ADC(Pin(27))  # Eixo X
vry = ADC(Pin(26))  # Eixo Y
sw = Pin(22, Pin.IN, Pin.PULL_UP)  # Botão

# Configuração dos pinos dos LEDs
led_r = PWM(Pin(12, Pin.OUT))
led_g = PWM(Pin(13, Pin.OUT))
led_b = PWM(Pin(11, Pin.OUT))

# Definição das frequências dos PWMs dos LEDs
led_r.freq(500)
led_g.freq(500)
led_b.freq(500)

# Função para mapear o valor do joystick para o brilho do LED
def map_value(value, in_min, in_max, out_min, out_max):
    return int((value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

# Loop principal
while True:
    x_val = vrx.read_u16()
    y_val = vry.read_u16()
    
    # Mapeia os valores do joystick para os valores de PWM dos LEDs
    led_r.duty_u16(x_val)
    led_g.duty_u16(y_val)
    led_b.duty_u16(x_val // 2 + y_val // 2)

    if sw.value() == 0:  # Se o botão do joystick for pressionado
        led_r.duty_u16(0)
        led_g.duty_u16(0)
        led_b.duty_u16(0)
        
    # Pequena pausa para não sobrecarregar o processador.
    time.sleep_ms(10)
