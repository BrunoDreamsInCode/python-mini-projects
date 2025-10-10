# Hirst Painting with Turtle

A simple Python program created as part of a Python learning project. It draws a 10x10 grid of colored dots inspired by Damien Hirst's artwork using the `turtle` module. Each dot is drawn with a random color extracted from the image and uses a turtle cursor for visualization.

## How to Run

1. Make sure Python 3.x is installed.
2. Install the required library:

```bash
pip install colorgram.py
```

3. Run the script in your terminal or IDE:

```bash
python hirst_colors.py
```

4. Make sure `hirst.jpg` is in the project folder.

## Requirements
- Python 3.x
- `turtle` (built-in)
- `colorgram.py`

## Description
- Extracts colors from the image using `colorgram`.
- Draws a 10x10 grid of dots with random colors from the extracted palette.
- Uses `turtle` for drawing and RGB color mode for accurate colors.
- The turtle cursor is hidden and the drawing is displayed on a dark background.
- Keeps the window open until clicked.