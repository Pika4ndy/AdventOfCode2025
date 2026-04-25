# 🎄 Advent Of Code 2025

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status: In Progress](https://img.shields.io/badge/Status-In%20Progress-green.svg)](#progress)

This repository contains my solutions to the [Advent Of Code 2025](https://adventofcode.com/2025) puzzles. Each solution is written from scratch without using AI assistance or external solutions—the whole point of solving these puzzles!

## 📋 Table of Contents

- [Progress](#progress)
- [Code Structure](#code-structure)
- [Quick Start](#quick-start)
- [Repository Info](#repository-info)
- [Contributions](#contributions)

## 📊 Progress

| Day | Problem | Status | Solution |
|-----|---------|--------|----------|
| 1 | Historian Hysteria | ✅ Complete | [Day1.py](./Day1/Day1.py) |
| 2 | Red-Nosed Reports | ✅ Complete | [Day2.py](./Day2/Day2.py) |
| 3 | Mull It Over | ✅ Complete | [Day3.py](./Day3/Day3.py) |
| 4 | Ceres Search | ✅ Complete | [Day4.py](./Day4/Day4.py) |
| 5-25 | Coming Soon... | ⏳ In Progress | — |

## 🔧 Code Structure

Each solution follows a consistent pattern with two main functions:

- **`main()`** – Runs the full solution on the actual puzzle input
- **`sampleTest()`** – Experimental function used to develop and test the algorithm on sample inputs

This separation allows for quick iteration during development while keeping a clean, finalized solution.

> **Note:** All code includes comments explaining the algorithm logic. If you find any undocumented sections, they'll be added once all days are completed!

## 🚀 Quick Start

### Requirements

- **[Python](https://www.python.org/downloads/)** 3.10 or higher – Required to run the solutions
- **[Git](https://git-scm.com/install/)** *(mandatory)* – For cloning this repository
- **Code Editor** – I recommend [Visual Studio Code](https://code.visualstudio.com/download), but any editor works

> *Tip:* If you prefer not to install an external IDE, Python comes with **IDLE**, a built-in IDE that works just fine!

### Installation & Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Pika4ndy/AdventOfCode2025.git
   cd AdventOfCode2025
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Run a solution:**

   ```bash
   python3 Day1/Day1.py
   ```

### Troubleshooting

**Don't have Git installed?** You can download this repository as a ZIP file:

1. Click the green **"Code"** button at the top of this page
2. Select **"Download ZIP"**
3. Extract the folder and open it in your editor

![How to download](images/where_to_click.png)

## ℹ️ Repository Info

### Guiding Principle

> ✨ **No AI or external solutions used** – The entire point is to solve these puzzles independently and learn from the process!

### File Structure

```text
AdventOfCode2025/
├── README.md              # This file
├── test.py               # Quick testing script
├── Day1/                 # Each day folder contains:
│   ├── Day1.py          #   - Solution file
│   ├── Day1_input       #   - Actual puzzle input
│   └── Day1_test_input  #   - Sample test input from problem statement
├── Day2/
├── Day3/
├── Day4/
└── images/              # Documentation images
```

### Why This Structure?

- **Separate input files** allow for easy testing with sample data before running against the actual puzzle input
- **Consistent naming** makes it simple to find and navigate solutions
- **Self-contained folders** keep each day's work organized and independent

## 🤝 Contributions & Questions

Have suggestions, questions, or found an issue? I'd love to hear from you! Feel free to:

- 🐛 **Open an issue** if you spot a bug or have a question about the code
- 💡 **Suggest improvements** to the solutions or repository structure
- 📝 **Share feedback** on the code quality or documentation

Your input helps make this repository better for everyone!

---

**Happy coding! 🚀** If you're solving Advent of Code too, feel free to star this repository or share your own solutions!
