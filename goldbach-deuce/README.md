# Goldbach Deuce: Optimized Two-Sum Search

## 📘 Overview
This project implements an optimized solution to the classic **Two-Sum Problem**:  
Given a list of random integers, determine whether any two distinct numbers sum up to a target value `n`.

Unlike the naive O(n²) approach, this solution improves the time complexity to **O(n log n)** by using sorting and binary search techniques.  
The project simulates real-world algorithm optimization scenarios and showcases fundamental problem-solving strategies.

---

## 🛠️ Technology Stack
- **Language**: Python 3.x
- **Key Techniques**:
  - List sorting (Merge Sort level complexity)
  - Binary search for efficient lookup
  - Random number generation
  - Time complexity optimization

---

## 🧠 Design Approach
The program operates as follows:
1. Accepts user input for:
   - `i`: number of integers to generate (random numbers between 0 and 100)
   - `n`: the target sum value.
2. Generates a random list of `i` integers.
3. Sorts the list (preprocessing, O(n log n)).
4. For each element, uses binary search to efficiently determine if a complement exists.
5. Outputs whether a valid pair was found.

This approach reduces overall computational time compared to brute-force methods, demonstrating how smart preprocessing and searching techniques lead to major performance gains.

---

## 🖥️ How to Run
1. Ensure you have **Python 3.x** installed.
2. Place the script file in your working directory:
    - `goldbach_deuce_two_sum.py`
3. Run the program:
    ```bash
    python goldbach_deuce_two_sum.py
    ```
4. Follow the prompts to enter the number of integers and the target sum.

*Note*:  
- The program uses only the Python standard library.
- No additional packages are required.

---

## 📄 Files Included
| File | Description |
|:---|:---|
| `goldbach_deuce_two_sum.py` | Main script implementing the optimized Two-Sum solution |
