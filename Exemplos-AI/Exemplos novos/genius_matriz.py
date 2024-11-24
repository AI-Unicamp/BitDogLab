Cada "quadrante" da matriz representará uma cor:
Vermelho (quadrante superior esquerdo).
Azul (quadrante superior direito).
Verde (quadrante inferior esquerdo).
Amarelo (quadrante inferior direito).

Botão A e Botão B serão usados para reproduzir a sequência. A escolha de cores pode ser feita usando os botões em combinação ou em diferentes pressões.

A matriz acenderá LEDs indicando sucesso ou erro:
Verde para acerto.
Vermelho para erro.

from machine import Pin
import neopixel
from utime import sleep
import random

# Configurações da matriz de LEDs
NUM_LEDS = 25  # Total de LEDs na matriz 5x5
PIN = 7  # Pino onde a matriz Neopixel está conectada
np = neopixel.NeoPixel(Pin(PIN), NUM_LEDS)

# Configuração dos botões
botao_a = Pin(11, Pin.IN, Pin.PULL_UP)  # Botão A (com pull-up interno)
botao_b = Pin(12, Pin.IN, Pin.PULL_UP)  # Botão B (com pull-up interno)

# Definição de cores e quadrantes
CORES = {
    "vermelho": (255, 0, 0),
    "azul": (0, 0, 255),
    "verde": (0, 255, 0),
    "amarelo": (255, 255, 0)
}

# Quadrantes
QUADRANTES = {
    "vermelho": [0, 1, 5, 6],
    "azul": [3, 4, 8, 9],
    "verde": [15, 16, 20, 21],
    "amarelo": [18, 19, 23, 24]
}

# Funções auxiliares
def apagar():
    """Apaga todos os LEDs."""
    np.fill((0, 0, 0))
    np.write()

def acender_cor(cor):
    """Acende LEDs de um quadrante na cor especificada."""
    apagar()
    for led in QUADRANTES[cor]:
        np[led] = CORES[cor]
    np.write()
    sleep(0.5)
    apagar()
    sleep(0.2)

def feedback(correto):
    """Feedback visual: verde para acerto, vermelho para erro."""
    cor = (0, 255, 0) if correto else (255, 0, 0)
    np.fill(cor)
    np.write()
    sleep(1)
    apagar()

def ler_botao():
    """Lê a entrada do jogador e retorna a cor correspondente."""
    while True:
        if not botao_a.value() and not botao_b.value():
            return "amarelo"  # Ambos pressionados
        elif not botao_a.value():
            return "vermelho"
        elif not botao_b.value():
            return "azul"

# Programa principal
print("Iniciando o jogo Genius. Siga a sequência de cores!")

sequencia = []  # Sequência de cores a ser memorizada
rodando = True

while rodando:
    # Adiciona uma nova cor aleatória à sequência
    nova_cor = random.choice(list(CORES.keys()))
    sequencia.append(nova_cor)

    # Exibe a sequência na matriz
    for cor in sequencia:
        acender_cor(cor)

    # Entrada do jogador
    for cor_esperada in sequencia:
        entrada = ler_botao()
        acender_cor(entrada)

        if entrada != cor_esperada:
            feedback(False)  # Erro
            print("Você perdeu!")
            rodando = False
            break
    else:
        feedback(True)  # Acerto

    # Pequena pausa entre as rodadas
    sleep(1)
