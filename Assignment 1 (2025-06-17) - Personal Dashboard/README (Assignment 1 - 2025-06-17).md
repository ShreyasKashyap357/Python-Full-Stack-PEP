# PEP Python Full Stack Assignment - Personal Dashboard

## Overview
This repository contains my Python Full Stack assignment for the Personal Enhancement Program (PEP). The project is a personal dashboard implemented in Python, designed to manage user data, track expenses, maintain a contact book, perform string manipulations, and demonstrate list and dictionary comprehensions. The program is structured with modular functions for reusability and clarity, meeting all the assignment objectives.

## Assignment Objectives
The goal is to create a Python program that serves as a personal dashboard with the following features:
- **User Profile**: Collect and store personal information (name, age, hobbies) in a dictionary.
- **Expense Tracker**: Record expenses with categories, calculate the total, and list unique categories.
- **Contact Book**: Store at least 3 contacts (name, age), compute the average age, and display contacts over 25.
- **String Fun**: Manipulate a user-provided sentence by converting it to uppercase, counting vowels, and reversing word order while preserving punctuation.
- **Comprehensions**: Generate a list of squares (1–10) and a dictionary of cubes (1–5) using comprehensions.
- **Bonus**: Organize the code into reusable functions for clarity and modularity.

## Features
1. **User Profile**:
   - Prompts for name, age, and comma-separated hobbies.
   - Stores data in a dictionary with hobbies as a list.
2. **Expense Tracker**:
   - Allows users to input any number of expenses with categories.
   - Validates expense amounts to ensure numeric input.
   - Displays total expenses and unique categories.
3. **Contact Book**:
   - Ensures at least 3 contacts are added with name and age.
   - Provides a menu to view contacts, compute average age, show contacts over 25, or exit.
   - Validates age input to ensure it’s numeric.
4. **String Fun**:
   - Takes a sentence about the user’s day.
   - Displays it in uppercase, counts vowels, and reverses word order while handling punctuation correctly.
5. **Comprehensions**:
   - Generates a list of squares for numbers 1–10.
   - Creates a dictionary mapping numbers 1–5 to their cubes.

## Repository Structure
```
Assignment 1 (2025-06-17) - Personal Dashboard/
├── dashboard.py       # Main Python script with the personal dashboard program
├── 2025-06-17 Assignment - Personal Dashboard.pdf #Assignment document
├── README.md         # This file, describing the project and usage
```

## How to Run
1. **Prerequisites**:
   - Python 3.x installed on your system.
2. **Setup**:
   - Clone this repository:
     ```
     git clone https://github.com/your-username/personal-dashboard.git
     ```
   - Navigate to the repository folder:
     ```
     cd personal-dashboard
     ```
3. **Run the Program**:
   - Execute the Python script:
     ```
     python dashboard.py
     ```
4. **Usage**:
   - Follow the interactive menu to select options (1–6).
   - Input data as prompted for each feature (e.g., name, expenses, contacts, sentence).
   - Use `Ctrl+C` to exit gracefully if needed, or select option 6 to exit the dashboard.

## Code Details
- **File**: `dashboard.py`
- **Functions**:
  - `user_profile()`: Collects and returns user data as a dictionary.
  - `expense_tracker()`: Tracks expenses, validates inputs, and displays totals and categories.
  - `contact_book()`: Manages contacts with a menu-driven interface.
  - `string_fun()`: Performs string manipulations (uppercase, vowel count, reverse words).
  - `comprehensions()`: Demonstrates list and dictionary comprehensions.
- **Error Handling**:
  - Validates numeric inputs for age and expenses.
  - Handles `KeyboardInterrupt` for graceful exit.
- **Modularity**: Each feature is encapsulated in a separate function for reusability.

## Technologies Used
- **Python**: Core programming language for the dashboard.
- **Standard Libraries**: Used for input handling, string manipulation, and data structures (lists, dictionaries, sets).

## Notes
- The program is interactive and console-based, designed for simplicity and clarity.
- Input validation ensures robust handling of user errors (e.g., non-numeric inputs).
- The code is organized to meet the assignment’s bonus requirement of using functions for modularity.

## Author
[Shreyas Kashyap]
Created as part of the Personal Enhancement Program (PEP) Python Full Stack course.
