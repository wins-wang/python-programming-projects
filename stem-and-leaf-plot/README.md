# Stem-and-Leaf Plot Program

## 📘 Overview
This project implements a **Stem-and-Leaf Plot generator** based on structured numerical data files.  
It was designed and developed following a **Top-Down structured programming** approach, where the main functionality was broken down into modular and reusable components.

The program reads a data file, organizes the numbers into stems and leaves according to standard stem-and-leaf plotting rules, and outputs a neatly formatted textual plot.  
This tool helps visualize the distribution and shape of a dataset in a compact way, similar to a histogram but preserving original data values.

---

## 🛠️ Technology Stack
- **Language**: Python 3.x
- **Key Techniques**:
  - File I/O operations (reading and processing plain text files)
  - Modular function decomposition
  - Basic data structuring (stems and leaves separation)
  - Input validation and formatted output printing
- **Documentation**:  
  Top-down design document is included (`stem_and_leaf_plot_design.pdf`).

---

## 🧠 Design Approach
The program was built based on a **Top-Down Design Methodology**, which first outlined the major functional components before coding:

- **Main Function**: Orchestrates the program flow.
- **File Selection**: Handles user input for choosing which data file to process.
- **File Conversion**: Reads the numerical data and prepares it for plotting.
- **Stem and Leaf Setting**: Processes numbers to determine their stems and leaves.
- **Printing Function**: Formats and displays the stem-and-leaf plot clearly.

This modularization ensures that each function has a **single, clear responsibility**, making the code easy to read, maintain, and expand.

---

## 🖥️ How to Run
1. Ensure you have **Python 3.x** installed.
2. Place the data file you wish to process in the working directory.
3. Run the program:
    ```bash
    python stem_and_leaf_plot.py
    ```
4. Follow the on-screen prompts to select a dataset and view the generated stem-and-leaf plot.

*Note*:  
- Example data files and detailed structure chart are provided in this repository.
- No external packages are required; the program uses standard Python libraries only.

---

## 📄 Files Included
| File | Description |
|:---|:---|
| `stem_and_leaf_plot.py` | Main program code implementing the Stem-and-Leaf Plot generator |
| `stem_and_leaf_plot_design.pdf` | Top-down structure chart and design documentation |
| `StemAndLeaf1.txt` | Sample dataset for generating a simple stem-and-leaf plot |
| `StemAndLeaf2.txt` | Sample dataset with larger numbers for expanded plotting |
| `StemAndLeaf3.txt` | Sample dataset with four-digit numbers for more complex plots |
