# Pomodoro Timer

> Exercise from my current Python course. (https://www.udemy.com/course/100-days-of-code/)

Python exercise focused on learning:

- Tkinter GUI programming
- Functions and modular code organization
- Using global variables to manage program state
- while loop simulation using `after()` method
- Basic UI design with Canvas and Labels

## Description

This program is a classic **Pomodoro Timer**, a productivity tool that helps manage focus and rest periods.

- Work sessions last 25 minutes by default
- Short breaks last 5 minutes
- Every 4 work sessions, a long 20-minute break starts
- Timer automatically switches between work and break phases
- Check marks (✔) appear after each completed work session

### Example interaction

```
[Timer shows 25:00]
User clicks "Start"
Timer counts down to 0
Switches to short break (5:00)
After break, returns to work session
```

### Learning Goal

- Practice GUI creation with Tkinter
- Use `after()` for timer-like behavior without freezing the window
- Manage global variables across function calls
- Organize functions for clarity and maintainability
- Combine logic, flow control, and user interface elements

## How to Run
```
python pomodoro.py
```

## Customization
- Adjust `WORK_MIN`, `SHORT_BREAK_MIN`, or `LONG_BREAK_MIN` to change session durations.
- Change color constants (`PINK`, `RED`, `GREEN`, `YELLOW`) to personalize the UI.

## Requirements
```
pip install pillow
```

## Screenshot
![Pomodoro Timer](img.png)

## License
This project is free to use and modify for learning purposes.