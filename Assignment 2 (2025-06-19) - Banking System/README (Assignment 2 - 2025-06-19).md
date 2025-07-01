# PEP Python Full Stack Assignment - Simple Banking System

## Overview
This repository contains my Python Full Stack assignment for the Personal Enhancement Program (PEP). The project is a simple banking system implemented in Python to demonstrate Object-Oriented Programming (OOP) concepts, including class construction, encapsulation, inheritance, polymorphism, duck typing, operator overloading, and composition. The program is structured with modular classes and functions, meeting all assignment objectives through a robust implementation of bank accounts, customer management, and utility functions.

## Assignment Objectives
The goal is to create a Python program that implements a banking system with the following features:
- **BankAccount Base Class**: Manage accounts with owner and balance, track total accounts, support deposits, withdrawals, and merging via the + operator.
- **Subclasses**: Implement `SavingsAccount` with interest and `CheckingAccount` with overdraft limits, overriding withdrawal behavior.
- **Customer Class**: Manage a collection of accounts using composition, with methods to add accounts, calculate total balance, and transfer funds.
- **Duck Typing Utility**: Provide a function to print account summaries without type checking, working with any object that has the required interface.
- **Polymorphism Demo**: Show polymorphic dispatch by invoking common methods on different account types and merging accounts.
- **Special Methods**: Implement string representations and operator overloading for usability.

## Features
1. **BankAccount Base Class**:
   - Stores owner publicly and balance with name-mangling.
   - Tracks total accounts created using a class variable.
   - Supports deposits and withdrawals with validation.
   - Merges accounts using the + operator, combining balances and owner names.
   - Provides string representations via `__str__` and `__repr__`.
2. **SavingsAccount Subclass**:
   - Adds an interest rate and a method to apply interest to the balance.
3. **CheckingAccount Subclass**:
   - Adds an overdraft limit with property-based access.
   - Overrides withdrawal to allow overdrafts up to the limit.
4. **Customer Class**:
   - Manages a list of accounts (composition).
   - Supports adding accounts, calculating total balance, and transferring funds between accounts.
   - Includes string representations for clarity.
5. **Duck Typing Utility**:
   - A `print_account_summary` function that works with any object having `owner` and `balance` or `get_balance()` attributes/methods.
   - Demonstrated with `BankAccount` subclasses and a custom `CryptoWallet` class.
6. **Polymorphism Demo**:
   - Iterates over a list of different account types, calling common methods (`deposit`, `withdraw`) to show polymorphic behavior.
   - Merges accounts to demonstrate operator overloading.

## Repository Structure
```
Assignment 2 (2025-06-19) - Banking System/
├── banking.py                                 # Class definitions and utility function
├── demo.py                                    # Demonstration script for all features
├── 2025-06-19 Assignment - Banking System.pdf # Assignment document
├── README.md                                  # This file, describing the project and usage
```

## How to Run
1. **Prerequisites**:
   - Python 3.x installed on your system.
2. **Setup**:
   - Clone this repository:
     ```
     git clone https://github.com/ShreyasKashyap357/Python-Full-Stack-PEP.git
     ```
   - Navigate to the repository folder:
     ```
     cd Assignment 2 (2025-06-19) - Banking System
     ```
3. **Run the Program**:
   - Execute the demonstration script:
     ```
     python demo.py
     ```
4. **Usage**:
   - The script automatically runs a comprehensive demo, showcasing account creation, deposits, withdrawals, overdraft, interest application, account merging, customer management, duck typing, and object printing.
   - Review the output to see all operations and their results.

## Code Details
- **Files**:
  - `banking.py`: Defines `BankAccount`, `SavingsAccount`, `CheckingAccount`, `Customer`, `print_account_summary`, and `demo_polymorphism`.
  - `demo.py`: Demonstrates all features with error handling and includes `CryptoWallet` for duck typing.
- **Classes and Functions**:
  - `BankAccount`: Base class with `owner`, `__balance`, `total_accounts`, methods for `deposit`/`withdraw`, properties, and special methods (`__add__`, `__str__`, `__repr__`).
  - `SavingsAccount`: Inherits from `BankAccount`, adds `interest_rate` and `apply_interest`.
  - `CheckingAccount`: Inherits from `BankAccount`, adds `_overdraft_limit` and overrides `withdraw`.
  - `Customer`: Composes `BankAccount` objects, with methods for adding accounts, calculating total balance, and transferring funds.
  - `print_account_summary`: Duck typing utility to print owner and balance.
  - `CryptoWallet`: Custom class for duck typing demo with `owner` and `get_balance()`.
  - `demo_polymorphism`: Shows polymorphic dispatch in `banking.py`.
  - `main`: Comprehensive demo in `demo.py`.
- **Error Handling**:
  - Validates inputs (e.g., non-negative amounts, account ownership).
  - Handles exceptions in `withdraw`, `deposit`, `transfer`, and account merging.
- **Modularity**: Classes and functions are organized for reusability and clarity.

## Technologies Used
- **Python**: Core language for the banking system.
- **Standard Libraries**: Used for input handling, string formatting, and data structures (lists, dictionaries).

## Notes
- The program is console-based for simplicity, focusing on OOP concepts.
- Robust error handling ensures graceful failure for invalid inputs or operations.
- The `__add__` method creates a generic `BankAccount` for merged accounts, as specific subclass attributes (e.g., `interest_rate`) weren’t required.
- `print_account_summary` supports both `balance` and `get_balance()` for flexible duck typing.
- Polymorphism is demonstrated by calling common methods on different account types, with `hasattr` used for subclass-specific methods to maintain flexibility.
- The `Customer` class includes `__str__` and `__repr__` for better usability, though not explicitly required.

## Author
[Shreyas Kashyap]
Created as part of the Personal Enhancement Program (PEP) Python Full Stack course.
