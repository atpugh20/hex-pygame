import pygame as pg
from board import Board
import random


def hex(surface, clock, sW, sH):
    '''
    * Runs the game loop for the standard PvE Hex Game.
    '''
    running = True
    FPS = 60
    BOARD_DIMENSION = 11
    board = Board(0, 0, BOARD_DIMENSION, sW, sH)
    user_turn = True
    cpu_turn = False
    user_color = "red"
    cpu_color = "blue"

    sim_moves = 100

    # Game Loop
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # Clear and draw board
        surface.fill("black")
        board.draw(surface)

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
        if board.check_winner(user_color, board.tiles):
            board.clear()
            temp = user_color
            user_color = cpu_color
            cpu_color = temp

        # CPU Turn
        if cpu_turn:
            choice = board.simulate_moves(sim_moves, cpu_color, user_color)
            board.tiles[choice].color = cpu_color
            user_turn = True
            cpu_turn = False
        if board.check_winner(cpu_color, board.tiles):
            board.clear()
            temp = user_color
            user_color = cpu_color
            cpu_color = temp

        # Display surface and set FPS
        pg.display.flip()
        clock.tick(FPS)
