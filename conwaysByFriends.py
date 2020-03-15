#! python3
# conwaysByFriends.py - Game of life

# 1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# 2. Any live cell with two or three live neighbours lives on to the next generation.
# 3. Any live cell with more than three live neighbours dies, as if by overpopulation.
# 4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
from os import system, name 
import random
import numpy as np
import time

def get_neighbours(x, y):
    live_neighbour = []
    dead_neighbour = []

    for i in range(x - 1, x + 1 + 1):
        for j in range(y - 1, y + 1 + 1):
            if (i,j) != (x,y):
                if (i, j) in live_cells:
                    live_neighbour.append((i, j))
                elif 0 <= i <= size-1 and 0 <= j <= size-1: 
                    dead_neighbour.append((i, j))

    # print(f"Live neighbours for {x}, {y}: {live_neighbour}")

    return live_neighbour, dead_neighbour


live_cells = []
size = 17

initial_live_cells = 20

initial_population_x = random.choices(list(range(size)), k=initial_live_cells)
initial_population_y = random.choices(list(range(size)), k=initial_live_cells)

for i in range(initial_live_cells):
    live_cells.append((initial_population_x[i], initial_population_y[i]))

live_cells = [
    (2, 4), (2, 5), (2, 6), (2, 10), (2, 11), (2, 12),
    (7, 4), (7, 5), (7, 6), (7, 10), (7, 11), (7, 12),
    (9, 4), (9, 5), (9, 6), (9, 10), (9, 11), (9, 12),
    (14, 4), (14, 5), (14, 6), (14, 10), (14, 11), (14, 12),
   
    (4, 2), (5, 2), (6, 2), (10, 2), (11, 2), (12, 2),  
    (4, 7), (5, 7), (6, 7), (10, 7), (11, 7), (12, 7),  
    (4, 9), (5, 9), (6, 9), (10, 9), (11, 9), (12, 9),  
    (4, 14), (5, 14), (6, 14), (10, 14), (11, 14), (12, 14)  
            ]

while True:

    matrix = np.full((size, size), ' ')

    for i, j in live_cells:
        matrix[j, i] = 'O'

    system('cls') 
    print(matrix)

    live_cells_next = []
    dead_cells = set()
    for x, y in live_cells:
        live, dead = get_neighbours(x, y)
        if len(live)==2 or len(live)==3:
            live_cells_next.append((x, y))

        dead_cells = dead_cells.union(set(dead))

    for x, y in dead_cells:

        live, _ = get_neighbours(x, y)

        if len(live) == 3:
            live_cells_next.append((x, y))

    live_cells = live_cells_next
    time.sleep(1)
