from machine import Pin, I2C, ADC
from neopixel import NeoPixel
import time
from random import randint

np = NeoPixel(Pin(7), 25)
np.fill((0, 0, 0))
np.write()

LEDS = [
    [4, 3, 2, 1, 0],
    [5, 6, 7, 8, 9],
    [14, 13, 12, 11, 10],
    [15, 16, 17, 18, 19],
    [24, 23, 22, 21, 20]
]

def npLed(pos: tuple[int, int], rgb: tuple[int, int, int], update: bool = False):
    if not (0 <= pos[0] <= 4 and 0 <= pos[1] <= 4):
        return
    global np, LEDS
    x, y = pos
    index = LEDS[y][x]
    np[index] = rgb
    if update:
        np.write()

vrx = ADC(Pin(27))
vry = ADC(Pin(26))
sw = Pin(22, Pin.IN, Pin.PULL_UP)

COLORS = {
    'player': (0, 0, 40),
    'fruit': (40, 0, 0),
    'gold fruit': (40, 40, 0),
    'collecting': (40, 0, 40)
}

fruits = []
def createFruit():
    global fruits
    is_golden = (randint(1, 10) == 10) # 10% golden fruit
    fruits.append(
        {
            'type': 'gold fruit' if is_golden else 'fruit',
            'value': 50 if is_golden else 10,
            'pos': [randint(0, 4), 5]
        }
    )


contador = 0
score = 0
player_x = vrx.read_u16() // 13107
while True:
    # Fruta desce a cada segundo
    fruits_at_zero = []
    if contador % 20 == 0:
        expired = []
        for i, f in enumerate(fruits):
            npLed(f['pos'], (0, 0, 0))
            f['pos'][1] -= 1
            if f['pos'][1] == 0:
                fruits_at_zero.append((i, f['pos'][0]))
            if f['pos'][1] < 0:
                expired.append(i)
            else:
                npLed(f['pos'], COLORS[f['type']])
        for i in reversed(expired):
            fruits.pop(i)
        createFruit()
        print(fruits)
    
    # Jogador se move a cada 1/5 de segundo
    if contador % 2 == 0:
        is_collecting = False
        npLed((player_x, 0), (0, 0, 0))
        player_x = vrx.read_u16() // 13107
        for i, x in fruits_at_zero:
            if player_x == x:
                is_collecting = True
                score += fruits[i]['value']
                fruits.pop(i)
                break
        npLed((player_x, 0), COLORS['collecting' if is_collecting else 'player'], True)
    
    time.sleep_ms(50)
    contador += 1