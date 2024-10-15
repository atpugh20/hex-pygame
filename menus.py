import pygame as pg
import webbrowser as browser


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 135, 135)
blue = (135, 135, 255)
green = (135, 255, 135)


def main_menu(surface, clock, sW, sH):
    '''
    * Displays the main menu to the screen
    '''

    # Initialize font and text objects
    title_font = pg.font.Font("freesansbold.ttf", 64)
    button_font = pg.font.Font("freesansbold.ttf", 32)
    title = title_font.render("HEX", True, white)
    play = button_font.render("Play", True, white)
    quit = button_font.render("Quit", True, white)
    instructions = button_font.render("How to play (Wikipedia)", True, white)
    title_rect = title.get_rect()
    play_rect = play.get_rect()
    quit_rect = quit.get_rect()
    instructions_rect = instructions.get_rect()

    # Position text boxes
    title_rect.center = (sW // 2, sH // 3)
    play_rect.center = (sW // 2, sH * 30 // 50)
    quit_rect.center = (sW // 2, sH * 35 // 50)
    instructions_rect.center = (sW // 2, sH * 4 // 5)

    running = True

    while running:
        surface.fill("black")
        surface.blit(title, title_rect)
        surface.blit(play, play_rect)
        surface.blit(quit, quit_rect)
        surface.blit(instructions, instructions_rect)

        mouse = pg.mouse.get_pos()
        play_hover = play_rect.collidepoint(mouse)
        quit_hover = quit_rect.collidepoint(mouse)
        instructions_hover = instructions_rect.collidepoint(mouse)

        # Buttons
        if play_hover:
            play = button_font.render("Play", True, red)
        else:
            play = button_font.render("Play", True, white)
        if quit_hover:
            quit = button_font.render("Quit", True, blue)
        else:
            quit = button_font.render("Quit", True, white)

        if instructions_hover:
            instructions = button_font.render("How to play (Wikipedia)",
                                              True, green)
        else:
            instructions = button_font.render("How to play (Wikipedia)",
                                              True, white)

        # Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.MOUSEBUTTONDOWN and play_hover:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN and quit_hover:
                pg.quit()
                quit()
            elif event.type == pg.MOUSEBUTTONDOWN and instructions_hover:
                browser.open("https://en.wikipedia.org/wiki/Hex_(board_game)")

        pg.display.update()
        clock.tick(120)


def match_result_menu(surface, clock, sW, sH, winner, user_score, cpu_score):
    '''
    * Displays the results, and lets the player decide if they would like
    * to play again or return to the main menu.
    '''
    result_font = pg.font.Font("freesansbold.ttf", 64)
    button_font = pg.font.Font("freesansbold.ttf", 32)

    # Set the result string
    if winner == "user":
        r_text = "YOU WIN"
    else:
        r_text = "YOU LOSE"

    # Initialize text objects
    result = result_font.render(r_text, True, white)
    score = button_font.render(f"User: {user_score} - CPU: {cpu_score}", True, white)
    play = button_font.render("Play Again", True, white)
    quit = button_font.render("Main Menu", True, white)
    result_rect = result.get_rect()
    score_rect = score.get_rect()
    play_rect = play.get_rect()
    quit_rect = quit.get_rect()

    # Position text on screen
    result_rect.center = (sW // 2, sH // 3)
    score_rect.center = (sW // 2, sH // 2)
    play_rect.center = (sW // 2, sH * 2 // 3)
    quit_rect.center = (sW // 2, sH * 3 // 4)

    running = True

    while running:
        surface.fill("black")
        surface.blit(result, result_rect)
        surface.blit(score, score_rect)
        surface.blit(play, play_rect)
        surface.blit(quit, quit_rect)

        # Set the mouse hover boundaries
        mouse = pg.mouse.get_pos()
        play_hover = play_rect.collidepoint(mouse)
        quit_hover = quit_rect.collidepoint(mouse)

        # Change text color when hovering over
        if play_hover:
            play = button_font.render("Play Again", True, red)
        else:
            play = button_font.render("Play Again", True, white)
        if quit_hover:
            quit = button_font.render("Main Menu", True, blue)
        else:
            quit = button_font.render("Main Menu", True, white)

        # Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            # Play again
            if event.type == pg.MOUSEBUTTONDOWN and play_hover:
                return True
            # Return to main menu
            elif event.type == pg.MOUSEBUTTONDOWN and quit_hover:
                return False

        pg.display.update()
