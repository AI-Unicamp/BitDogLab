# Toca Lá no buzzer se apertar o botão A e Sol se apertar o botão B
from machine import Pin, PWM
from utime import sleep

# Configuração dos buzzers
buzzer_a = PWM(Pin(21))  # Buzzer A no GPIO21
buzzer_b = PWM(Pin(10))  # Buzzer B no GPIO10

# Configuração dos botões
botao_a = Pin(5, Pin.IN, Pin.PULL_UP)  # Botão A no GPIO5
botao_b = Pin(6, Pin.IN, Pin.PULL_UP)  # Botão B no GPIO6

# Frequências das notas
NOTA_A = 261  # Nota Lá (A4) para o Buzzer A
NOTA_B = 293  # Nota Sol (G4) para o Buzzer B

# Função para tocar uma nota em um buzzer passivo
def tocar_nota(buzzer, frequencia, duracao=0.5):
    """
    Toca uma nota no buzzer passivo.
    :param buzzer: Objeto PWM do buzzer
    :param frequencia: Frequência da nota (Hz)
    :param duracao: Duração da nota (segundos)
    """
    buzzer.freq(frequencia)  # Define a frequência

    buzzer.duty_u16(1000)  # Define o volume 
    
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
    

