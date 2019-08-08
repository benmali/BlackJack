import pygame
import time
(width, height) = (1000, 700)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('BlackJack')
running = True

background_colour = (255,255,255)
screen.fill(background_colour)
while running:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False