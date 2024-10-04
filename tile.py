import pygame
import math as m


class Tile:
    def __init__(self, x, y, size):
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
        pygame.draw.polygon(surface, self.color, self.points, 0)
        pygame.draw.polygon(surface, "white", self.points, 2)
