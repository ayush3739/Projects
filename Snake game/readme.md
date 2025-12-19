# Snake Game

A classic Snake game built using Python's Turtle graphics library with smooth controls and score tracking.

## Features
- Snake moves continuously in the current direction
- Food appears randomly on the screen
- Snake grows longer when eating food
- Score increases with each food consumed
- Game ends when snake hits walls or itself
- Keyboard controls (Arrow keys)
- High score tracking

## Files
- `main.py` - Main game loop and setup
- `snake.py` - Snake class with movement and collision logic
- `food.py` - Food class for random food generation
- `scoreboard.py` - Score tracking and game over display

## How to Play
1. Run `main.py`
2. Use arrow keys to control the snake:
   - ↑ - Move Up
   - ↓ - Move Down
   - ← - Move Left
   - → - Move Right
3. Eat the food (red dots) to grow and increase score
4. Avoid hitting walls or the snake's own body
5. Try to achieve the highest score possible!

## Game Rules
- Snake moves continuously in the direction it's facing
- Eating food makes the snake longer and increases score
- Game ends if snake hits the wall boundaries
- Game ends if snake collides with its own body
- Score resets when game ends

## Technical Features
- Smooth 60 FPS gameplay
- Object-oriented design with separate classes
- Collision detection for walls and self-collision
- Random food placement
- Score persistence and display

## Learning Concepts
- Object-oriented programming
- Game loop architecture
- Event handling and keyboard input
- Collision detection algorithms
- Turtle graphics animation
- Class design and inheritance

## Requirements
- Python 3.x
- turtle module (included with Python)

## Game Controls
- **Arrow Keys**: Control snake direction
- **Close Window**: End game

This is a classic implementation of the popular Snake game, perfect for learning Python game development concepts!