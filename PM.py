import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 620, 580  # Adjusted for the size of the maze
BACKGROUND_COLOR = (0, 0, 0)
WALL_COLOR = (0, 0, 255)
DOT_COLOR = (255, 200, 200)
PACMAN_COLOR = (255, 255, 0)
FPS = 10  # Frame rate

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pacman Game")
clock = pygame.time.Clock()

# Define the maze layout
maze = [
    "##############################",
    "#............##............#",
    "#.####.#####.##.#####.####.#",
    "#o####.#####.##.#####.####o#",
    "#.####.#####.##.#####.####.#",
    "#..........................#",
    "#.####.##.########.##.####.#",
    "#.####.##.########.##.####.#",
    "#......##....##....##......#",
    "######.##### ## #####.######",
    "######.##### ## #####.######",
    "######.##          ##.######",
    "######.## ###--### ##.######",
    "######.## #      # ##.######",
    "      .   #      #   .      ",
    "######.## #      # ##.######",
    "######.## ######## ##.######",
    "######.##          ##.######",
    "######.## ######## ##.######",
    "#............##............#",
    "#.####.#####.##.#####.####.#",
    "#o..##................##..o#",
    "###.##.##.########.##.##.###",
    "###.##.##.########.##.##.###",
    "#......##....##....##......#",
    "#.##########.##.##########.#",
    "#.##########.##.##########.#",
    "#..........................#",
    "##############################"
]

# Scale factor for rendering
scale = 20

# Pacman's initial position and direction
pacman_x, pacman_y = 1, 1
direction = 'RIGHT'

# Helper functions
def draw_maze():
    for y, line in enumerate(maze):
        for x, char in enumerate(line):
            rect = pygame.Rect(x*scale, y*scale, scale, scale)
            if char == '#':
                pygame.draw.rect(screen, WALL_COLOR, rect)
            elif char in '.o':
                pygame.draw.circle(screen, DOT_COLOR, rect.center, 3 if char == '.' else 6)

def move_pacman():
    global pacman_x, pacman_y
    next_x, next_y = pacman_x, pacman_y
    if direction == 'LEFT':
        next_x -= 1
    elif direction == 'RIGHT':
        next_x += 1
    elif direction == 'UP':
        next_y -= 1
    elif direction == 'DOWN':
        next_y += 1

    # Check for wall collision
    if maze[next_y][next_x] != '#':
        pacman_x, pacman_y = next_x, next_y
        eat_dot()

def eat_dot():
    global maze
    if maze[pacman_y][pacman_x] in '.o':
        maze[pacman_y] = maze[pacman_y][:pacman_x] + ' ' + maze[pacman_y][pacman_x+1:]

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                direction = 'RIGHT'
            elif event.key == pygame.K_UP:
                direction = 'UP'
            elif event.key == pygame.K_DOWN:
                direction = 'DOWN'

    # Move Pacman
    move_pacman()

    # Draw everything
    screen.fill(BACKGROUND_COLOR)
    draw_maze()
    pacman_rect = pygame.Rect(pacman_x*scale, pacman_y*scale, scale, scale)
    pygame.draw.circle(screen, PACMAN_COLOR, pacman_rect.center, scale//2)

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
