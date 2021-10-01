import pygame
pygame.init()

som = pygame.mixer.Sound('mission.wav')
som.play(-1)
som.set_volume(1)
