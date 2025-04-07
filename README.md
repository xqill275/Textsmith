# TEXTSMITH

**Version 0.1**

This is a simple, modular, text-based game engine built in Python. It provides a framework for developers to create their own interactive text-based games, focusing on rooms, players, and basic commands like "LOOK" and "MOVE." It aims to offer a flexible foundation for building adventure games and other text-based experiences.

---

## Features

- **Player Class**: Represents the player in the game world. The player can move between rooms.
- **Room Class**: Defines rooms in the game world with connections in four cardinal directions (north, south, east, west). Each room has a name and description.
- **Game Class**: Handles game logic, such as processing player commands ("LOOK", "MOVE"), updating the player's location, and displaying room descriptions.

---

## Getting Started

To get started with the engine, follow these steps:

### Prerequisites

- Python 3.x installed on your machine.

### Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/xqill275/Textsmith.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Textsmith
    ```

3. install Textsmith
   ```bash
   pip install .
   ```

---

## Usage

Here’s a quick example to get you started with the engine:

### Example: Basic Game Setup

```python
from textsmith import Game, Player, Room

# Create rooms
room1 = room.Room("Test Room1", "This is a test room where you spawn.")
room2 = room.Room("Test Room2", "This is the second room you can move to.")

# Link rooms together (north direction for this example)
room1.updateConnectionts(0, room2)

# Create a player
playerObject = player.Player("Test Player")

# Create a game object
gameObject = game.Game(playerObject)

# Update the player's current room
gameObject.updateRoom(room1)

# Player looks at their current room description
gameObject.readCommand("LOOK", None)

# Player moves north
gameObject.readCommand("MOVE", 0)

# Player looks at the new room description
gameObject.readCommand("LOOK", None)
```

### Available Commands

- **LOOK**: Shows the description of the current room.
- **MOVE**: Moves the player in the specified direction (0 - north, 1 - south, 2 - east, 3 - west).

---

## Structure

The project structure is as follows:

```
engine/
├── game.py          # Contains the Game class handling game logic and commands.
├── player.py        # Contains the Player class that represents the player.
├── room.py          # Contains the Room class that defines rooms and connections.
```

---

## Version 0.1

- Initial release of the game engine with basic player movement, room setup, and basic command handling.

---

## Contributing

Feel free to fork this repository, make changes, and submit a pull request if you'd like to contribute. Please make sure to:

1. Fork the repo
2. Create a feature branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a pull request

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
