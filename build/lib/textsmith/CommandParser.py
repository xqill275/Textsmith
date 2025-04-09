class CommandParser:
    def __init__(self, command):
        self.command = command
        self.parsedCommand = self.parseCommand() 

    def parseCommand(self):
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
        return self.parsedCommand