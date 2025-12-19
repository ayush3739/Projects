# Higher or Lower Guessing Game

A social media follower count guessing game where players compare the popularity of celebrities, brands, and public figures.

## Features
- Random celebrity/brand comparisons
- Follower count guessing mechanics
- Score tracking system
- ASCII art graphics and visual elements
- Continuous gameplay until wrong guess
- Screen clearing for clean interface

## Game Components
- `higher or lower.py` - Main game logic and flow
- `data.py` - Database of celebrities/brands with follower counts
- `images.py` - ASCII art graphics (logo, VS symbol)

## How to Play
1. Run `higher or lower.py`
2. Two celebrities/brands are displayed with their descriptions
3. Guess which one has more social media followers
4. Enter 'A' for the first option or 'B' for the second option
5. Correct guesses increase your score
6. Game continues until you guess incorrectly
7. Final score is displayed

## Example Gameplay
```
Compare A: Cristiano Ronaldo, Footballer, from Portugal.
    _    __
   | |  / /
   | | / / 
   | |/ /  
   |___/   

Compare B: Kylie Jenner, Reality TV personality, from United States.

Higher or Lower? Type 'A' or 'B': A
You're right! Current score: 1
```

## Game Features
- **Data-driven**: Uses real follower count data
- **Visual Appeal**: ASCII art for enhanced experience
- **Score System**: Track consecutive correct guesses
- **Randomization**: Different combinations each game
- **Cross-platform**: Works on Windows, Mac, and Linux

## Data Categories
The game includes various types of personalities:
- Athletes and sports figures
- Musicians and entertainers
- Social media influencers
- Brands and companies
- Politicians and public figures

## Learning Concepts
- Random selection algorithms
- Data structure management
- User input validation
- Score tracking systems
- ASCII art integration
- Cross-platform compatibility

## Requirements
- Python 3.x
- No external dependencies required

## Customization
- Add new personalities to `data.py`
- Modify ASCII art in `images.py`
- Adjust game difficulty by changing data