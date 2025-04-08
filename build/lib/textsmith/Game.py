from textsmith import InputParser
class Game():
    """
    Represents the game world and handles interactions between the player and rooms.

    Attributes:
        playerClass (Player): The player object interacting with the game.
        currentRoom (Room or None): The current room the player is in. Defaults to None.
        acceptedCommands (list): A list of commands that the game recognizes, such as "LOOK" and "MOVE".

    Methods:
        __init__(playerClass): Initializes the game with a player object and a list of accepted commands.
        readCommand(command, direction): Processes the player's command and calls the appropriate method.
        attemptLook(): Displays the description of the current room.
        attemptMove(direction): Moves the player to the next room in the specified direction.
        updateRoom(roomObject): Updates the current room for the player and the game.
    """
    
    def __init__(self, playerClass):
        """
        Initializes the game with the given player and sets up the accepted commands list.

        Args:
            playerClass (Player): The player object that will interact with the game.
        """
        self.playerClass = playerClass
        self.currentRoom = None
        self.acceptedCommands = ["LOOK", "MOVE"]
    
    def readCommand(self, command, direction=None):
        """
        Processes the player's input command and executes the corresponding action.

        Args:
            command (str): The command entered by the player (e.g., "LOOK", "MOVE").
            direction (int, optional): The direction to move in (0 - north, 1 - south, 2 - east, 3 - west). Only used with "MOVE" command.
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
        Attempts to display the description of the current room.

        If there is no current room loaded, it will prompt the player to update the room.
        """
        if self.currentRoom:
            description = self.currentRoom.getDescription()
            print(description)
        else:
            print("No room has been loaded. Please update the room first using 'updateRoom(roomObject)'.")

    def attemptMove(self, direction):
        """
        Attempts to move the player to the next room in the specified direction.

        Args:
            direction (int): The direction in which to move (0 - north, 1 - south, 2 - east, 3 - west).

        If there is no valid room in the specified direction, the player will not be moved.
        """
        if self.currentRoom:
            # Check if there's a valid room in the given direction
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
        Updates the current room for both the game and the player.

        Args:
            roomObject (Room): The new room object to set as the current room.
        """
        self.playerClass.currentRoom = roomObject
        self.currentRoom = roomObject
        print(f"Room updated to {self.currentRoom.name}.")

    def getUserInput(self, dataType, lineArt, attempts=1):
        inputParser = InputParser(dataType)
        inputParser.setAttempts(attempts)
        return inputParser.getUserInput(lineArt)



    

         




