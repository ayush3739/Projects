# Hirst Painting Generator

A digital art generator inspired by Damien Hirst's famous spot paintings, created using Python's Turtle graphics.

## Features
- **Spot Painting Recreation**: Mimics Hirst's famous dot artworks
- **Color Extraction**: Uses colorgram.py to extract colors from real images
- **Grid Pattern**: Creates organized rows and columns of colored dots
- **Random Color Selection**: Each dot uses a randomly selected color
- **Customizable Size**: Adjustable number of dots and grid dimensions

## How It Works
1. Color palette is extracted from a reference image using colorgram
2. Turtle starts at bottom-left corner of canvas
3. Creates a grid pattern by drawing colored dots
4. Each dot color is randomly selected from the extracted palette
5. Turtle moves systematically to create rows and columns

## Files
- `main.py` - Main art generation script
- `image.jpg` - Reference image for color extraction
- Generated artwork appears on screen

## Color Palette
The script uses a pre-extracted color palette from the reference image:
- 30 different RGB color values
- Colors range from earth tones to vibrant hues
- Palette mimics real Hirst painting color schemes

## Technical Features
- **Grid System**: Mathematical positioning for perfect alignment
- **Color Mode**: RGB color mode for accurate color representation
- **Speed Optimization**: Fastest turtle speed for quick generation
- **Position Management**: Precise turtle positioning and heading

## Customization Options
```python
number_of_dots = 100        # Total dots to draw
grid_size = 10             # Dots per row/column
dot_size = 20              # Size of each dot
spacing = 50               # Distance between dots
```

## Art Generation Process
1. Turtle moves to starting position (bottom-left)
2. Draws dots in rows from left to right
3. Moves up to next row when row is complete
4. Continues until all dots are drawn
5. Final artwork displays on screen

## Color Extraction (Advanced)
The colorgram.py package can extract colors from any image:
```python
import colorgram
colors = colorgram.extract('image.jpg', 30)
rgb_colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]
```

## Learning Concepts
- Digital art generation
- Color theory and palettes
- Grid-based positioning systems
- Random selection algorithms
- Turtle graphics advanced techniques
- Image processing basics

## Requirements
- Python 3.x
- turtle module (included with Python)
- colorgram.py (for color extraction from new images)

## Installation
```bash
pip install colorgram.py  # Only needed for new color extraction
python main.py
```

## Artistic Inspiration
Damien Hirst's spot paintings are famous for:
- Perfect circular spots in grid patterns
- Vibrant, non-repeating colors
- Mathematical precision and randomness
- Large-scale visual impact

This digital recreation captures the essence of these iconic artworks while teaching programming concepts!