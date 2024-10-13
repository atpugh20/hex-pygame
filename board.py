from tile import Tile
import random
import math as m
import numpy as np


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
        self.empty_color = "darkgrey"
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
                                       self.dimension,
                                       self.empty_color))
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
            tile.color = self.empty_color

    def filled(self):
        '''
        * Returns True if the board is full of pieces. Returns False if not.
        '''
        for tile in self.tiles:
            if not tile.filled():
                return False
        return True

    def check_winner(self, color, tile_colors):
        '''
        * Uses the color's starting wall to find a path to the opposite wall.
        '''
        interval = 1
        if color == "blue":
            interval = self.dimension

        # Visit and color initialize
        visited = [False] * len(self.tiles)

        # Begin checking from the color's start wall
        for i in range(0, interval * self.dimension, interval):
            if self.find_path(color, i, tile_colors, visited):
                return True
        return False

    def find_path(self, color, label, tile_colors, visited):
        '''
        * If there is a full path from one wall to the other, return True. If
        * not, return False. Uses recursion to check adjacent tiles.
        '''
        # If the tile has the right color and is unvisited
        if tile_colors[label] == color and not visited[label]:
            visited[label] = True

            # Check if opposite wall has been reached
            if tile_colors[label] == "red" and label // self.dimension == self.dimension - 1:
                return True
            if tile_colors[label] == "blue" and label % self.dimension == self.dimension - 1:
                return True

            # Check adjacent nodes
            if self.tiles[label].t_right != -1:
                if self.find_path(color, self.tiles[label].t_right, tile_colors, visited):
                    return True
            if self.tiles[label].m_right != -1:
                if self.find_path(color, self.tiles[label].m_right, tile_colors, visited):
                    return True
            if self.tiles[label].b_right != -1:
                if self.find_path(color, self.tiles[label].b_right, tile_colors, visited):
                    return True
            if self.tiles[label].b_left != -1:
                if self.find_path(color, self.tiles[label].b_left, tile_colors, visited):
                    return True
            if self.tiles[label].m_left != -1:
                if self.find_path(color, self.tiles[label].m_left, tile_colors, visited):
                    return True
            if self.tiles[label].t_left != -1:
                if self.find_path(color, self.tiles[label].t_left, tile_colors, visited):
                    return True

        # If a path is not found
        return False

    def simulate_moves(self, sim_num, current_color, other_color):
        '''
        * Simulates 'sim_num' matches for each move that can be made on the
        * current turn. Returns the tile label with the most simulated wins.
        * The larger 'sim_num' is, the better the move will be. This is used
        * to determine the next move for the CPU.
        '''
        rates = [0] * len(self.tiles)
        empty_tiles = -1
        first_color = current_color
        colors = np.array([tile.color for tile in self.tiles])

        # Get number of empty tiles
        for t in self.tiles:
            if t.color == self.empty_color:
                empty_tiles += 1
        # Runs simulations with every possible move that can be made
        for i in range(len(self.tiles)):
            # If the current tile is not empty, move to next
            if colors[i] != self.empty_color:
                continue
            wins = 0

            # Simulate 'sim_num' matches with the move
            for j in range(sim_num):
                sim_colors = colors.copy() 
                sim_colors[i] = current_color               
                # Randomly fill in every space, alternating colors
                for k in range(empty_tiles):
                    # Randomly fill empty space
                    while True:
                        r_index = random.randint(0, len(self.tiles) - 1)
                        if sim_colors[r_index] == self.empty_color:
                            sim_colors[r_index] = current_color
                            break

                    # Alternate colors
                    temp = current_color
                    current_color = other_color
                    other_color = temp

                # Increment over wins when the player wins with the move
                if self.check_winner(first_color, sim_colors):
                    wins += 1
            rates[i] = wins

        # Return the move with the most simulated wins
        biggest = 0
        biggest_index = 0
        for i in range(len(rates)):
            if rates[i] > biggest:
                biggest = rates[i]
                biggest_index = i
        return biggest_index
