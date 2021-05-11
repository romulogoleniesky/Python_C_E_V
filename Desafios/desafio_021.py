# Desafio 21:
from pygame import*

pygame.init()  # inicia o pygame
pygame.mixer.music.load('crazy.mp3')  # carrega o arquivo
pygame.mixer.music.play()  # inicia o arquivo
pygame.event.wait()  # espera o arquivo finalizar
