import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((255, 0, 0))
#rect(screen, (255, 0, 255), (100, 100, 200, 200))
#rect(screen, (0, 0, 255), (100, 100, 200, 200), 5)
#polygon(screen, (255, 255, 0), [(100,100), (200,50), (300,100), (100,100)])
#polygon(screen, (0, 0, 255), [(100,100), (200,50), (300,100), (100,100)], 5)
#circle(screen, (0, 255, 0), (200, 175), 50)
#circle(screen, (255, 255, 255), (200, 175), 50, 5)
circle(screen, (0, 0, 0), (200, 200), 151)
circle(screen, (255, 255, 0), (200, 200), 150)
rect(screen, (0, 0, 0), (120, 270, 160, 40),)
circle(screen, (255, 0, 0), (130, 150), 30)
circle(screen, (0, 0, 0), (130, 150), 15)
circle(screen, (255, 0, 0), (270, 140), 24)
circle(screen, (0, 0, 0), (270, 140), 12)
polygon(screen, (0, 0, 0), [(160, 100), (170, 80), (70, 30), (60, 50)])
polygon(screen, (0, 0, 0), [(240, 100), (230, 80), (330, 30), (340, 50)])
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()