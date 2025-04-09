class InputParser:
    """
    A utility class to parse and validate user input based on expected data types.

    Attributes:
        dataStructure (str): The name of the expected data type ("int", "str", "float").
        attempts (int): Number of input attempts allowed before failing.
        dataDic (dict): Mapping of string type names to actual Python type constructors.

    Methods:
        setAttempts(newAttempts): Sets the number of input attempts allowed.
        getDataStructure(): Retrieves the corresponding Python type based on the dataStructure string.
        getUserInput(lineArt): Prompts the user for input, validates it, and returns the value if valid.
    """

    def __init__(self, dataStructure):
        """
        Initializes the InputParser with a specified data type.

        Args:
            dataStructure (str): The name of the data type to expect ("int", "str", or "float").
        """
        self.dataStructure = dataStructure
        self.attempts = 1
        self.dataDic = {
            "int": int,
            "str": str,
            "float": float
        }

    def setAttempts(self, newAttempts):
        """
        Sets the number of input attempts the user is allowed.

        Args:
            newAttempts (int): Number of attempts to allow.
        """
        self.attempts = newAttempts

    def getDataStructure(self):
        """
        Retrieves the actual Python type corresponding to the expected data type.

        Returns:
            type or None: The Python type constructor (e.g., int, str, float), or None if unsupported.
        """
        if self.dataStructure in self.dataDic:
            return self.dataDic[self.dataStructure]
        else:
            print(f"Sorry, '{self.dataStructure}' is not a supported data type.")
            return None

    def getUserInput(self, lineArt):
        """
        Prompts the user for input and attempts to convert it to the expected data type.

        Args:
            lineArt (str): The prompt string (can include ASCII art or custom formatting).

        Returns:
            Any or None: The converted input value if successful, or None if all attempts fail or type is unsupported.
        """
        dataType = self.getDataStructure()
        if dataType is None:
            return None

        for numAttempts in range(self.attempts):
            try:
                return dataType(input(lineArt))
            except ValueError:
                print(f"Invalid input. Expected {self.dataStructure}.")
        print("Too many failed attempts.")
        return None
