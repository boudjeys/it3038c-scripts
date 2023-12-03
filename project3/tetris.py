# Tetris Game
# Yanis Boudjema IT3038C Project 3
# Coded following TokyoEdtech tutorial on YouTube (https://www.youtube.com/watch?v=JuMqaU_664k)
# Coded following FreecodeCamp.org https://www.youtube.com/watch?app=desktop&v=zfvxp7PgQ6c
# Uses Python 3, pygame, and random Module

import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 600
GRID_SIZE = 30
GRID_WIDTH, GRID_HEIGHT = WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE
BLACK = (0, 0, 0)
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
]

# Initialize game variables
grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
current_piece = None
score = 0

# Pygame setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

# Pygame font setup
font = pygame.font.Font(None, 36)

# Function to draw the grid with random colored circles
def draw_grid():
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell:
                color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
                pygame.draw.circle(screen, color, (x * GRID_SIZE + GRID_SIZE // 2, y * GRID_SIZE + GRID_SIZE // 2), GRID_SIZE // 2)
                pygame.draw.circle(screen, BLACK, (x * GRID_SIZE + GRID_SIZE // 2, y * GRID_SIZE + GRID_SIZE // 2), GRID_SIZE // 2, 2)

# Function to draw the current piece as circles
def draw_piece():
    for y, row in enumerate(current_piece):
        for x, cell in enumerate(row):
            if cell:
                color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
                pygame.draw.circle(screen, color, ((current_x + x) * GRID_SIZE + GRID_SIZE // 2, (current_y + y) * GRID_SIZE + GRID_SIZE // 2), GRID_SIZE // 2)
                pygame.draw.circle(screen, BLACK, ((current_x + x) * GRID_SIZE + GRID_SIZE // 2, (current_y + y) * GRID_SIZE + GRID_SIZE // 2), GRID_SIZE // 2, 2)

# Function to draw the score
def draw_score():
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

# Function to draw the game over screen
def draw_game_over():
    game_over_text = font.render("Game Over", True, (255, 255, 255))
    screen.blit(game_over_text, (WIDTH // 2 - 70, HEIGHT // 2 - 20))
    score_text = font.render(f"Your Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (WIDTH // 2 - 85, HEIGHT // 2 + 20))

# Function to check if a piece can be placed in the current position
def can_place_piece(piece, x, y):
    for i, row in enumerate(piece):
        for j, cell in enumerate(row):
            if (
                cell
                and (
                    y + i >= GRID_HEIGHT
                    or x + j < 0
                    or x + j >= GRID_WIDTH
                    or y + i >= 0 and grid[y + i][x + j]
                )
            ):
                return False
    return True

# Function to place the current piece in the grid
def place_piece(piece, x, y):
    for i, row in enumerate(piece):
        for j, cell in enumerate(row):
            if cell:
                grid[y + i][x + j] = 1

# Function to check and clear lines
def check_and_clear_lines():
    global score
    lines_to_clear = [i for i, row in enumerate(grid) if all(row)]
    for line in lines_to_clear:
        del grid[line]
        grid.insert(0, [0] * GRID_WIDTH)
        score += 100 * len(lines_to_clear)

# Main game loop
running = True
current_x, current_y = 0, 0
current_piece = random.choice(SHAPES)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and can_place_piece(current_piece, current_x - 1, current_y):
                current_x -= 1
            elif event.key == pygame.K_RIGHT and can_place_piece(current_piece, current_x + 1, current_y):
                current_x += 1
            elif event.key == pygame.K_DOWN and can_place_piece(current_piece, current_x, current_y + 1):
                current_y += 1
            elif event.key == pygame.K_SPACE:
                rotated_piece = list(zip(*reversed(current_piece)))
                if can_place_piece(rotated_piece, current_x, current_y):
                    current_piece = rotated_piece

    # Move the piece down
    if can_place_piece(current_piece, current_x, current_y + 1):
        current_y += 1
    else:
        place_piece(current_piece, current_x, current_y)
        check_and_clear_lines()
        current_x, current_y = 0, 0
        current_piece = random.choice(SHAPES)

        # Check for game over condition
        if not can_place_piece(current_piece, current_x, current_y):
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Draw the grid and piece with random colored circles
    draw_grid()
    draw_piece()

    # Draw the score
    draw_score()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(5)

# Display game over screen
draw_game_over()
pygame.display.flip()

# Wait for a few seconds before quitting
pygame.time.wait(3000)

pygame.quit()
