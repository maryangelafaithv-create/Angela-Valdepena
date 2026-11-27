#=============================================================
#   SNAKE GAME(pygame)
#   Arrow keys to move. Eat the food, don't hit yourself.
#   Run it: python snske_gama.py (inside your activated venv)
#=============================================================
import random
import pygame

#=============================================================
#   PART 1: GAME SETTINGS (safe to change: start here!)
#=============================================================
GAME_TITLE = "Snake It"
CELL_SIZE = 25
GRID_WIDTH  = 30
GRID_HEIGHT= 28
SPEED = 8
START_LENNGTH = 3
POINTS_PER_FOOD = 1
GROW_PER_FOOD = 1
WALLS_KILL = True

# Colors are (red, green, blue), each from 0 to 255
BACKGROUND_COLOR = (60, 80,100)
GRID_COLOR = (32,38,56)
SNAKE_COLOR = (125, 150, 200)
HEAD_COLOR = (50, 150, 80)
FOOD_COLOR = (20, 40, 60)
TEXT_COLOR = (240,240,240)

#=============================================================
#   PART 2: SETUP
#=============================================================
pygame.init()
WIDTH = CELL_SIZE * GRID_WIDTH
HEIGHT = CELL_SIZE * GRID_HEIGHT 
screen = pygame.display.set_mod((WIDTH, HEIGHT))
pygame.display.set_caption(GAME_TITLE)
clock = pygame.time.font
font = pygame.font.font(None, 36)


#=============================================================
#   PART 3: FUNCTIONS
#=============================================================
def new_game():
    """Return a fresh snake, direction, food, score and growth counter."""
    start_x = GRID_WIDTH // 2
    start_y = GRID_HEIGHT // 2
    snake = []
    for i in range(START_LENGTH):
        snake.append((start_x-i, start_y))            # head is snake[0]
    direction = (1, 0)                                # moving right
    food = place_food(snake)
    return snake, direction, food, 0, 0


def place_food(snake):
    """Pick a random empty square for the food."""
    while True:
        spot = (random.randint(0, GRID_WIDTH -1), random.randint(0, GRID_HEIGHT))
        if spot not in snake:
            return spot


def draw_square(position, color):
    """Draw one grid square at (x, y) grid position."""
    x, y = position
    rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, color, rect, border_radius=5)


def draw_text(text, y):
    """Draw text centered across the screen at height y."""
    image = font.render(text, True, TEXT_COLOR)
    screen.blit(image, (WIDTH // 2 - image.get_width() // 2, y))


def draw_game(snake, food, score):
    """Draw the background, grid, food, snake and score."""
    screen.fill(BACKGROUND_COLOR)
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line (screen, GRID_COLOR, (0, y), (WIDTH, y))
    draw_square(food, FOOD_COLOR)
    for part in snake [1:]:
        draw_square(part, SNAKE_COLOR)
    draw_square(snake[0], HEAD_COLOR)
    draw_text("Score: " + str(score), 10)


#=============================================================
# PAET 4: THE GAME LOOP (events -> update -> draw)
#=============================================================
snake, direction, food, score,grow = new_game()
game_over = False
running = True

while running:
    # ---- 1. EVENTS: read the keyboard ----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if game_over:
                if event.key == pygame.K_r:
                    snake, direction, food, score, grow = new_game()
                    game_over = False
                elif event.key == pygame.K_q:
                 running = False
            # The "!=" checks stop the snake from turning back into itself
            elif event.key == pygame.K_UP and direction != (0, 1):
                direction = (0, -1) 
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                direction (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                direction (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                direction (1, 0)

# --- 2. UPDATE: move the snake and check what happened ----
if not game_over:
    head_x, head_y = snake[0]
    new_head = (head_x + direction[0], head_y + direction [1])

    if WALLS_KILL:
        if new_head[0] < 0 or new_head[0] >= GRID_WIDTH or new_head[1] < 0:
            game_over = True
    else:
        new_head = (new_head[0] % GRID_WIDTH, new_head [1] % GRID_HEIGHT)

    if new_head in snake:
        game_over = True

    if not game_over:
        snake.insert(0, new_head)
        if new_head == food:
            score = score + POINTS_PER_FOOD
            grow = grow + GROW_PER_FOOD
            food = place_food(snake)
        if grow > 0:
            grow = grow -1
        else:
            snake.pop()

# ---- 3. DRAW: paint the new frame ----
if score > high_score:
    high_score = score
    draw_text("Best:" + str(high_score),40)
draw_game(snake, food, score)
if game_over:
    draw_text("GAME OVER, WANT TO TRY AGAIN?", HEIGHT // 2-40)
    draw_text("Score: " + str(score) +" R = play again  Q = quit", HEIGHT)
pygame.display.flip()
clock.tick(SPEED)

pygame.quit()