import pygame as pg


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 135, 135)
blue = (135, 135, 255)

def main_menu(surface, clock, sW, sH):
    '''
    * Displays the main menu to the screen
    '''    
    title_font = pg.font.Font("freesansbold.ttf", 64)
    button_font = pg.font.Font("freesansbold.ttf", 32)

    title = title_font.render("HEX", True, white)
    play = button_font.render("Play", True, white)
    quit = button_font.render("Quit", True, white)

    title_rect = title.get_rect()
    play_rect = play.get_rect()
    quit_rect = quit.get_rect()

    title_rect.center = (sW // 2, sH // 3)
    play_rect.center = (sW // 2, sH * 28 // 50)
    quit_rect.center = (sW // 2, sH * 2 // 3)

    running = True

    while running:
        surface.fill("black")
        surface.blit(title, title_rect)
        surface.blit(play, play_rect)
        surface.blit(quit, quit_rect)

        mouse = pg.mouse.get_pos()
        play_hover = play_rect.collidepoint(mouse)
        quit_hover = quit_rect.collidepoint(mouse)        

        # Buttons
        if play_hover:
            play = button_font.render("Play", True, red)
        else:
            play = button_font.render("Play", True, white)
        if quit_hover:
            quit = button_font.render("Quit", True, blue)
        else:
            quit = button_font.render("Quit", True, white)

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

        pg.display.update()
        clock.tick(120)


def match_result_menu(surface, clock, sW, sH, winner, user_score, cpu_score):
    '''
    * Displays the results, and lets the player decide if they would like
    * to play again.
    '''
    result_font = pg.font.Font("freesansbold.ttf", 64)
    button_font = pg.font.Font("freesansbold.ttf", 32)

    if winner == "user":
        r_text = "YOU WIN"
    else:
        r_text = "YOU LOSE"

    result = result_font.render(r_text, True, white)
    score = button_font.render(f"User: {user_score} - CPU: {cpu_score}", True, white)
    play = button_font.render("Play again", True, white)
    quit = button_font.render("Quit", True, white)

    result_rect = result.get_rect()
    score_rect = score.get_rect()
    play_rect = play.get_rect()
    quit_rect = quit.get_rect()

    result_rect.center = (sW // 2, sH // 3)
    score_rect.center = (sW // 2, sH // 2)
    play_rect.center = (sW // 2, sH * 30 // 50)
    quit_rect.center = (sW // 2, sH * 2 // 3)

    running = True

    while running:
        surface.fill("black")
        surface.blit(result, result_rect)
        surface.blit(score, score_rect)
        surface.blit(play, play_rect)
        surface.blit(quit, quit_rect)

        mouse = pg.mouse.get_pos()
        play_hover = play_rect.collidepoint(mouse)
        quit_hover = quit_rect.collidepoint(mouse)        

        # Buttons
        if play_hover:
            play = button_font.render("Play", True, red)
        else:
            play = button_font.render("Play", True, white)
        if quit_hover:
            quit = button_font.render("Quit", True, blue)
        else:
            quit = button_font.render("Quit", True, white)

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

        pg.display.update()
     
