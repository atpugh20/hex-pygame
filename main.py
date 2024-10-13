import cython
import pygame as pg
from hex import hex

@cython.boundscheck(True)

def main():
    pg.init()

    sW = 600
    sH = 600
    screen = pg.display.set_mode((sW, sH))
    clock = pg.time.Clock()

    hex(screen, clock, sW, sH)

    pg.quit()


if __name__ == "__main__":
    main()
