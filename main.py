import pygame as pg
from hex import hex
from menus import main_menu


def main():
    pg.init()
    pg.display.set_caption("Hex")

    sW = 800
    sH = 600
    screen = pg.display.set_mode((sW, sH))
    clock = pg.time.Clock()

    while True:
        main_menu(screen, clock, sW, sH)
        hex(screen, clock, sW, sH)

    pg.quit()


if __name__ == "__main__":
    main()
