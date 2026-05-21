# 🔐 Password Strength Checker

A powerful, modular Python CLI tool that analyzes password strength in real-time, scores them intelligently, flags common passwords instantly, and gives actionable feedback to help users create stronger, more secure passwords.

---

## 📋 Table of Contents

- [Overview](#https://github.com/arpitdevgoswami/Password_Strength_Checker/blob/main/README.md#-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Scoring System](#scoring-system)
- [Strength Levels](#strength-levels)
- [Installation](#installation)
- [Usage](#usage)
- [Modules Explained](#modules-explained)
- [Running Tests](#running-tests)
- [Tech Stack](#tech-stack)
- [Future Improvements](#future-improvements)

---

## 🧾 Overview

Password Strength Checker is a beginner-to-intermediate level Python project built entirely using core Python concepts. It runs in the terminal with a clean, color-coded interface powered by `colorama`. The tool checks multiple security criteria, penalizes weak patterns, and tells the user exactly what to improve.

---

## ✨ Features

- ✅ Real-time password strength analysis
- ✅ Intelligent scoring system (0 to 9)
- ✅ Color-coded terminal output
- ✅ Detects and flags **common passwords** instantly
- ✅ Penalizes repeated characters (`aaa`, `111`)
- ✅ Penalizes sequential patterns (`abc`, `123`)
- ✅ Actionable feedback with specific improvement tips
- ✅ Hidden password input option (no echo on screen)
- ✅ Visible password input option
- ✅ 23 unit tests covering all core functions

---

## 📁 Project Structure

```
Password_Strength_Checker/
│
├── checker.py              # Core password analysis logic
├── scorer.py               # Scoring engine & strength labels
├── feedback.py             # Feedback & suggestions generator
├── common_passwords.py     # Common password loader & checker
├── main.py                 # CLI entry point & interface
│
├── tests/
│   └── test_checker.py     # 23 unit tests
│
├── wordlists/
│   └── common.txt          # List of most common passwords
│
└── README.md
```

---

## ⚙️ How It Works

```
User enters password
        ↓
checker.py → analyzes password (length, uppercase, lowercase,
              digit, special char, repeated char, sequential, common)
        ↓
scorer.py  → adds up all points → calculates final score
        ↓
feedback.py → generates tips based on what's missing or weak
        ↓
main.py    → displays color-coded result + feedback in terminal
```

Each module has a **single responsibility** — making the codebase clean, modular, and easy to maintain.

---

## 🧮 Scoring System

Each check contributes points to the final score:

| Check | Condition | Points |
|---|---|---|
| Length | Less than 8 characters | 0 |
| Length | 8 – 11 characters | +1 |
| Length | 12 – 15 characters | +2 |
| Length | 16 – 19 characters | +3 |
| Length | 20+ characters | +4 |
| Uppercase | Has A-Z | +1 |
| Lowercase | Has a-z | +1 |
| Digit | Has 0-9 | +1 |
| Special Char | Has `!@#$%^&*` etc | +1 |
| Repeated Char | Has `aaa` or `111` | −1 |
| Sequential | Has `abc` or `123` | −1 |
| Common Password | Found in common list | −2 |
| **Maximum Score** | | **9** |

> Score is always minimum 1, never goes below zero.

---

## 🏷️ Strength Levels

| Score | Label | Color |
|---|---|---|
| 8 – 9 | 🔵 Highly Secure | Cyan |
| 6 – 7 | 🟢 Very Strong | Green |
| 5 | 🟡 Strong | Yellow |
| 3 – 4 | 🟠 Fair | Magenta |
| 1 – 2 | 🔴 Weak | Red |

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Password_Strength_Checker.git
cd Password_Strength_Checker
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install colorama
```

---

## 💻 Usage

Run the application:

```bash
python main.py
```

You will see a menu with options:

```
Options:
  [1] Check password (hidden input)
  [2] Check password (visible input)
  [3] Exit
```

### Example Output

```
══════════════════════════════════════════════════

  Strength  :  🔵 Highly Secure
  Score     :  8 / 9

──────────────────────────────────────────────────
  📋 Feedback:

    ✅ Excellent password! Extremely hard to crack.

══════════════════════════════════════════════════
```

### Example — Weak Password

```
══════════════════════════════════════════════════

  Strength  :  🔴 Weak
  Score     :  1 / 9

──────────────────────────────────────────────────
  📋 Feedback:

    🚨 This is a very common password! Avoid it completely.
    ❌ Password is too short. Use at least 8 characters.
    ❌ Add at least one uppercase letter (A-Z).
    ❌ Add at least one lowercase letter (a-z).
    ❌ Add at least one special character (!@#$%^&*).
    ⚠️  Avoid sequential patterns like 'abc' or '123'.

══════════════════════════════════════════════════
```

---

## 🧩 Modules Explained

### `checker.py`
The brain of the project. Contains individual functions for each password check:
- `check_length(password)` — returns 0 to 4 based on length
- `check_uppercase(password)` — returns 1 if has uppercase, else 0
- `check_lowercase(password)` — returns 1 if has lowercase, else 0
- `check_digit(password)` — returns 1 if has digit, else 0
- `check_special_char(password)` — returns 1 if has special char, else 0
- `check_repeated_char(password)` — returns -1 if has `aaa`/`111`, else 0
- `check_sequential(password)` — returns -1 if has `abc`/`123`, else 0
- `check_common_password(password)` — returns -2 if found in common list, else 0
- `analyze_password(password)` — runs all checks and returns a results dictionary

### `scorer.py`
The calculator. Takes the results dictionary and adds up all points:
- `calculate_score(results)` — sums all values, minimum score is 1
- `get_strength_label(score)` — maps score to a strength label
- `evaluate(results)` — returns both score and label together

### `feedback.py`
The advisor. Generates a list of human-readable tips based on what's missing:
- `generate_feedback(results, score, password)` — returns a list of feedback messages, common password check always shown first

### `common_passwords.py`
The database loader. Reads `wordlists/common.txt` and checks passwords against it:
- `load_common_passwords()` — loads the wordlist into a Python set for O(1) lookup
- `is_common_password(password, common_passwords)` — returns True if password is in the set

### `main.py`
The interface. Handles all user interaction:
- `print_banner()` — displays the ASCII art banner
- `print_result()` — displays color-coded score and feedback
- `main()` — runs the main loop with menu options

---

## 🧪 Running Tests

The project includes **23 unit tests** covering all core functions:

```bash
python tests/test_checker.py
```

Expected output:

```
.......................
----------------------------------------------------------------------
Ran 23 tests in 0.001s

OK
```

### What's Tested

| Test Class | What It Covers |
|---|---|
| `TestChecker` | All individual check functions in `checker.py` |
| `TestScorer` | Score calculation and strength labels |
| `TestFeedback` | Feedback messages for various passwords |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3 | Core language |
| `re` | Regex for pattern matching |
| `getpass` | Hidden password input |
| `colorama` | Colored terminal output |
| `os` | File path handling |
| `unittest` | Unit testing framework |

> No database, no framework, no heavy dependencies — pure Python!

---

## 🔮 Future Improvements

- [ ] 🎲 Password Generator — suggest strong random passwords
- [ ] 📁 Bulk checker — check multiple passwords from a `.txt` file
- [ ] 📊 Strength progress bar in terminal
- [ ] 🌐 Web interface using Flask
- [ ] 📦 Package it as a pip installable CLI tool

---

## 👨‍💻 Author

Built with ❤️ by **arpitdevgoswami**

> *"A strong password is your first line of defense."*
