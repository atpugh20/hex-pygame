from tile import Tile
import math as m


class Board:
    '''
    * The board contains all the tiles and methods used for gameplay
    '''

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
                                       self.tile_size,
                                       i * self.dimension + j,
                                       self.dimension))
            x_add += self.tile_size

    def draw(self, surface):
        '''
        * Draws all tiles to the surface
        '''
        for tile in self.tiles:
            tile.draw(surface)

    def clear(self):
        '''
        * Wipes the board of all pieces and sets them all as unvisited.
        '''
        for tile in self.tiles:
            tile.visited = False
            tile.color = "darkgrey"

    def filled(self):
        '''
        * Returns True if the board is full of pieces. Returns False if not.
        '''
        for tile in self.tiles:
            if not tile.filled():
                return False
        return True

    def check_winner(self, color, tiles):
        pass

    def find_path(self, color, label, tiles):
        '''
        * If there is a full path from one wall to the other, return True. If
        * not, return False. Uses recursion to check adjacent tiles.
        '''
        tile = tiles[label]

        # If the tile has the right color and is unvisited
        if tile.color == color and not tile.visited:
            tile.visited = True

            # Check if opposite wall has been reached
            if tile.color == "red" and tile.y == self.dimension - 1:
                return True
            if tile.color == "blue" and tile.x == self.dimension - 1:
                return True

            # Check adjacent nodes
            if tile.t_right != -1:
                if self.find_path(color, tile.t_right, tiles):
                    return True
            if tile.m_right != -1:
                if self.find_path(color, tile.m_right, tiles):
                    return True
            if tile.b_right != -1:
                if self.find_path(color, tile.b_right, tiles):
                    return True
            if tile.b_left != -1:
                if self.find_path(color, tile.b_left, tiles):
                    return True
            if tile.m_left != -1:
                if self.find_path(color, tile.m_left, tiles):
                    return True
            if tile.t_left != -1:
                if self.find_path(color, tile.t_left, tiles):
                    return True

        # If a path is not found
        return False
