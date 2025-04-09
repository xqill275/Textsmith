class CommandParser:
    """
    A utility class to parse raw user input strings into structured game commands.

    This class takes a raw command string like "move north" and returns a standardized
    command and any arguments in a structured format (e.g., ["MOVE", 0]).

    Attributes:
        command (str): The raw command input by the user.
        parsedCommand (list): A list containing the parsed command and optional argument.
    """

    def __init__(self, command):
        """
        Initializes the CommandParser with a raw input string and immediately parses it.

        Args:
            command (str): The raw input string from the user.
        """
        self.command = command
        self.parsedCommand = self.parseCommand() 

    def parseCommand(self):
        """
        Parses the raw input command string into a structured format.

        Recognizes basic commands like "move <direction>" and converts directions
        to their corresponding index values:
            0 - north, 1 - south, 2 - east, 3 - west

        Returns:
            list: A list where the first element is the uppercase command string (e.g., "MOVE")
                  and the second element is an optional argument (e.g., direction index or None).
        """
        parts = self.command.lower().strip().split()
        if not parts:
            return [None, None]  # Empty input

        cmd = parts[0].upper()  # e.g., 'MOVE', 'LOOK'
        arg = None

        if cmd == "MOVE" and len(parts) > 1:
            directionMap = {
                "north": 0,
                "south": 1,
                "east": 2,
                "west": 3
            }
            arg = directionMap.get(parts[1].lower(), None)

        return [cmd, arg]
    
    def getParsedCommand(self):
        """
        Returns the result of the parsed command.

        Returns:
            list: A two-element list containing the command and its argument.
        """
        return self.parsedCommand
