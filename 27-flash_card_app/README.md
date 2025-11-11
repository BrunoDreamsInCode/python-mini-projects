# Flashy App (French Flashcards)

> Exercise from my current Python course. (https://www.udemy.com/course/100-days-of-code/)

Python exercise focused on learning:

- Tkinter GUI programming  
- File handling with pandas  
- Exception handling with `try / except`  
- Timed events using `after()`  
- Data persistence (saving progress to CSV)  
- Randomized selection and dictionary manipulation  

## Description

This program is a **Flashcard Learning App**, designed to help memorize French vocabulary efficiently.

- Shows a French word on each flashcard  
- After 3 seconds, the card flips to show the English translation  
- ✅ Button marks the word as known and removes it from future rounds  
- ❌ Button skips to the next word without saving progress  
- Progress is automatically saved in `words_to_learn.csv`  

### Example interaction

```
French side shows: "partir"
(3 seconds later)
English side shows: "to leave"
User clicks ✅ → word removed from learning list
```

### Learning Goals

- Practice GUI design with Tkinter  
- Understand event scheduling with `after()`  
- Work with data persistence and CSV manipulation  
- Apply control flow and error handling in real projects  

## How to Run
```
python main.py
```

## Files
- `main.py` – main application file  
- `data/french_words.csv` – original dataset  
- `data/words_to_learn.csv` – file automatically created to save progress  
- `images/` – folder containing card and button graphics  

## Requirements
```
pip install pandas
```

## Screenshot
![img_1.png](img_1.png)

## License
This project is free to use and modify for learning purposes.
