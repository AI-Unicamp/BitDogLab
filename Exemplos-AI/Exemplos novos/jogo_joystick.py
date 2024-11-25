''' Este código é de um jogo onde aleatóriamente é impressa uma seta,
    para cima, para baixo, para esquerda ou para a direita.
    Ele recebe o input do usuário pelo joystick, se acertar, a matriz fica verde,
     se errar, vermelha
'''
from machine import Pin, ADC
import neopixel
from utime import sleep
import random

# Configurações da matriz de LEDs
NUM_LEDS = 25  # Total de LEDs na matriz 5x5
PIN = 7  # Pino onde a matriz Neopixel está conectada
np = neopixel.NeoPixel(Pin(PIN), NUM_LEDS)

# Mapeamento da matriz de LEDs com a origem no canto superior esquerdo
LED_MATRIX = [
    [0,   1,  2,  3,  4],
    [5,   6,  7,  8,  9],
    [10, 11, 12, 13, 14],
    [15, 16, 17, 18, 19],
    [20, 21, 22, 23, 24]
]

# Configuração do joystick (eixos analógicos)
joystick_x = ADC(27)  # Pino do eixo X
joystick_y = ADC(26)  # Pino do eixo Y

# Funções auxiliares
def apagar():
    """Apaga todos os LEDs."""
    np.fill((0, 0, 0))
    np.write()

def desenhar_seta(direcao):
    """
    Desenha uma seta na matriz com base na direção:
    'cima', 'baixo', 'esquerda', 'direita'
    """
    apagar()
    if direcao == "cima":
        coords = [2, 7, 12, 17, 22, 6, 8, 10, 14]  # Seta para cima
    elif direcao == "baixo":
        coords = [2, 7, 12, 17, 22, 10, 14, 16, 18]  # Seta para baixo
    elif direcao == "esquerda":
        coords = [10, 11, 12, 13, 14, 2, 6, 16, 22]  # Seta para a esquerda
    elif direcao == "direita":
        coords = [10, 11, 12, 13, 14, 2, 8, 18, 22]  # Seta para a direita
    else:
        return

    for c in coords:
        np[c] = (0, 0, 100)  # Cor azul para a seta
    np.write()

def ler_joystick():
    """
    Lê o estado do joystick e determina a direção.
    Retorna: 'cima', 'baixo', 'esquerda', 'direita', ou 'centro'
    """
    x = joystick_x.read_u16()
    y = joystick_y.read_u16()

    # Define os limiares para determinar a direção do joystick
    if x < 15000:
        return "esquerda"
    elif x > 50000:
        return "direita"
    elif y < 15000:
        return "cima"
    elif y > 50000:
        return "baixo"
    else:
        return "centro"

def feedback(correto):
    """
    Dá feedback na matriz de LEDs:
    - Verde se a direção estiver correta
    - Vermelho se a direção estiver errada
    """
    cor = (0, 100, 0) if correto else (100, 0, 0)  # Verde ou vermelho
    np.fill(cor)
    np.write()
    sleep(0.5)
    apagar()

# Programa principal
print("Jogo iniciado. Movimente o joystick para a direção da seta.")

while True:
    # Escolhe uma direção aleatória
    direcao_esperada = random.choice(["cima", "baixo", "esquerda", "direita"])
    desenhar_seta(direcao_esperada)

    # Aguarda o jogador fazer um movimento
    acertou = False
    while not acertou:
        direcao_jogador = ler_joystick()
        if direcao_jogador != "centro":  # Evita reagir enquanto o joystick está no centro
            acertou = direcao_jogador == direcao_esperada
            feedback(acertou)
            break  # Sai do loop para gerar a próxima seta

    sleep(0.5)  # Pequena pausa antes de mostrar a próxima seta
