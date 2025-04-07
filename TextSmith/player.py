class player():
    """
    Represents a player in the game.

    Attributes:
        name (str): The name of the player.
        currentRoom (Room or None): The room the player is currently in. Defaults to None.

    Methods:
        __init__(name): Initializes the player with a name and sets the current room to None.
        moveToRoom(desiredRoom): Moves the player to the specified room.
    """
    
    def __init__(self, name):
        """
        Initializes a new player with the given name and sets their current room to None.

        Args:
            name (str): The name of the player.
        """
        self.name = name
        self.currentRoom = None
    
    def moveToRoom(self, desiredRoom):
        """
        Moves the player to the specified room.

        Args:
            desiredRoom (Room): The room the player should move to.
        """
        self.currentRoom = desiredRoom
