# 🐍 Snake Game

A classic **Snake Game** built in Python using the Turtle Graphics module.  
This project was originally created for learning purposes and has now evolved into a more advanced version with persistent score tracking.

## 🧾 New Feature: Persistent High Score System
The latest version introduces a **persistent high score system**.  
Now, the game saves the **highest score** ever achieved in a file called `data.txt`.  

- When the game starts, it **reads** the current highest score from `data.txt`.  
- If the player beats that score, the file is **automatically updated** with the new record.  
- This allows the game to **remember the best player performance** even after closing and reopening the program.  

This feature was implemented using Python’s built-in **file manipulation** tools, ensuring smooth reading and writing operations.

## 🧠 Overview
The player controls a snake that moves around the screen eating food.  
Each time the snake eats, it grows longer and the score increases.  
The game ends when the snake collides with the wall or with its own body.

## 🧩 Objectives Achieved
- Strengthened understanding of **Python fundamentals**  
- Practiced **loops**, **control flow**, and **object-oriented programming**  
- Implemented **event handling** with keyboard inputs  
- Built a functional **game loop** with screen updates  
- Introduced **file manipulation** for score persistence  

## 🛠️ Technologies Used
- **Python 3**  
- **Turtle Graphics** (for graphics and movement)  
- **Random module** (for food placement)  
- **File handling (I/O)** for saving and reading the highest score  

## 🎮 Features
- Smooth snake movement  
- Real-time score display  
- Random food generation  
- Collision detection (walls and self)  
- Persistent high score system (`data.txt`)  
- Game over screen  
- Simple and responsive controls  

## 🚀 How to Run
1. Make sure **Python 3** is installed on your computer.  
2. Clone or download this repository.  
3. Run the main file using the command below:
   ```bash
   python main.py
    ``` 
   ## 🎮 Control Commands

Use the arrow keys to move the snake:

- ⬆️ Up  
- ⬇️ Down  
- ⬅️ Left  
- ➡️ Right  

---

## 🧾 New Feature: Persistent High Score System

The latest version introduces a **persistent high score system**!  
Now, your game keeps track of the **highest score** ever achieved — even after you close the program.

- The game **reads** the previous high score from a file named `data.txt` when it starts.  
- If you beat the previous record, the game **updates** the file automatically with your new high score.  
- This means your progress is **saved permanently** between play sessions.

This feature was implemented using Python’s built-in **file manipulation (read/write)** tools for simplicity and efficiency.

---

## 🧑‍💻 Author
Developed by **Bruno Henrique** as part of a personal learning project.  
Feel free to contribute, suggest improvements, or fork the project!