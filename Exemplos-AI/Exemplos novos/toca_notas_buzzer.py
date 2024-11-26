from machine import Pin, PWM, ADC
import utime

# Configuração dos GPIOs
buzzer = PWM(Pin(21))  # Buzzer A
button_a = Pin(6, Pin.IN, Pin.PULL_UP)  # Botão B
joystick_x = ADC(Pin(27))  # Eixo X do joystick
joystick_y = ADC(Pin(26))  # Eixo Y do joystick

# Notas musicais (frequências em Hz)
NOTAS = {
    "do": 261,  # Dó
    "re": 293,  # Ré
    "mi": 329,  # Mi
    "fa": 349,  # Fá
    "sol": 392,  # Sol
}

def tocar_nota(frequencia, duracao=0.1):
    """Toca uma nota no buzzer."""
    if frequencia > 0:  # Frequência válida
        buzzer.freq(frequencia)
        buzzer.duty_u16(500)  # Volume médio
        utime.sleep(duracao)
        buzzer.duty_u16(0)  # Para o som

# Loop principal
print("Use o joystick e o botão B para tocar as notas musicais.")

while True:
    # Leitura do joystick
    posicao_x = joystick_x.read_u16()
    posicao_y = joystick_y.read_u16()
    
    # Identifica a direção do joystick
    if posicao_x < 20000:  # Joystick para esquerda
        print("Tocando Dó")
        tocar_nota(NOTAS["do"])
    elif posicao_x > 45000:  # Joystick para direita
        print("Tocando Ré")
        tocar_nota(NOTAS["re"])
    elif posicao_y < 20000:  # Joystick para baixo
        print("Tocando Fá")
        tocar_nota(NOTAS["fa"])
    elif posicao_y > 45000:  # Joystick para cima
        print("Tocando Mi")
        tocar_nota(NOTAS["mi"])
    # Verifica se o botão B foi pressionado
    if not button_a.value():  # Botão B pressionado
        print("Tocando Sol")
        tocar_nota(NOTAS["sol"])
    
    utime.sleep(0.1)  # Pausa para evitar leituras consecutivas

