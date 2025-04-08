class Player:
    """
    Represents a player in the game.

    Attributes:
        name (str): The name of the player.
        currentRoom (Room or None): The room the player is currently in. Defaults to None.

    Methods:
        __init__(): Initializes the player with a default name and no current room.
        moveToRoom(desiredRoom): Moves the player to the specified room.
        setName(newName): Updates the player's name.
    """

    def __init__(self):
        """
        Initializes a new player with a default name and sets their current room to None.
        """
        self.name = "Defualt Name"  # Note: Consider correcting the spelling to "Default Name"
        self.currentRoom = None

    def moveToRoom(self, desiredRoom):
        """
        Moves the player to the specified room.

        Args:
            desiredRoom (Room): The room to move the player into.
        """
        self.currentRoom = desiredRoom

    def setName(self, newName):
        """
        Sets a new name for the player.

        Args:
            newName (str): The new name to assign to the player.
        """
        self.name = newName
