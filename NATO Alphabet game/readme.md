# NATO Phonetic Alphabet Game

A Python application that converts any word into NATO phonetic alphabet code words.

## Features
- Converts user input words to NATO phonetic alphabet
- Uses pandas for efficient CSV data processing
- Dictionary comprehension for fast letter-to-code mapping
- Case-insensitive input handling
- Interactive command-line interface

## How It Works
1. Loads NATO phonetic alphabet data from CSV file
2. Creates a dictionary mapping each letter to its NATO code word
3. Prompts user to enter a word
4. Converts each letter to corresponding NATO phonetic code
5. Displays the complete phonetic representation

## Example
```
Input: "HELLO"
Output: ['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']
```

## Files
- `main.py` - Main application script
- `nato_phonetic_alphabet.csv` - NATO alphabet data (A-Z with code words)

## NATO Phonetic Alphabet Reference
A=Alpha, B=Bravo, C=Charlie, D=Delta, E=Echo, F=Foxtrot, G=Golf, H=Hotel, I=India, J=Juliet, K=Kilo, L=Lima, M=Mike, N=November, O=Oscar, P=Papa, Q=Quebec, R=Romeo, S=Sierra, T=Tango, U=Uniform, V=Victor, W=Whiskey, X=X-ray, Y=Yankee, Z=Zulu

## Requirements
- Python 3.x
- pandas library

## Installation
```bash
pip install pandas
python main.py
```

## Usage
1. Run the script
2. Enter any word when prompted
3. View the NATO phonetic alphabet conversion