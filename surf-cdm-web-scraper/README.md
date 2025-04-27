# Surf CDM Web Scraper and Word Frequency Analyzer

## 📘 Overview
This project implements a **web scraper** that extracts text content from the CDM (College of Computing and Digital Media) website, processes the text, and identifies the 25 most frequent words.  
The system extends Python’s built-in `HTMLParser` to cleanly and efficiently extract meaningful content while ignoring HTML tags and structural elements.

This project demonstrates basic web scraping, custom HTML parsing, and text processing techniques in Python.

---

## 🛠️ Technology Stack
- **Language**: Python 3.x
- **Key Techniques**:
  - Extending the `HTMLParser` class
  - Overriding `handle_starttag`, `handle_endtag`, and `handle_data` methods
  - String manipulation and text cleaning
  - Word frequency counting using dictionaries and sorting

---

## 🧠 Design Approach
The program structure includes:
- **Custom HTML Parser**:
  - Overrides relevant methods to extract only visible text.
- **Data Aggregation**:
  - Collects and preprocesses words (e.g., lowercasing, filtering).
- **Analysis and Output**:
  - Counts word occurrences.
  - Identifies and prints the 25 most frequent words found on the website.

Special attention was paid to restricting the scraping only to relevant pages under the CDM domain.

---

## 🖥️ How to Run
1. Ensure you have **Python 3.x** installed.
2. Place the script file in your working directory:
    - `surf_cdm_web_scraper.py`
3. Run the program:
    ```bash
    python surf_cdm_web_scraper.py
    ```
4. Follow any instructions provided in the script to perform the scraping and view the results.

*Note*:  
- The program uses only standard Python libraries.
- Internet access may be required if scraping live data (depending on implementation).

---

## 📄 Files Included
| File | Description |
|:---|:---|
| `surf_cdm_web_scraper.py` | Main script for web scraping and word frequency analysis |
