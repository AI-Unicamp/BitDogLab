# Toca "Hello World!" no buzzer passivo em código Morse
from machine import Pin, PWM
import utime

# Configuração do Buzzer
buzzer = PWM(Pin(21))

# Tabela Morse
MORSE_CODE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--..", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    "0": "-----", " ": "/"
}

# Configurações de tempo (em segundos)
DOT_DURATION = 0.2  # Duração de um ponto (.)
DASH_DURATION = DOT_DURATION * 3  # Duração de um traço (-)
LETTER_PAUSE = DOT_DURATION * 3  # Pausa entre letras
WORD_PAUSE = DOT_DURATION * 7  # Pausa entre palavras

def beep(duration):
    """Emite um som no buzzer por um tempo especificado."""
    buzzer.freq(1000)  # Frequência do som
    buzzer.duty_u16(3000)  # Volume médio
    utime.sleep(duration)
    buzzer.duty_u16(0)  # Para o som
    utime.sleep(DOT_DURATION)  # Pequena pausa após o som

def tocar_morse(mensagem):
    """Converte uma mensagem para código Morse e a toca no buzzer."""
    for letra in mensagem.upper():
        if letra in MORSE_CODE:
            codigo = MORSE_CODE[letra]
            print(f"{letra}: {codigo}")
            for simbolo in codigo:
                if simbolo == ".":
                    beep(DOT_DURATION)  # Toca um ponto
                elif simbolo == "-":
                    beep(DASH_DURATION)  # Toca um traço
                utime.sleep(DOT_DURATION)  # Pausa entre símbolos
            utime.sleep(LETTER_PAUSE - DOT_DURATION)  # Pausa entre letras
        elif letra == " ":
            utime.sleep(WORD_PAUSE)  # Pausa entre palavras

# Mensagem a ser tocada
mensagem = "Hello World"
print(f"Tocando mensagem: {mensagem}")
tocar_morse(mensagem)
