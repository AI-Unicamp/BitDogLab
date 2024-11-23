from machine import Pin, PWM
from utime import sleep

# Configuração dos buzzers
buzzer_a = PWM(Pin(21))  # Buzzer A no GPIO21
buzzer_b = PWM(Pin(10))  # Buzzer B no GPIO10

# Configuração dos botões
botao_a = Pin(11, Pin.IN, Pin.PULL_UP)  # Botão A no GPIO11
botao_b = Pin(12, Pin.IN, Pin.PULL_UP)  # Botão B no GPIO12

# Frequências das notas
NOTA_A = 440  # Nota Lá (A4) para o Buzzer A
NOTA_B = 392  # Nota Sol (G4) para o Buzzer B
NOTA_C = 523  # Nota Dó (C5) para os dois buzzers juntos

# Função para tocar uma nota em um buzzer passivo
def tocar_nota(buzzer, frequencia, duracao=0.5):
    """
    Toca uma nota no buzzer passivo.
    :param buzzer: Objeto PWM do buzzer
    :param frequencia: Frequência da nota (Hz)
    :param duracao: Duração da nota (segundos)
    """
    buzzer.freq(frequencia)  # Define a frequência
    buzzer.duty_u16(32768)  # Define o volume (50% do duty cycle)
    sleep(duracao)  # Toca a nota por um tempo específico
    buzzer.duty_u16(0)  # Para o som

# Programa principal
print("Pressione os botões para controlar os buzzers.")

while True:
    if not botao_a.value() and botao_b.value():  # Apenas Botão A pressionado
        tocar_nota(buzzer_a, NOTA_A)  # Toca a nota no Buzzer A
        sleep(0.2)  # Delay para debounce
    elif not botao_b.value() and botao_a.value():  # Apenas Botão B pressionado
        tocar_nota(buzzer_b, NOTA_B)  # Toca a nota no Buzzer B
        sleep(0.2)  # Delay para debounce
    elif not botao_a.value() and not botao_b.value():  # Ambos os botões pressionados
        # Toca uma nota em ambos os buzzers simultaneamente
        buzzer_a.freq(NOTA_C)
        buzzer_b.freq(NOTA_C)
        buzzer_a.duty_u16(32768)
        buzzer_b.duty_u16(32768)
        sleep(0.5)  # Duração da nota
        buzzer_a.duty_u16(0)
        buzzer_b.duty_u16(0)
        sleep(0.2)  # Delay para debounce
