# Pong Game

A classic Pong game implementation using Python's Turtle graphics with two-player paddle controls and physics simulation.

## Features
- Two-player local multiplayer gameplay
- Realistic ball physics with paddle and wall bouncing
- Score tracking for both players
- Smooth paddle movement controls
- Classic arcade-style visual design with black background
- Collision detection for paddles and boundaries

## Game Components
- `main.py` - Main game loop, setup, and event handling
- `paddle.py` - Paddle class with movement mechanics
- `ball.py` - Ball class with physics and collision logic
- `scoreboard.py` - Score tracking and display system

## Controls
- **Right Paddle**: Up/Down arrow keys
- **Left Paddle**: W/S keys
- **Quit Game**: Close window or use window controls

## How to Play
1. Run `main.py` to start the game
2. Left player uses W/S keys to move their paddle
3. Right player uses Up/Down arrow keys to move their paddle
4. Hit the ball with your paddle to send it to the opponent
5. Score points when your opponent misses the ball
6. First to reach the target score wins

## Game Physics
- Ball bounces off top and bottom walls
- Ball bounces off paddles with angle variation
- Ball speed may increase during gameplay
- Paddle movement is smooth and responsive

## Visual Features
- Classic black and white color scheme
- Smooth animation with controlled frame rate
- Clear score display
- Retro arcade aesthetic

## Learning Concepts
- Object-oriented programming design
- Game physics and collision detection
- Event handling and real-time input
- Turtle graphics animation techniques
- Game loop architecture
- Class inheritance and composition

## Requirements
- Python 3.x
- turtle module (included with Python)

## Technical Features
- 60 FPS gameplay with controlled animation
- Efficient collision detection algorithms
- Modular code structure for easy modification
- Real-time score updates