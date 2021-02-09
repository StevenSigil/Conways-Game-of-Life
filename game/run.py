import pygame
import numpy as np
import life_logic

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)

WINDOW_SIZE = 480, 480

MARGIN = 1  # Visual spacing between cells

# Board dimensions
h = 80 	# 120 XL	# 80 LG 	# 60 MD 	# 40 SM
w = 80	# 120 XL	# 80 LG 	# 60 MD 	# 40 SM

grid = np.zeros([h, w], int)

life_logic.setup_random(grid)  # Random starting values - Comment out if you want a blank canvas

# Initialize pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Conway's Game of Life")

cell_width = (WINDOW_SIZE[1] // grid.shape[1]) - MARGIN
cell_height = WINDOW_SIZE[0] // grid.shape[0] - MARGIN

# Set the clock
clock = pygame.time.Clock()

# Controllers
playing = False
start = True

# First loop - Draw cells on the board (or use random)
dragging = False
while start:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            # Closing the first window starts the 'playing' loop
            start = False
            playing = False

        elif event.type == pygame.KEYDOWN:
            # Pressing a key will break and exit
            start = False
            playing = False
            pygame.quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Click cells in window
            try:
                dragging = True
                mouse_x, mouse_y = event.pos
                w_cord = mouse_y // (cell_width + MARGIN)
                h_cord = mouse_x // (cell_height + MARGIN)
                grid[w_cord][h_cord] = 1
            except IndexError:
                # Mouse goes out of window
                pass

        elif event.type == pygame.MOUSEMOTION:
            # Draw cells in window
            try:
                if dragging:
                    mouse_x, mouse_y = event.pos
                    w_cord = mouse_y // (cell_width + MARGIN)
                    h_cord = mouse_x // (cell_height + MARGIN)
                    grid[w_cord][h_cord] = 1
            except IndexError:
                pass

        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False

    # Window background
    screen.fill(WHITE)	# Change to GRAY for visible grid

    # Draw board and cell values
    for row in range(0, grid.shape[1]):
        for column in range(0, grid.shape[0]):
            if grid[row][column] == 0:
                color = WHITE
            elif grid[row][column] == 1:
                color = BLACK
            a = (cell_width * column + MARGIN) + (MARGIN * column)
            b = (cell_height * row + MARGIN) + (MARGIN * row)
            c = cell_width
            d = cell_height

            pygame.draw.rect(screen, color, [a, b, c, d])

    pygame.display.flip()
    clock.tick()

playing = True
start = False

# Second (playing) Loop
while playing:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            # Breaks loop
            playing = False

        elif event.type == pygame.KEYDOWN:
            pygame.quit()

    # Background
    screen.fill(WHITE)

    grid = life_logic.update_grid(grid)

    # Draw visual elements on screen from 'grid'
    for row in range(0, grid.shape[1]):
        for column in range(0, grid.shape[0]):
            if grid[row][column] == 0:
                color = WHITE
            elif grid[row][column] == 1:
                color = BLACK

            a = (cell_width * column + MARGIN) + (MARGIN * column)
            b = (cell_height * row + MARGIN) + (MARGIN * row)
            c = cell_width
            d = cell_height

            pygame.draw.rect(screen, color, [a, b, c, d])

    # Update Screen with drawn
    pygame.display.flip()

    # Documentation makes it sound like using clock.tick(n) is preferred. However, using time.delay(Ms) seems to be
    # much easier on the CPU and visually smoother.
    pygame.time.delay(10)

# On loop break
pygame.quit()
