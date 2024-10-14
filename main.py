import pygame as pg
from hex import hex
import menus

def main():
    pg.init()
    pg.display.set_caption("Hex")

    sW = 600
    sH = 600
    screen = pg.display.set_mode((sW, sH))
    clock = pg.time.Clock()

    menus.match_result_menu(screen,clock, sW, sH, "user", 0, 0)
    menus.main_menu(screen, clock, sW, sH)
    hex(screen, clock, sW, sH)

    pg.quit()


if __name__ == "__main__":
    main()
