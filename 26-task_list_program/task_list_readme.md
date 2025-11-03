# Task List Program

> Exercise from my current Python course. (https://www.udemy.com/course/100-days-of-code/)

Python exercise focused on learning:

- input() and user interaction  
- Reading from and writing to text files  
- while loops to control program flow  
- Lists and indexing  
- Conditional statements (if/else)  
- Functions to organize code and reuse logic

## Description

This program simulates a simple task manager:

- Users can add new tasks  
- Users can list all current tasks with numbering  
- Users can remove a task by typing its number  
- The program updates the text file to store tasks persistently

### Example interaction:

```
Type 'a' to ADD
Type 'l' to LIST
Type 'r' to REMOVE
Type 's' to Exit
Your choice: a
Write down your new task: Buy groceries

Type 'a' to ADD
Type 'l' to LIST
Type 'r' to REMOVE
Type 's' to Exit
Your choice: a
Write down your new task: Study Python

Type 'a' to ADD
Type 'l' to LIST
Type 'r' to REMOVE
Type 's' to Exit
Your choice: l

1 - Buy groceries
2 - Study Python

Type 'a' to ADD
Type 'l' to LIST
Type 'r' to REMOVE
Type 's' to Exit
Your choice: r
Type the task number to remove: 1
Task 'Buy groceries' removed successfully!
```

Each run can have different tasks added, listed, and removed.

### Learning Goal

- Practice reading from and writing to files in Python  
- Learn how to manage lists and index items  
- Understand the use of while loops for continuous input  
- Learn to write functions to organize code and reuse logic  
- Combine user input, file handling, and program flow to solve a practical problem

## How to Run
```
python main.py
```