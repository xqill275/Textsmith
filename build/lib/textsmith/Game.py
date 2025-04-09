from textsmith.InputParser import InputParser

class Game():
    """
    Represents the game world and manages interactions between the player and rooms.

    Attributes:
        playerClass (Player): The player object that interacts with the game.
        currentRoom (Room or None): The room the player is currently in. Defaults to None.
        acceptedCommands (list): List of recognized commands such as "LOOK" and "MOVE".

    Methods:
        __init__(playerClass): Initializes the game with a player and sets accepted commands.
        readCommand(command, direction=None): Processes and executes the player's command.
        attemptLook(): Displays the current room's description.
        attemptMove(direction): Moves the player in the specified direction if possible.
        updateRoom(roomObject): Sets the current room for both the player and the game.
        getUserInput(dataType, lineArt, attempts=1): Retrieves and validates user input based on expected type.
    """
    
    def __init__(self, playerClass):
        """
        Initializes the Game instance with a player and sets accepted commands.

        Args:
            playerClass (Player): The player object that will interact with the game world.
        """
        self.playerClass = playerClass
        self.currentRoom = None
        self.acceptedCommands = ["LOOK", "MOVE"]
    
    def readCommand(self, command, direction=None):
        """
        Processes the player's input and performs the appropriate action.

        Args:
            command (str): The command entered by the player (e.g., "LOOK", "MOVE").
            direction (int, optional): The direction in which to move (0 - north, 1 - south, 2 - east, 3 - west).
                                       Required only when using the "MOVE" command.

        If the command is not recognized, an error message is printed.
        """
        if command in self.acceptedCommands:
            if command == "LOOK":
                self.attemptLook()
            elif command == "MOVE" and direction is not None:
                self.attemptMove(direction)
        else:
            print(f"Sorry, the command '{command}' does not exist.")

    def attemptLook(self):
        """
        Displays the description of the current room.

        If no room is currently loaded, prompts the player to update the room.
        """
        if self.currentRoom:
            description = self.currentRoom.getDescription()
            print(description)
        else:
            print("No room has been loaded. Please update the room first using 'updateRoom(roomObject)'.")

    def attemptMove(self, direction):
        """
        Moves the player to a connected room in the specified direction, if available.

        Args:
            direction (int): The direction to move (0 - north, 1 - south, 2 - east, 3 - west).

        If no room exists in the specified direction, the player remains in the current room.
        """
        if self.currentRoom:
            if self.currentRoom.connections[direction] is not None:
                self.currentRoom = self.currentRoom.connections[direction]
                self.playerClass.currentRoom = self.currentRoom
                print(f"Moved to {self.currentRoom.name}.")
            else:
                print("No room in that direction.")
        else:
            print("No room has been loaded. Please update the room first using 'updateRoom(roomObject)'.")

    def updateRoom(self, roomObject):
        """
        Sets a new current room for both the player and the game.

        Args:
            roomObject (Room): The room to set as the current room.
        """
        self.playerClass.currentRoom = roomObject
        self.currentRoom = roomObject
        print(f"Room updated to {self.currentRoom.name}.")

    def getUserInput(self, dataType, lineArt, attempts=1):
        """
        Retrieves and validates user input using the InputParser.

        Args:
            dataType (str): The expected type of input (e.g., "int", "str").
            lineArt (str): The prompt or decorative ASCII art to show the user.
            attempts (int, optional): Number of input attempts allowed. Defaults to 1.

        Returns:
            Any: The validated user input based on the specified data type.
        """
        inputParser = InputParser(dataType)
        inputParser.setAttempts(attempts)
        return inputParser.getUserInput(lineArt)
