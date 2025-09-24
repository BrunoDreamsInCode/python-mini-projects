# Grading Program

> Python exercise to convert student exam scores into grades.
> Exercise from my current Python course. (https://www.udemy.com/course/100-days-of-code/)


Python exercise focused on learning:

* `for` loops and iteration
* Conditional statements (`if`, `elif`, `else`)
* Working with dictionaries
* Assigning values based on conditions

## Description

This program takes a dictionary of student exam scores (`student_scores`) and converts each score into a corresponding grade. The grades are then stored in a new dictionary (`student_grades`) while keeping the original scores intact.

### Grading Criteria

- Scores 91 - 100: Grade = "Outstanding"
- Scores 81 - 90: Grade = "Exceeds Expectations"
- Scores 71 - 80: Grade = "Acceptable"
- Scores 70 or lower: Grade = "Fail"

### Features

1. **Original scores preserved**: The original `student_scores` dictionary is not modified.
2. **Grades stored separately**: Each student's grade is stored in `student_grades`.
3. **Simple conditional logic**: Uses `if`/`elif` statements to determine grades.
4. **Easy to extend**: You can add more students or change grading rules easily.

### Example output

Original: {'Harry': 88, 'Ron': 78, 'Hermione': 95, 'Draco': 75, 'Neville': 60}  
Grades: {'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}

### Learning Goals

* Practice using dictionaries for storing key-value pairs
* Understand iteration through dictionary keys
* Learn to apply conditional statements in real scenarios
* Keep original data intact while creating a new output

## How to Run

```bash
python grading.py
