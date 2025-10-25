# U.S.A States Guessing Game

A simple Python program created as a learning project.
It is an interactive game where the player tries to guess all 50 U.S.A states by typing their names. Correct guesses are displayed on a U.S.A map using the `turtle` module. The game tracks your score and exports a CSV file with the states you missed for learning purposes.

## How to Run

1. Make sure Python 3.x is installed.
2. Install the required library:

```
pip install pandas
```

3. Run the script in your terminal or IDE:

```
python main.py
```

4. Make sure the following files are in the project folder:
   - `50_states.csv` (contains state names and coordinates)
   - `blank_states_img.gif` (map image)
   - Python files: `main.py`, `turtlestate.py`, `screenboard.py`

## Requirements
- Python 3.x
- `turtle` (built-in)
- `pandas`

## How to Play
1. A U.S.A map will appear.
2. Type the name of a state in the input box.
3. Correct guesses will appear on the map.
4. Your score will update at the top-left corner.
5. Type `Exit` to quit the game early.
6. After the game ends, a CSV file `States_to_learn.csv` will be generated with the states you missed.

## Project Structure
```
/project-folder
├── main.py
├── turtlestate.py
├── screenboard.py
├── 50_states.csv
├── blank_states_img.gif
└── States_to_learn.csv  # Generated after running the game
```

## Description
- The game displays a blank U.S.A map.
- Players type the name of a state in an input box.
- Correct guesses are displayed at their corresponding coordinates on the map.
- Keeps track of the number of correct guesses out of 50.
- Typing `Exit` ends the game early.
- After the game ends, a CSV file `States_to_learn.csv` is generated with the states that were not guessed.
- The window remains open until clicked, allowing players to review their progress.