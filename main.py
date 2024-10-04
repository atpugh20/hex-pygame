import pygame
from board import Board
pygame.init()

sW = 600
sH = 600
screen = pygame.display.set_mode((sW, sH))
clock = pygame.time.Clock()
running = True

FPS = 60
BOARD_DIMENSION = 11

board = Board(0, 0, BOARD_DIMENSION, sW, sH)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    board.draw(screen)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
