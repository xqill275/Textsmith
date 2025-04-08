class InputParser:
    def __init__(self, dataStructure):
        self.dataStructure = dataStructure
        self.attempts = 1
        self.dataDic = { "int": int,
                   "str": str,
                   "float": float
        }

    def setAttempts(self, newAttempts):
        self.attempts = newAttempts

    def getDataStructure(self):
        if self.dataStructure in self.dataDic:
            return self.dataDic[self.dataStructure]
            
        else:
            print(f"Sorry, '{self.dataStructure}' is not a supported data type.")
            return None
        
    def getUserInput(self, lineArt):
        dataType = self.getDataStructure()
        if self.dataStructure is None:
            return None  

        for numAttempts in range(self.attempts):
            try:
                return dataType(input(lineArt))
            except ValueError:
                print(f"Invalid input. Expected {self.dataStructure}.")
        print("Too many failed attempts.")
        return None