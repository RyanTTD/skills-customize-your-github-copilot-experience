
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a text-based Hangman game in Python that uses strings, loops, and conditionals. By completing this assignment, you will practice tracking game state, validating user input, and controlling game flow.

## 📝 Tasks

### 🛠️ Core Game Loop and Word Selection

#### Description
Create the main game loop for Hangman. Your program should choose a random word from a predefined list and repeatedly ask the player to guess one letter at a time.

#### Requirements
Completed program should:

- Define a list of at least 5 possible words.
- Randomly select one word at the start of each game.
- Accept a single-letter guess from the player each turn.
- Continue looping until the player wins or runs out of attempts.


### 🛠️ Progress Display and Win/Loss Conditions

#### Description
Track and display progress after each guess so the player can see correctly guessed letters and remaining attempts. End the game with a clear result message.

#### Requirements
Completed program should:

- Display hidden letters as underscores (example: _ _ _ _ _).
- Reveal correctly guessed letters in their proper positions.
- Decrease remaining attempts only for incorrect guesses.
- Print a win message when the full word is guessed.
- Print a lose message when attempts reach 0 and reveal the word.
