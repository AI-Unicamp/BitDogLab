from machine import Pin, PWM
from utime import sleep

# Configuração do buzzer
BUZZER_PIN = 21  # GPIO conectado ao buzzer
buzzer = PWM(Pin(BUZZER_PIN))

# Frequências das notas musicais em Hertz
NOTES = {
    "C": 261,  # Nota Dó
    "D": 294,  # Nota Ré
    "E": 329,  # Nota Mi
    "F": 349,  # Nota Fá
    "G": 392   # Nota Sol (se precisar adicionar)
}

# Função para tocar uma nota
def tocar_nota(nota, duracao):
    if nota in NOTES:
        buzzer.freq(NOTES[nota])  # Define a frequência da nota
        buzzer.duty_u16(3000)    # Define o volume (ajustável)
        sleep(duracao)           # Toca a nota pelo tempo definido
        buzzer.duty_u16(0)       # Para o som
        sleep(0.1)               # Pausa curta entre as notas

# Função para tocar a melodia "Parabéns para Você"
def parabens():
    # Primeiro verso
    tocar_nota("C", 0.5)  # Dó
    tocar_nota("D", 0.5)  # Ré
    tocar_nota("E", 1.0)  # Mi
    tocar_nota("D", 0.5)  # Ré
    tocar_nota("F", 0.5)  # Fá
    tocar_nota("E", 1.0)  # Mi
    sleep(1)              # Pausa entre os versos

    # Segundo verso (mesma melodia, pode variar conforme necessário)
    tocar_nota("C", 0.5)  # Dó
    tocar_nota("D", 0.5)  # Ré
    tocar_nota("E", 1.0)  # Mi
    tocar_nota("D", 0.5)  # Ré
    tocar_nota("F", 0.5)  # Fá
    tocar_nota("E", 1.0)  # Mi

# Programa principal
print("Tocando a melodia 'Parabéns para Você' no buzzer")
parabens()
