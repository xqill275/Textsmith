from textsmith import Game, Player, Room, InputParser

# Create rooms
room1 = Room("Test Room1", "This is a test room where you spawn.")
room2 = Room("Test Room2", "This is the second room you can move to.")


# Link rooms togethe (north direction for this example)
room1.updateConnectionts(0, room2)

playerObject = Player()
gameObject = Game(playerObject)

playerName = gameObject.getUserInput("str", "Whats is your name?: ", 1)

playerObject.setName(playerName)


# Update the player's current room
gameObject.updateRoom(room1)

# Player looks at their current room description
gameObject.readCommand("LOOK", None)

# get userInput
command = gameObject.getUserInput("str", ":// ", 1)
direction = gameObject.getUserInput("int", ":// ", 1)


gameObject.readCommand(command, direction)

# Player looks at the new room description
gameObject.readCommand("LOOK", None)