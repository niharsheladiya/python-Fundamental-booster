# 🐍 Python Fundamental Booster — Interactive Personal Data Collector

A beginner-friendly Python console application built for the **PR.1 Fundamental Booster** assignment (Python – Data Science track). The program interactively collects a user's personal information, demonstrates core Python fundamentals (data types, variables, operators, type casting, `id()`, and `type()`), and prints a clean, formatted summary.

---

## 🎥 Live Demo Video Link

[Watch the live demo here](https://drive.google.com/file/d/18Cfy_pdT3Zui3kdTGjWbO2gzrn-kJMa-/view?usp=drivesdk)

---

## 📌 Objective

Create an **Interactive Personal Data Collector** application in Python that captures, processes, and displays personal information from the user using fundamental Python functions and concepts. This project demonstrates a working understanding of:

- `print()` and `input()` functions
- Data types, variables, and operators
- Type casting / type constructors
- Built-in functions like `id()` and `type()`

---

## ✅ Features / Requirements Covered

### 1. Detailed Use of `print()` and `input()`
- Uses `input()` to collect the user's **name**, **age**, **height**, and **favourite number**.
- Uses `print()` to display formatted guidance messages and results at every step.

### 2. Data Types, Variables & Operators
- Stores each piece of collected information in an appropriately typed variable.
- Uses arithmetic operators (`+`, `-`, `*`, `/`) to calculate the user's **approximate birth year** based on their age.
- Uses string concatenation / formatted strings (f-strings) to build user-friendly output messages.

### 3. Type Casting / Constructors
- Casts age input to `int` and height input to `float`.
- Demonstrates converting between types (e.g., float → int) and explains the conversion clearly in the output.

### 4. `id()` and `type()` Functions
- Displays the **data type** and **memory address** of every collected variable.
- Prints a full summary showing each variable's name, value, data type, and memory location.

---

## 🔄 Program Flow

1. **Welcome & Instructions** – Displays a welcome message and a short description of what the program does.
2. **Collect Information** – Prompts the user for their name (string), age (integer), height (float), and favourite number (integer).
3. **Data Processing** – Calculates the user's approximate birth year and gathers `type()`/`id()` info for each variable.
4. **Display Results** – Prints a neatly formatted summary of all collected and processed data.
5. **Exit Message** – Thanks the user and encourages them to keep exploring Python.

---

## 💻 Example Console Interaction

```
Welcome to the Interactive Personal Data Collector!

Please enter your name: Alice
Please enter your age: 25
Please enter your height in meters: 1.68
Please enter your favourite number: 7

Thank you! Here is the information we collected:

Name: Alice (Type: <class 'str'>, Memory Address: 140703847239568)
Age: 25 (Type: <class 'int'>, Memory Address: 9793456)
Height: 1.68 (Type: <class 'float'>, Memory Address: 140703847253232)
Favourite Number: 7 (Type: <class 'int'>, Memory Address: 9793312)

Your birth year is approximately: 1998 (based on your age of 25)

Thank you for using the Personal Data Collector. Goodbye!
```

> 💡 **Note:** Memory addresses change every run — that's Python's memory manager at work, and this is expected behavior, not a bug.

---

## 🚀 How to Run

```bash
python program.py
```

Make sure you have **Python 3** installed. No external libraries are required — this project only uses Python's built-in functions.

---

## 📁 Project Structure

```
Python-Fundamental-Booster-Red-White/
├── program.py       # Main application source code
└── README.md        # Project documentation (this file)
```

---

## 🧠 Assumptions Made

- Height is entered in **meters** (e.g., `1.68`) rather than centimeters.
- Birth year is calculated approximately as `current_year - age`, without accounting for whether the user's birthday has already occurred this year.
- All user input is assumed to be valid and correctly formatted (no error-handling for invalid input was required by the assignment scope).
- Memory addresses shown via `id()` are illustrative — actual values will differ on every run and every machine.

---

## 📝 Academic Integrity

This project was completed independently as part of the **Fundamental Booster** exam for the **Python – Data Science** course. All code is original and written specifically to satisfy the requirements outlined in the assignment brief.

---

**Fundamental Booster — Python - Data Science**
*"Bring on your coding attitude — skills for scaling higher!"*
