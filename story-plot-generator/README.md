# Story Plot Generator System

## 📘 Overview
This project implements a **Story Plot Generator System** featuring random and interactive plot creation tools, developed with **object-oriented design principles** and an emphasis on separating model and view responsibilities (similar to the MVC pattern).

The system allows:
- Simple random plot generation.
- Fully randomized plot construction using multiple thematic components.
- Interactive user-driven plot assembly by selecting among random options.

This project demonstrates class inheritance, modular design, and user interaction strategies in Python.

---

## 🛠️ Technology Stack
- **Language**: Python 3.x
- **Key Techniques**:
  - Object-Oriented Programming (Classes, Inheritance, Extension)
  - MVC-inspired Model and View separation
  - File reading and random sampling
  - Modular and reusable code structure

---

## 🧠 Design Approach
The project includes three main generator classes:

- **SimplePlotGenerator**:  
  Always generates the fixed plot "Something happens."

- **RandomPlotGenerator**:  
  Randomly assembles a plot by combining elements from multiple input files:
  - Names, adjectives, professions, verbs, villain descriptions.

- **InteractivePlotGenerator**:  
  Guides the user through making choices step-by-step to assemble a custom plot.

Each generator **registers a viewer** (like `PlotViewer`) to handle input/output, ensuring the generators remain agnostic to the I/O format (console, GUI, etc.).

---

## 🖥️ How to Run
1. Ensure you have **Python 3.x** installed.
2. Place all provided `.txt` files and the script in the same working directory:
    - `plot_generator_system.py`
    - `plot_names.txt`
    - `plot_adjectives.txt`
    - `plot_profesions.txt`
    - `plot_verbs.txt`
    - `plot_adjectives_evil.txt`
    - `plot_villian_job.txt`
    - `plot_villains.txt`
3. Run the main script:
    ```bash
    python plot_generator_system.py
    ```
4. Follow the prompts to generate a random or interactive story plot!

*Note*:  
- `DieRollerExample.txt` is provided as a reference for the initial MVC architecture idea.

---

## 📄 Files Included
| File | Description |
|:---|:---|
| `plot_generator_system.py` | Main program implementing all three plot generators |
| `plot_names.txt` | List of hero names |
| `plot_adjectives.txt` | Positive adjectives |
| `plot_profesions.txt` | List of professions |
| `plot_verbs.txt` | Verbs for hero actions |
| `plot_adjectives_evil.txt` | Negative adjectives for villains |
| `plot_villian_job.txt` | Villain professions |
| `plot_villains.txt` | Villain names |
