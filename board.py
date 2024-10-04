from tile import Tile
import math as m


class Board:
    def __init__(self, x, y, dimension, sW, sH):
        self.x = x
        self.y = y
        self.dimension = dimension

        self.sW = sW
        self.sH = sH
        self.sE = self.sH if self.sH < self.sW else self.sW  # Smaller edge

        self.tile_size = self.sE / self.dimension / 3
        self.board_height = 2 * self.tile_size * self.dimension
        self.board_width = self.board_height + 2 * self.tile_size * m.floor(self.dimension / 2)

        self.tiles = []
        self.fill_tiles()

    def fill_tiles(self):
        '''
        * Initializes all tiles and sets their x and y coordinates
        '''
        x_shift = (self.sW - self.board_width) / 2
        y_shift = (self.sH - self.board_height) / 2
        x_add = self.tile_size + x_shift
        y_add = self.tile_size + y_shift

        for i in range(self.dimension):
            for j in range(self.dimension):
                self.tiles.append(Tile(self.x + x_add + self.tile_size * j * 2,
                                       self.y + y_add + self.tile_size * i * 1.75,
                                       self.tile_size))
            x_add += self.tile_size

    def draw(self, surface):
        '''
        * Draws all tiles to the surface
        '''
        for tile in self.tiles:
            tile.draw(surface)
