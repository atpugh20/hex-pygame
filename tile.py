import pygame
import math as m


class Tile:
    '''
    * A tile is a singular space on the board. It can be filled in with a
    * color. The color indicates which player put the piece on the tile.
    '''

    def __init__(self, x, y, size, label, dimension):
        # Game Logic Attributes
        self.label = label
        self.visited = False
        self.dimension = dimension

        # Adjacent Tile Labels
        self.t_right = -1
        self.m_right = -1
        self.b_right = -1
        self.b_left = -1
        self.m_left = -1
        self.t_left = -1
        self.connect_tiles()

        # Visual Attributes
        self.x = x
        self.y = y
        self.color = "darkgrey"
        self.size = size
        self.alt_size = m.sqrt(self.size**2 - (self.size * 0.5)**2)
        self.half_size = self.size * 0.5

        # Tile Vertices
        self.points = [
            [x, y - self.size],
            [x + self.alt_size, y - self.half_size],
            [x + self.alt_size, y + self.half_size],
            [x, y + self.size],
            [x - self.alt_size, y + self.half_size],
            [x - self.alt_size, y - self.half_size]
        ]

    def connect_tiles(self):
        '''
        * Sets all of the adjacent tiles to their proper labels.
        '''
        # Top Right
        if (
            self.label % self.dimension != self.dimension - 1 and
            self.label // self.dimension > 0
        ):
            self.t_right = self.label - self.dimension + 1
        # Middle Right
        if self.label % self.dimension != self.dimension - 1:
            self.m_right = self.label + 1
        # Bottom Right
        if self.label // self.dimension < self.dimension - 1:
            self.b_right = self.label + self.dimension
        # Bottom Left
        if (
            self.label % self.dimension != 0 and
            self.label // self.dimension < self.dimension - 1
        ):
            self.b_left = self.label + self.dimension - 1
        # Middle Left
        if self.label % self.dimension != 0:
            self.m_left = self.label - 1
        # Top Left
        if self.label // self.dimension > 0:
            self.t_left = self.label - self.dimension

    def draw(self, surface):
        '''
        * Draws the tile to the surface using 'points' and 'color'.
        '''
        pygame.draw.polygon(surface, self.color, self.points, 0)
        pygame.draw.polygon(surface, "white", self.points, 2)

    def filled(self):
        '''
        * Returns true if a player has filled this tile. False if not.
        '''
        if self.color == "red" or self.color == "blue":
            return True
        return False

    def hovered(self, mouse_x, mouse_y):
        '''
        * If the tile is hovered, returns True. If not, returns False.
        '''
        x_diff = (mouse_x - self.x) ** 2
        y_diff = (mouse_y - self.y) ** 2
        distance = m.sqrt(x_diff + y_diff)
        if distance < self.size:
            self.color = "black"
            return True
        else:
            self.color = "darkgrey"
            return False
