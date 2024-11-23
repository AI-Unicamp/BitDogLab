''' 
    Código para testar contagem dos botões A e B
    Se apertar o Botão A, acende um LED Vermelho no painel
    Se apertar o Botão B, acende um LED Azul no painel
    Acende da esquerda para a direita de cima para baixo
    
    Ao pressionar o botão A, um LED vermelho é aceso no próximo índice disponível.
    O LED vermelho segue o mapeamento da matriz (esquerda para direita, de cima para baixo).
    Quando o último LED é aceso, o programa reinicia a matriz.
    
    Ao pressionar o botão B, o próximo LED é aceso em azul.
    Assim como no botão A, o programa segue o mapeamento e reseta ao final.

    Quando todos os 25 LEDs forem acesos, o índice é reiniciado, e todos os LEDs são apagados antes de continuar.
'''


from machine import Pin
import neopixel
from utime import sleep

# Configurações da matriz de LEDs
NUM_LEDS = 25  # Total de LEDs na matriz 5x5
PIN = 7  # Pino onde a matriz Neopixel está conectada
np = neopixel.NeoPixel(Pin(PIN), NUM_LEDS)

# Mapeamento da matriz de LEDs com a origem no canto superior esquerdo
LED_MATRIX = [
    [0, 1, 2, 3, 4],
    [5, 6, 7, 8, 9],
    [10, 11, 12, 13, 14],
    [15, 16, 17, 18, 19],
    [20, 21, 22, 23, 24]
]

# Configuração dos botões
botao_a = Pin(11, Pin.IN, Pin.PULL_UP)  # Botão A (com pull-up interno)
botao_b = Pin(12, Pin.IN, Pin.PULL_UP)  # Botão B (com pull-up interno)

# Variável para controlar o índice atual na matriz
led_index = 0

# Função para apagar todos os LEDs
def apagar():
    np.fill((0, 0, 0))  # Todos os LEDs desligados
    np.write()

# Função para acender o próximo LED
def acender_proximo(cor):
    global led_index
    if led_index < NUM_LEDS:
        np[led_index] = cor  # Define a cor do LED atual
        np.write()
        led_index += 1  # Avança para o próximo LED
    else:
        led_index = 0  # Reseta a contagem
        apagar()  # Apaga todos os LEDs

# Programa principal
print("Pressione Botão A para vermelho, Botão B para azul.")

while True:
    if not botao_a.value():  # Botão A pressionado
        acender_proximo((255, 0, 0))  # LED vermelho
        sleep(0.2)  # Debounce para evitar múltiplos cliques rápidos

    if not botao_b.value():  # Botão B pressionado
        acender_proximo((0, 0, 255))  # LED azul
        sleep(0.2)  # Debounce para evitar múltiplos cliques rápidos
