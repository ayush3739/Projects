# Pomodoro Timer

A productivity timer application based on the Pomodoro Technique with GUI interface and visual indicators.

## Features
- **Pomodoro Technique Implementation**: Work sessions with breaks
- **Visual Timer Display**: Countdown timer with tomato imagery
- **Progress Tracking**: Checkmarks for completed sessions
- **Automatic Transitions**: Switches between work and break periods
- **Color-coded Sessions**: Different colors for work vs. break time
- **Reset Functionality**: Reset timer and progress anytime

## Pomodoro Technique
The app follows the standard Pomodoro Technique:
- **Work Session**: 25 minutes of focused work
- **Short Break**: 5 minutes rest after each work session
- **Long Break**: 20 minutes rest after every 4 work sessions
- **Visual Progress**: Checkmarks show completed sessions

## Files
- `main.py` - Main timer application with GUI
- `tomato.png` - Timer background image
- `snorlax.png` - Additional imagery
- `pngwing.com.png` - UI graphics

## How to Use
1. Run `main.py` to start the timer
2. Click "Start" to begin a work session
3. Work for 25 minutes until timer reaches zero
4. Take the automatic break when prompted
5. Repeat the cycle for maximum productivity
6. Use "Reset" to restart anytime

## Visual Indicators
- **Green Text**: Timer ready/reset state
- **Red Text**: Work session active
- **Pink Text**: Break session active
- **Checkmarks (✓)**: Completed work sessions
- **Tomato Background**: Visual timer display

## Timer Settings (Customizable)
```python
WORK_MIN = 25         # Work session duration
SHORT_BREAK_MIN = 5   # Short break duration
LONG_BREAK_MIN = 20   # Long break duration
```

## Benefits of Pomodoro Technique
- Improved focus and concentration
- Better time management
- Reduced mental fatigue
- Increased productivity
- Regular rest prevents burnout

## GUI Features
- Clean, minimalist design
- Large, easy-to-read timer display
- Color-coded status indicators
- Progress tracking with checkmarks
- Simple start/reset controls

## Learning Concepts
- GUI development with Tkinter
- Timer implementation with threading
- Image integration in applications
- State management
- User interface design principles
- Productivity methodology implementation

## Requirements
- Python 3.x
- tkinter (included with Python)
- Image files (included)

## Customization
- Modify timer durations in constants section
- Change colors by updating color variables
- Replace tomato image with custom graphics
- Adjust fonts and styling as desired