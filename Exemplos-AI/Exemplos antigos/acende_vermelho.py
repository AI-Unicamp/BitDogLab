# Acende LED RGB principal na cor vermelha

from machine import Pin

# Configuração do GPIO para o canal vermelho do LED RGB
led_vermelho = Pin(13, Pin.OUT)

# Acende o LED na cor vermelha
led_vermelho.value(1)
