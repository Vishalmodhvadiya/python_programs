# Python Lab Practicals — README

This repository contains solutions for Python lab practicals covering data types, control structures, data structures, OOP, exception handling, file management, regular expressions, and database operations.

## Requirements
- Python 3.8+
- Built-in modules only: `re`, `json`, `sqlite3`, `math`
- No external installations needed

## How to Run
```bash
python <filename>.py
```
Each file is self-contained and can be run independently. Suggested naming convention below (adjust to match your own folder structure, e.g. `2_syllabus_program/a.py`).

---

## Practical 2 — Data Types, Operators and Conditional Statements
| File | Description |
|---|---|
| `2a.py` | Print "Hello World" |
| `2b.py` | Find the maximum of 3 numbers |
| `2c.py` | Swap two variables without a temporary variable (using tuple unpacking or arithmetic) |
| `2d.py` | Menu-driven calculator (add, subtract, multiply, divide) |
| `2e.py` | Calculate the sum of digits in an integer |

## Practical 3 — Control Structures and Functions
| File | Description |
|---|---|
| `3a.py` | Factorial of a number — iterative and recursive versions |
| `3b.py` | Count digits, letters, uppercase, lowercase, and spaces in a sentence |
| `3c.py` | GCD of two numbers — iterative and recursive (Euclidean algorithm) |
| `3d.py` | Convert a decimal number to hexadecimal, octal, and binary |

## Practical 4 — Working with Data Structures (Part I)
| File | Description |
|---|---|
| `4a.py` | Remove duplicates from a list |
| `4b.py` | Find frequency of elements in a list |
| `4c.py` | Sort a given list |
| `4d.py` | Matrix addition and matrix multiplication using nested lists |
| `4e.py` | Generate Pascal's Triangle using lists |
| `4f.py` | Find min/max in a list of tuples; remove an element from a tuple |

## Practical 5 — Working with Data Structures (Part II)
| File | Description |
|---|---|
| `5a.py` | Map two lists into a dictionary (`zip` + `dict`) |
| `5b.py` | Invert keys and values of a dictionary |
| `5c.py` | Generate a dictionary of alphabet frequency from a string |
| `5d.py` | Sum all values in a dictionary |
| `5e.py` | Concatenate two dictionaries |
| `5f.py` | Nested dictionary of students (name → {semester, age, cpi}); print all student names |

## Practical 6 — Object-Oriented Programming
| File | Description |
|---|---|
| `6a.py` | `BankAccount` class — `showBalance`, `withdraw`, `deposit`, `transfer`, with getters/setters via `@property`; 2 objects instantiated |
| `6b.py` | `Person` base class with `Businessman`/`Employee` subclasses; compares income and prints the name with greater income |
| `6c.py` | `Clock` class — `setClock`, `displayTime`, `tick` (with second → minute → hour rollover) |
| `6d.py` | Diamond inheritance: base class `A`, children `B` and `C`, class `D(B, C)`; each class has a `Call` method; a single `D().Call()` triggers `Call` in every class via `super()` (MRO) |

## Practical 7 — Exception Handling and Assertions
| File | Description |
|---|---|
| `7a.py` | Open a file and write data to it, handling I/O exceptions (`FileNotFoundError`, `PermissionError`, `IsADirectoryError`, `IOError`) |
| `7b.py` | Prompt for a number; print if positive/zero, raise exception if negative; "Code execution completed" always prints via `finally` |
| `7c.py` | Interactive calculator with custom `FormulaError` exception — validates 3-part formula input, supports `+`/`-`, loops until `quit` |
| `7d.py` | Practical 6a (`BankAccount`) with full exception handling added (invalid amounts, insufficient balance, wrong types, invalid recipients) |
| `7e.py` | Reciprocal of list elements `[12, 0, 'a', 20, 'hi']` with exception handling (`ZeroDivisionError`, `TypeError`) |
| `7f.py` | Discount calculator using `assert` — discount cannot be negative or exceed the original price |
| `7g.py` | Division of two vectors — `raise` for mismatched lengths, exception handling for division by zero |

## Practical 8 — File Management
| File | Description |
|---|---|
| `8a.py` | Read n integers, store in `total.txt`, separate odds/evens into `odd.txt`/`even.txt`, display all three files |
| `8b.py` | Copy content of one JSON file into another using `json.load`/`json.dump` |

## Practical 9 — Regular Expressions
| File | Description |
|---|---|
| `9a.py` | Match a string containing `a` followed by one or more `b`'s (`ab+`) |
| `9b.py` | Find sequences of lowercase letters joined with an underscore (e.g. `hello_world`) |
| `9c.py` | Find all five-character-long words in a string |
| `9d.py` | Validate email format: `username@domain.com/edu/org`, username allows `+ . _ -` |
| `9e.py` | Extract the top-level domain (TLD) from an email address |
| `9f.py` | Password validator — at least 1 lowercase, 1 uppercase, 1 digit, 1 special character (`$#@`), length 6–12 |

## Practical 10 — Database Operations
| File | Description |
|---|---|
| `10a.py` | Create a `student` table (`id`, `name`, `spi`) using SQLite |
| `10b.py` | Insert data into the `student` table |
| `10c.py` | Display students with `spi > 8` |
| `10d.py` | Create a `course` table (`id`, `name`, `student_id`) with a foreign key to `student`; display students registered for a specific course (JOIN query) |

---

## Notes
- Exception handling (`try`/`except`/`finally`) is used throughout wherever file I/O, user input, or invalid data is possible.
- Where relevant, both **iterative** and **recursive** approaches are shown (factorial, GCD) for comparison.
- Regex-based and manual string-logic versions are provided for some string/pattern problems, for learning purposes.
- Practical 6d demonstrates Python's Method Resolution Order (MRO) and diamond inheritance using `super()`.
- Database programs use `sqlite3` (built into Python) — no external database server required; each run creates/reuses a local `.db` file.
