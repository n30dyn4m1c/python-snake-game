import curses
import random
import time

def main(stdscr):
    # Initialize curses
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)   # Make getch non-blocking
    stdscr.timeout(100) # Refresh screen every 100ms (controls game speed)

    # Get screen dimensions
    sh, sw = stdscr.getmaxyx()

    # Initialize snake
    snake = [
        [sh // 2, sw // 2 + 1],  # Head
        [sh // 2, sw // 2],
        [sh // 2, sw // 2 - 1]
    ]

    # Initial direction: right (0: right, 1: down, 2: left, 3: up)
    # Using row_delta, col_delta for movement
    direction = 0
    directions_map = {
        0: (0, 1),   # Right (row_delta, col_delta)
        1: (1, 0),   # Down
        2: (0, -1),  # Left
        3: (-1, 0)   # Up
    }

    # Generate initial food
    food = []
    while not food:
        fy = random.randint(1, sh - 2)
        fx = random.randint(1, sw - 2)
        if [fy, fx] not in snake:
            food = [fy, fx]

    # Game score
    score = 0

    # Draw initial snake and food
    for y, x in snake:
        stdscr.addch(y, x, '#')
    stdscr.addch(food[0], food[1], '*')
    stdscr.addstr(0, 0, f'Score: {score}')

    game_over = False
    while not game_over:
        # Get user input
        key = stdscr.getch()

        # Update direction based on input
        if key == curses.KEY_RIGHT and direction != 2: # Cannot go right if currently going left
            direction = 0
        elif key == curses.KEY_DOWN and direction != 3: # Cannot go down if currently going up
            direction = 1
        elif key == curses.KEY_LEFT and direction != 0: # Cannot go left if currently going right
            direction = 2
        elif key == curses.KEY_UP and direction != 1:   # Cannot go up if currently going down
            direction = 3
        elif key == 27: # ESC key to exit
            game_over = True
            break

        # Calculate new head position
        y_delta, x_delta = directions_map[direction]
        new_head = [snake[0][0] + y_delta, snake[0][1] + x_delta]

        # Check for game over conditions
        # 1. Wall collision
        if (new_head[0] < 1 or new_head[0] >= sh - 1 or
            new_head[1] < 1 or new_head[1] >= sw - 1):
            game_over = True
            break
        # 2. Self-collision (check against all body parts except the very last one, which will be removed)
        if new_head in snake[:-1]:
            game_over = True
            break

        # Insert new head
        snake.insert(0, new_head)

        # Check if snake ate food
        if new_head == food:
            score += 1
            stdscr.addstr(0, 0, f'Score: {score}')
            # Generate new food
            food = []
            while not food:
                fy = random.randint(1, sh - 2)
                fx = random.randint(1, sw - 2)
                # Ensure new food doesn't spawn on the snake
                if [fy, fx] not in snake:
                    food = [fy, fx]
            stdscr.addch(food[0], food[1], '*')
        else:
            # Remove tail if no food was eaten
            tail = snake.pop()
            stdscr.addch(tail[0], tail[1], ' ') # Erase old tail

        # Draw new head
        stdscr.addch(new_head[0], new_head[1], '#')

        # Control game speed based on score (optional)
        stdscr.timeout(100 - (score * 5)) # Faster as score increases, up to a limit

    # Game over screen
    stdscr.clear()
    center_y = sh // 2
    center_x = sw // 2
    game_over_message = "GAME OVER!"
    score_message = f"Your Score: {score}"
    exit_message = "Press any key to exit."

    stdscr.addstr(center_y - 2, center_x - len(game_over_message) // 2, game_over_message, curses.A_BOLD)
    stdscr.addstr(center_y, center_x - len(score_message) // 2, score_message)
    stdscr.addstr(center_y + 2, center_x - len(exit_message) // 2, exit_message)
    stdscr.refresh()
    stdscr.getch() # Wait for a key press before exiting

# Run the game
if __name__ == '__main__':
    curses.wrapper(main)
