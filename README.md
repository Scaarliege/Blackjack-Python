# Blackjack Game

Welcome to the Blackjack game! This project is a console-based implementation of the classic card game Blackjack, featuring both a player and an AI dealer. The game includes various difficulty levels for the AI and provides an engaging user experience with colorful prompts and ASCII art.

## Project Structure

The project is organized as follows:

```
Blackjack
├── src
│   ├── Blackjack.py          # Main game logic
│   ├── Blackjack_ASCII.py    # ASCII art for game states
│   ├── Blackjack_AI.py       # AI behavior for different difficulty levels
│   ├── Blackjack_Lib.py      # Utility functions for game mechanics
│   ├── Blackjack_UI.py       # User interface enhancements
│   └── types
│       └── index.py          # Type definitions and interfaces
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd Blackjack
   ```

2. **Install dependencies**:
   Make sure you have Python installed. Then, install the required packages using:
   ```
   pip install -r requirements.txt
   ```

3. **Run the game**:
   Execute the main game file:
   ```
   python src/Blackjack.py
   ```

## Gameplay Rules

- The objective of Blackjack is to beat the dealer by having a hand value closer to 21 without exceeding it.
- Each player starts with two cards, and they can choose to "hit" (take another card) or "stand" (keep their current hand).
- Aces can count as either 1 or 11, and face cards (Kings, Queens, Jacks) count as 10.
- The dealer must hit until their hand value is at least 17.

## Modules Overview

- **Blackjack.py**: Contains the core game logic, including player and dealer interactions, betting, and win conditions.
- **Blackjack_ASCII.py**: Provides functions to display ASCII art for various game states, enhancing the visual appeal of the game.
- **Blackjack_AI.py**: Implements AI strategies for different difficulty levels, determining how the dealer plays against the player.
- **Blackjack_Lib.py**: Includes utility functions for shuffling the deck, dealing cards, calculating hand values, and managing player inputs.
- **Blackjack_UI.py**: Enhances the user interface with colorful prompts, animations, and improved layouts for hands and betting information.
- **types/index.py**: Defines types and interfaces for better type checking and clarity throughout the project.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.