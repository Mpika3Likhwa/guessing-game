# Guessing Game (My First Python Project)

A simple, interactive number-guessing game built while transitioning from Java and C# to Python. This project served as my introduction to Pythonic syntax and the importance of indentation.

## Overview
The program generates a random number between 1 and 10. The user must guess the number, and the program provides feedback ("Higher" or "Lower") until the correct number is found. It also tracks the number of attempts and handles invalid non-integer inputs without crashing.

## What I Learned (Coming from Java/C#)

This project highlighted the core structural differences between C-style languages and Python:

* Indentation over Curly Braces: Unlike Java/C#, Python does not use curly brackets to define blocks. I learned that whitespace is functional and required for the code to execute correctly.
* Dynamic Typing: I noticed that variable types do not need to be declared (for example, using int x = 5). Variables are assigned directly.
* Type Conversion: In Java and C#, I was used to simple string concatenation. In Python, I learned to use f-strings and the int() function for proper type casting.
* Error Handling: I implemented a try-except block, which is the Python equivalent of try-catch, to manage ValueError exceptions when users provide non-numeric input.

## Features
- Randomization: Uses the Python random module to generate numbers.
- Input Validation: Prevents the program from crashing on invalid user input.
- Score Tracking: Records and displays the total number of guesses taken.
- User Feedback: Provides "Higher" or "Lower" guidance to the user.

## How to Run
1. Ensure Python 3.x is installed on your system.
2. Clone this repository to your local machine.
3. Run the script using the following command:
   python main.py

## Project Structure
- main.py: Contains the game logic.
- .gitignore: Configured to exclude the .venv/ and .idea/ folders to maintain a clean repository.
