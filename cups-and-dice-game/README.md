# Cups and Dice Game Simulation

## 📘 Overview
This project builds an **object-oriented dice game simulation** featuring multiple types of dice and an interactive betting game.  
The system was developed by first creating a modular set of die classes (six-sided, ten-sided, and twenty-sided) and a composite Cup class to hold multiple dice.  
On top of this foundation, a fully interactive game engine was implemented, allowing players to place bets, roll the cup, and win rewards based on how close their rolls are to a randomly generated goal.

This project demonstrates a strong understanding of **object-oriented programming principles**, **class inheritance**, and **composite design patterns**.

---

## 🛠️ Technology Stack
- **Language**: Python 3.x
- **Key Techniques**:
  - Object-Oriented Programming (Classes, Inheritance, Composition)
  - User Input and Output handling
  - Random Number Generation
  - Game State Management (balance tracking, multiple game rounds)

---

## 🧠 Design Approach
The project was developed in two main stages:

1. **Class Design**:
   - **SixSidedDie, TenSidedDie, TwentySidedDie** classes were implemented with shared interfaces.
   - A **Cup** class was created to hold any combination of dice and manage batch rolling and sum calculation.

2. **Game Engine**:
   - Players are given an initial balance and a random goal number.
   - Players can bet money and select the dice configuration for each round.
   - Winnings are calculated based on the proximity of the roll sum to the goal:
     - Exact match: 10x payout
     - Within 3 points (but not over): 5x payout
     - Within 10 points (but not over): 2x payout
   - The game continues until the player decides to quit.

All components were developed using clean, modular, and reusable code following **top-down design principles**.

---

## 🖥️ How to Run
1. Ensure you have **Python 3.x** installed.
2. Place both files in the same working directory:
    - `dice_and_cup_classes.py`
    - `dice_game_simulation.py`
3. Run the main game script:
    ```bash
    python dice_game_simulation.py
    ```
4. Follow the on-screen prompts to play the game!

*Note*:  
- The system relies only on the Python standard library.
- No external packages are required.

---

## 📄 Files Included
| File | Description |
|:---|:---|
| `dice_and_cup_classes.py` | Defines the SixSidedDie, TenSidedDie, TwentySidedDie, and Cup classes |
| `dice_game_simulation.py` | Implements the interactive betting game logic |
