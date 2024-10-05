import pygame
import math as m


class Tile:
    def __init__(self, x, y, size, label):
        # Game Logic Attributes
        self.label = label
        self.t_r = -1
        self.m_r = -1
        self.b_r = -1
        self.b_l = -1
        self.m_l = -1
        self.t_l = -1

        # Visual Attributes
        self.x = x
        self.y = y
        self.color = "darkgrey"
        self.size = size
        self.alt_size = m.sqrt(self.size**2 - (self.size * 0.5)**2)
        self.half_size = self.size * 0.5

        self.points = [
            [x, y - self.size],
            [x + self.alt_size, y - self.half_size],
            [x + self.alt_size, y + self.half_size],
            [x, y + self.size],
            [x - self.alt_size, y + self.half_size],
            [x - self.alt_size, y - self.half_size]
        ]

    def draw(self, surface):
        '''
        * Draws the tile to the surface using 'points' and 'color'
        '''
        pygame.draw.polygon(surface, self.color, self.points, 0)
        pygame.draw.polygon(surface, "white", self.points, 2)
