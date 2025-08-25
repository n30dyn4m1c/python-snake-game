Python Terminal Snake Game 🐍

This is a classic Snake game implemented in Python, playable directly in your terminal using the curses library.
Features

    Classic Gameplay: Control a snake, eat food, and grow longer.

    Terminal-Based: Play directly in your command-line interface.

    Score Tracking: Keep track of your high score during a game.

    Dynamic Speed: The game speeds up as your score increases.

    Game Over Conditions: Collision with walls or self ends the game.

How to Play
Controls

    Arrow Keys (↑, ↓, ←, →): Move the snake.

    ESC Key: Exit the game at any time.

Objective

Guide your snake (#) to eat the food (*) that appears randomly on the screen. Each time the snake eats food, it gets longer, and your score increases. Avoid hitting the terminal borders or your own body, as this will end the game!
Setup and Running
Prerequisites

    Python 3: Make sure you have Python 3 installed.

    curses Library:

        Linux/macOS: The curses library is usually pre-installed.

        Windows: You'll need to install windows-curses. Open your command prompt or PowerShell and run:

        pip install windows-curses

Running the Game

    Save the Code:
    Save the provided Python code into a file named snake_game.py.

    Open your Terminal/Command Prompt:
    Navigate to the directory where you saved snake_game.py.

    Execute the Game:
    Run the game using the Python interpreter:

    python snake_game.py

Code Structure

The game logic is encapsulated within the main function, which takes a stdscr object (standard screen) provided by curses.

    Initialization: Sets up curses (hides cursor, non-blocking input, game speed).

    Game State: Initializes the snake's position, food position, direction, and score.

    Game Loop:

        Listens for user input (arrow keys to change direction, ESC to quit).

        Calculates the new head position.

        Checks for game over conditions (wall collision, self-collision).

        Handles food consumption (grows snake, generates new food, updates score).

        Redraws the snake and food on the screen.

    Game Over Screen: Displays "GAME OVER!", your score, and instructions to exit.

Enjoy the game!
