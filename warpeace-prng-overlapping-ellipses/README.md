# War and Peace PRNG and Overlapping Ellipses Monte Carlo Simulation

## 📘 Overview
This project contains two interconnected programs based on **randomness generation** and **probabilistic simulation**:

1. **War and Peace PRNG**:  
   Implements a pseudo-random number generator (PRNG) by extracting sequences from the text of *War and Peace* to simulate random values.

2. **Overlapping Ellipses Monte Carlo Simulation**:  
   Uses the PRNG to estimate the overlapping area between two ellipses using a Monte Carlo method.

Together, these programs demonstrate creativity in random number generation and practical application of stochastic simulation techniques.

---

## 🛠️ Technology Stack
- **Language**: Python 3.x
- **Key Techniques**:
  - Custom Pseudo-Random Number Generation (PRNG)
  - File I/O operations (text extraction)
  - Monte Carlo simulation for area estimation
  - 2D geometric calculations

---

## 🧠 Design Approach
**War and Peace PRNG**:
- Reads large text (`war-and-peace.txt`) to generate pseudo-random numbers based on character sequences.
- Provides random number outputs that approximate uniform randomness, albeit not cryptographically secure.

**Overlapping Ellipses Simulation**:
- Simulates a large number of random points within a bounding box.
- Checks whether each point lies inside one or both ellipses.
- Estimates the overlapping area based on the proportion of points within both shapes.

By chaining a custom PRNG into a real-world simulation, the project emphasizes both **algorithmic creativity** and **practical application**.

---

## 🖥️ How to Run
1. Ensure you have **Python 3.x** installed.
2. Place the following files in the same working directory:
    - `warpeace_prng.py`
    - `overlapping_ellipses_monte_carlo.py`
    - `war-and-peace.txt`
3. To generate random numbers based on *War and Peace*:
    ```bash
    python warpeace_prng.py
    ```
4. To run the Monte Carlo simulation:
    ```bash
    python overlapping_ellipses_monte_carlo.py
    ```

*Note*:  
- `war-and-peace.txt` is required by the PRNG to generate random sequences.
- No external packages are needed; only the Python standard library is used.

---

## 📄 Files Included
| File | Description |
|:---|:---|
| `warpeace_prng.py` | Pseudo-random number generator based on text extraction |
| `overlapping_ellipses_monte_carlo.py` | Monte Carlo simulation estimating ellipse overlap |
| `war-and-peace.txt` | Input text file (source for PRNG) |
