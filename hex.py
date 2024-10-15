import pygame as pg
from board import Board
from menus import match_result_menu
white = (255, 255, 255)


def hex(surface, clock, sW, sH):
    '''
    * Runs the game loop for the standard PvE Hex Game.
    '''
    running = True
    mouse_active = False
    FPS = 60
    BOARD_DIMENSION = 11
    board = Board(0, 0, BOARD_DIMENSION, sW, sH)
    user_turn = True
    cpu_turn = False
    user_color = "red"
    cpu_color = "blue"

    game_font = pg.font.Font("freesansbold.ttf", 20)

    color_text = game_font.render("Your color is: RED", True, white)
    color_rect = color_text.get_rect()
    color_rect.topleft = (25, 30)

    turn_text = game_font.render("Your turn.", True, white)
    turn_rect = turn_text.get_rect()
    turn_rect.topleft = (25, 60)

    user_score = 0
    cpu_score = 0
    sim_moves = 1000

    # Game Loop
    while running:
        winner = ""
        board.clear()
        color_text = game_font.render(f"You are: {user_color.upper()}", True, white)

        # Match Loop
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.MOUSEBUTTONUP:
                    mouse_active = True

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
                        pg.mouse.get_pressed()[0] and
                        mouse_active
                    ):
                        user_turn = False
                        cpu_turn = True
                        tile.color = user_color
            colors = [t.color for t in board.tiles]
            surface.fill("black")
            board.draw(surface)

            # Render Text
            if user_turn:
                turn_text = game_font.render("Your turn!", True, white)
            else:
                turn_text = game_font.render("Opponent chosing move...", True, white)
            surface.blit(turn_text, turn_rect)
            surface.blit(color_text, color_rect)
            pg.display.flip()

            # Check if user wins
            if board.check_winner(user_color, colors):
                winner = "user"
                user_score += 1
                break

            # CPU Turn
            if cpu_turn:
                choice = board.simulate_moves(sim_moves, cpu_color, user_color)
                board.tiles[choice].color = cpu_color
                user_turn = True
                cpu_turn = False
            colors = [t.color for t in board.tiles]
            board.draw(surface)
            pg.display.flip()

            # Check if CPU wins
            if board.check_winner(cpu_color, colors):
                winner = "cpu"
                cpu_score += 1
                break

            # Display surface and set FPS
            pg.display.flip()
            clock.tick(FPS)

        # Display match result and ask to replay
        if match_result_menu(surface, clock, sW, sH, winner,
                             user_score, cpu_score):
            running = True
            mouse_active = False
            temp = user_color
            user_color = cpu_color
            cpu_color = temp
            if user_color == "red":
                user_turn = True
                cpu_turn = False
            else:
                user_turn = False
                cpu_turn = True
        else:
            running = False
