Exibição da pontuação na tela OLED.
Reinício automático após o "Game Over".
Adição de sons no buzzer para ações específicas.

A tela OLED exibe a pontuação em tempo real durante o jogo.
Reinício Automático:

Após o "Game Over", o jogo reinicia automaticamente após exibir a mensagem na tela OLED.
Sons no Buzzer:

Ao comer comida, é emitido um som curto.
Ao perder, é emitido um som mais longo e grave.

from machine import Pin, ADC, I2C
import neopixel
from utime import sleep
import ssd1306
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

# Configuração da tela OLED (I2C)
i2c = I2C(0, scl=Pin(17), sda=Pin(16))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Configuração do buzzer
buzzer = Pin(15, Pin.OUT)

# Cores
COBRA = (0, 255, 0)  # Verde
COMIDA = (255, 0, 0)  # Vermelho
VAZIO = (0, 0, 0)  # Apagado

# Variáveis do jogo
cobra = [(2, 2)]  # Começa no centro
direcao = (0, 1)  # Direção inicial (direita)
comida = (random.randint(0, 4), random.randint(0, 4))  # Posição inicial da comida
velocidade = 0.5  # Velocidade inicial (em segundos)
pontuacao = 0

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

def emitir_som(duracao, frequencia):
    """Emite um som no buzzer."""
    periodo = 1 / frequencia
    ciclos = int(frequencia * duracao)
    for _ in range(ciclos):
        buzzer.on()
        sleep(periodo / 2)
        buzzer.off()
        sleep(periodo / 2)

def mover_cobra():
    """Move a cobra na direção atual."""
    global cobra, comida, velocidade, pontuacao
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
        pontuacao += 1
        emitir_som(0.1, 500)  # Som ao comer comida
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

def atualizar_oled():
    """Atualiza a pontuação na tela OLED."""
    oled.fill(0)
    oled.text("Snake Game", 0, 0)
    oled.text(f"Score: {pontuacao}", 0, 20)
    oled.show()

def game_over():
    """Exibe mensagem de Game Over e reinicia o jogo."""
    emitir_som(0.5, 200)  # Som de Game Over
    oled.fill(0)
    oled.text("Game Over!", 20, 20)
    oled.text(f"Score: {pontuacao}", 20, 40)
    oled.show()
    sleep(2)
    # Reinicia o jogo
    global cobra, direcao, comida, velocidade, pontuacao
    cobra = [(2, 2)]
    direcao = (0, 1)
    comida = (random.randint(0, 4), random.randint(0, 4))
    velocidade = 0.5
    pontuacao = 0

# Programa principal
print("Iniciando o jogo da cobrinha!")

while True:
    desenhar()
    atualizar_direcao()
    atualizar_oled()
    if not mover_cobra():
        game_over()
    sleep(velocidade)
