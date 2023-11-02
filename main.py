import pygame
import random


pygame.init()
x_limit = 1200
y_limit = 800
screen = pygame.display.set_mode((x_limit, y_limit))
pygame.display.set_caption("The Best Game Ever")

running = True

x_coordinate = 500
y_coordinate = 300
move_sensitivity = 50

while running == True:
    for event in pygame.event.get():
        pygame.draw.rect(screen, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (x_coordinate, y_coordinate, 50, 50))
        if event.type == pygame.QUIT:
            break


    print(x_coordinate, y_coordinate)
    button = pygame.key.get_pressed()

    if button[pygame.K_LEFT]:
        x_coordinate += -move_sensitivity

    if button[pygame.K_RIGHT]:
        x_coordinate += move_sensitivity

    if button[pygame.K_UP]:
        y_coordinate += -move_sensitivity

    if button[pygame.K_DOWN]:
        y_coordinate += move_sensitivity

    if x_coordinate < 0:
        x_coordinate = 0

    if x_coordinate > x_limit:
        x_coordinate = x_limit

    if y_coordinate < 0:
        y_coordinate = 0

    if y_coordinate > y_limit:
        y_coordinate = y_limit

    pygame.time.Clock().tick(5)


    pygame.display.flip()