import pygame as pg
from board import Board
import random


def main():
    pg.init()

    sW = 600
    sH = 600
    screen = pg.display.set_mode((sW, sH))
    clock = pg.time.Clock()
    running = True

    FPS = 60
    BOARD_DIMENSION = 11
    board = Board(0, 0, BOARD_DIMENSION, sW, sH)
    user_turn = True
    cpu_turn = False
    user_color = "red"
    cpu_color = "blue"

    # Game Loop
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # Clear and draw board
        screen.fill("black")
        board.draw(screen)

        # User Turn
        if user_turn:
            m_pos = pg.mouse.get_pos()
            for tile in board.tiles:
                if (
                    not tile.filled() and
                    tile.hovered(m_pos[0], m_pos[1]) and
                    pg.mouse.get_pressed()[0]
                ):
                    user_turn = False
                    cpu_turn = True
                    tile.color = user_color
        if board.filled():
            board.clear()
            temp = user_color
            user_color = cpu_color
            cpu_color = temp

        # CPU Turn
        if cpu_turn:
            while True:
                choice = random.choice(board.tiles)
                if not choice.filled():
                    choice.color = cpu_color
                    user_turn = True
                    cpu_turn = False
                    break
        if board.filled():
            board.clear()
            temp = user_color
            user_color = cpu_color
            cpu_color = temp

        # Display surface and set FPS
        pg.display.flip()
        clock.tick(FPS)

    # End game after the game loop ends
    pg.quit()


if __name__ == "__main__":
    main()
