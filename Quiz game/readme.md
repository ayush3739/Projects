# Quiz Game

An interactive True/False quiz game built with object-oriented programming principles.

## Features
- True/False question format
- Score tracking throughout the quiz
- Object-oriented design with separate classes
- Question bank system for easy content management
- Progress tracking (question number display)
- Immediate feedback on answers

## Game Components
- `main.py` - Main game controller and setup
- `question_model.py` - Question class definition
- `quiz_brain.py` - Quiz logic and game flow management
- `data.py` - Question data source

## How It Works
1. Questions are loaded from the data source
2. Question objects are created and stored in a question bank
3. QuizBrain manages the game flow and scoring
4. Players answer True/False questions sequentially
5. Score is tracked and displayed after each question
6. Game continues until all questions are answered

## Class Structure
- **Question**: Stores question text and correct answer
- **QuizBrain**: Manages game state, scoring, and question flow

## Example Gameplay
```
Q.1: The capital of France is Paris. (True/False): True
You got it right!
Your current score is: 1/1

Q.2: Python is a type of snake. (True/False): False
That's wrong.
Your current score is: 1/2
...
```

## How to Play
1. Run `main.py`
2. Answer each question with "True" or "False"
3. Receive immediate feedback on your answers
4. View your final score at the end

## Learning Concepts
- Object-oriented programming (OOP)
- Class design and encapsulation
- List management and iteration
- User input handling
- Score tracking systems

## Requirements
- Python 3.x
- No external dependencies required

## Customization
- Add new questions in `data.py`
- Modify question format in `question_model.py`
- Enhance scoring system in `quiz_brain.py`