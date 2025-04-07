class Room():
    """
    Represents a room in the game world.

    Attributes:
        name (str): The name of the room.
        description (str): A textual description of the room.
        connections (list): A list representing the room's connections in the four cardinal directions (north, south, east, west).
                            Each index corresponds to a direction: 0 - north, 1 - south, 2 - east, 3 - west. Defaults to None.

    Methods:
        __init__(name, description): Initializes a room with a name, description, and no connections.
        updateName(newName): Updates the room's name.
        updateDescription(newDescription): Updates the room's description.
        updateConnectionts(connectionIndex, room): Sets the connection for a specific direction (north, south, east, west) to a room.
        getDescription(): Returns the description of the room.
    """
    
    def __init__(self, name, description):
        """
        Initializes a new room with the given name, description, and no connections.

        Args:
            name (str): The name of the room.
            description (str): The description of the room.
        """
        self.name = name
        self.description = description
        self.connections = [None, None, None, None]  # 0 - north, 1 - south, 2 - east, 3 - west
    
    def updateName(self, newName):
        """
        Updates the name of the room.

        Args:
            newName (str): The new name for the room.
        """
        self.name = newName
    
    def updateDescription(self, newDescription):
        """
        Updates the description of the room.

        Args:
            newDescription (str): The new description for the room.
        """
        self.description = newDescription
    
    def updateConnectionts(self, connectionIndex, room):
        """
        Sets the connection for a specific direction (north, south, east, west) to a new room.

        Args:
            connectionIndex (int): The index representing the direction (0 - north, 1 - south, 2 - east, 3 - west).
            room (Room): The room to connect in the given direction.
        """
        if 0 <= connectionIndex <= 3:
            self.connections[connectionIndex] = room
        else:
            print(f"Invalid connection index: {connectionIndex}. Must be between 0 and 3.")
    
    def getDescription(self):
        """
        Returns the description of the room.

        Returns:
            str: The description of the room.
        """
        return self.description
