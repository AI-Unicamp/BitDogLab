from machine import Pin, PWM
import time

# Conecte o alto-falante ou buzzer passivo ao pino GP4
alto_falante = PWM(Pin(4))

# Conecte o LED RGB aos pinos GP13, GP12 e GP14
led_red = PWM(Pin(13))
led_green = PWM(Pin(12))
led_blue = PWM(Pin(14))

# Frequências das notas musicais
notas = {
    'C4': 261,
    'D4': 294,
    'Eb4': 311,
    'E4': 329,
    'F4': 349,
    'Gb4': 369,
    'G4': 392,
    'Ab4': 415,
    'A4': 440,
    'Bb4': 466,
    'B4': 494,
    'C5': 523,
    'Db5': 554,
    'D5': 588,
    'Eb5': 622,
    'E5': 658,
    'F5': 698,
    'Gb5': 738,
    'G5': 784,
    'PAUSA': 0
}

# Música "Marcha Imperial"
musica = [
    ('G4', 4), ('G4', 4), ('G4', 4), ('Eb4', 3), ('Bb4', 1), ('G4', 4), ('Eb4', 3), ('Bb4', 1), ('G4', 8),
    ('D5', 4), ('D5', 4), ('D5', 4), ('Eb5', 3), ('Bb4', 1), ('Gb4', 4), ('Eb4', 3), ('Bb4', 1), ('G4', 8),
    ('G5', 4), ('G4', 3), ('G4', 1), ('G5', 4), ('Gb5', 3), ('F5', 1), ('E5', 1), ('Eb5', 1), ('E5', 2), ('PAUSA', 2), ('Ab4', 2), ('Db5', 4),
    ('C5', 3), ('B4', 1), ('Bb4', 1), ('A4', 1), ('Bb4', 2), ('PAUSA', 2), ('Eb4', 2), ('Gb4', 4), ('Eb4', 3), ('Gb4', 1), ('Bb4', 4), ('G4', 3), ('Bb4', 1), ('D5', 8)
]

def tocar_musica():
    for nota, duracao in musica:
        freq = notas[nota]
        alto_falante.freq(freq if freq > 0 else 500)
        alto_falante.duty_u16(32767 if freq > 0 else 0)
        time.sleep_ms(120 * duracao)
        alto_falante.duty_u16(0)
        time.sleep_ms(50)

while True:
		tocar_musica()
		time.sleep(2)