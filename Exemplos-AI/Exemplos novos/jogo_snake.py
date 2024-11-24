A matriz de LEDs representa o tabuleiro de 5x5.
A cobra é formada por LEDs verdes.
A comida é representada por um LED vermelho.
Controles:

O joystick controla a direção (cima, baixo, esquerda, direita).
Cada movimento é um passo da cobra.
Regras do Jogo:

A cobra cresce ao comer a comida.
O jogo termina se a cobra bater em si mesma ou em uma parede.
Feedback:

Aumentar a velocidade da cobra conforme o comprimento cresce.
Reiniciar o jogo em caso de derrota.

from machine import Pin, ADC
import neopixel
from utime import sleep
import random

# Configurações da matriz de LEDs
NUM_LEDS = 25
PIN = 7
np = neopixel.NeoPixel(Pin(PIN), NUM_LEDS)

# Mapeamento da matriz (linear para 5x5)
LED_MATRIX = [
    [0, 1, 2, 3, 4],
    [5, 6, 7, 8, 9],
    [10, 11, 12, 13, 14],
    [15, 16, 17, 18, 19],
    [20, 21, 22, 23, 24]
]

# Configuração do joystick
x_axis = ADC(26)  # Eixo X do joystick
y_axis = ADC(27)  # Eixo Y do joystick

# Cores
COBRA = (0, 255, 0)  # Verde
COMIDA = (255, 0, 0)  # Vermelho
VAZIO = (0, 0, 0)  # Apagado

# Variáveis do jogo
cobra = [(2, 2)]  # Começa no centro
direcao = (0, 1)  # Direção inicial (direita)
comida = (random.randint(0, 4), random.randint(0, 4))  # Posição inicial da comida
velocidade = 0.5  # Velocidade inicial (em segundos)

# Funções auxiliares
def apagar():
    """Apaga todos os LEDs."""
    np.fill(VAZIO)
    np.write()

def desenhar():
    """Atualiza a matriz de LEDs com a posição da cobra e da comida."""
    apagar()
    for segmento in cobra:
        x, y = segmento
        np[LED_MATRIX[y][x]] = COBRA
    cx, cy = comida
    np[LED_MATRIX[cy][cx]] = COMIDA
    np.write()

def mover_cobra():
    """Move a cobra na direção atual."""
    global cobra, comida, velocidade
    # Calcula a nova posição da cabeça
    cabeca = cobra[-1]
    nova_cabeca = (cabeca[0] + direcao[0], cabeca[1] + direcao[1])

    # Verifica colisão com parede
    if nova_cabeca[0] < 0 or nova_cabeca[0] > 4 or nova_cabeca[1] < 0 or nova_cabeca[1] > 4:
        return False

    # Verifica colisão com o próprio corpo
    if nova_cabeca in cobra:
        return False

    # Adiciona a nova cabeça
    cobra.append(nova_cabeca)

    # Verifica se comeu a comida
    if nova_cabeca == comida:
        # Gera nova comida
        while comida in cobra:
            comida = (random.randint(0, 4), random.randint(0, 4))
        # Aumenta a velocidade
        velocidade = max(0.1, velocidade - 0.02)  # Limite de velocidade mínima
    else:
        # Remove o segmento da cauda (não cresce)
        cobra.pop(0)

    return True

def atualizar_direcao():
    """Atualiza a direção com base no joystick."""
    global direcao
    x = x_axis.read_u16()
    y = y_axis.read_u16()

    if x < 10000:  # Esquerda
        direcao = (-1, 0)
    elif x > 55000:  # Direita
        direcao = (1, 0)
    elif y < 10000:  # Cima
        direcao = (0, -1)
    elif y > 55000:  # Baixo
        direcao = (0, 1)

# Programa principal
print("Iniciando o jogo da cobrinha!")

while True:
    desenhar()
    atualizar_direcao()
    if not mover_cobra():
        print("Game Over!")
        apagar()
        break
    sleep(velocidade)

