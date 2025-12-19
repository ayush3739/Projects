# Turtle Crossing Game

A Frogger-style arcade game where a turtle must safely cross a busy road filled with moving cars.

## Features
- **Player Turtle**: Controlled by keyboard input
- **Moving Cars**: Randomly generated traffic at different speeds
- **Level Progression**: Game gets harder with each successful crossing
- **Collision Detection**: Game ends if turtle hits a car
- **Score Tracking**: Level counter shows progress
- **Increasing Difficulty**: Cars move faster at higher levels

## Game Components
- `main.py` - Main game loop and coordination
- `player.py` - Player turtle class with movement controls
- `car_manager.py` - Car generation and movement system
- `scoreboard.py` - Level tracking and display

## How to Play
1. Run `main.py` to start the game
2. Use the **Up Arrow** key to move the turtle forward
3. Navigate through moving cars to reach the top of the screen
4. Successfully crossing increases your level
5. Cars move faster with each level
6. Avoid getting hit by cars or the game ends

## Game Mechanics
- **Player Movement**: Up arrow key moves turtle forward
- **Car Generation**: Cars spawn randomly from the right side
- **Speed Increase**: Each level makes cars move faster
- **Win Condition**: Reach the top of the screen
- **Lose Condition**: Collision with any car

## Controls
- **↑ (Up Arrow)**: Move turtle forward
- **Game Window Close**: Exit game

## Level System
- Start at Level 1
- Each successful crossing advances to next level
- Higher levels = faster moving cars
- No upper limit - see how far you can go!

## Visual Layout
- Turtle starts at bottom of screen
- Cars move from right to left across screen
- Finish line at top of screen
- Score/level displayed on screen

## Learning Concepts
- Object-oriented programming with multiple classes
- Game physics and collision detection
- Event handling and keyboard input
- Random generation and probability
- Level progression systems
- Turtle graphics animation

## Technical Features
- Smooth 60 FPS gameplay
- Efficient collision detection
- Dynamic difficulty scaling
- Modular class design
- Real-time score updates

## Requirements
- Python 3.x
- turtle module (included with Python)

## Game Strategy
- Time your movements carefully
- Watch car patterns and speeds
- Be patient - rushing leads to collisions
- Higher levels require more precise timing

This classic arcade-style game is perfect for learning game development concepts while having fun with increasing challenges!