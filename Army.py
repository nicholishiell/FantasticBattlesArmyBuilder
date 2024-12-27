from Unit import Unit

class Army:
    
    def __init__(self,
                 name : str,
                 description : str):
        self.name = name
        self.description = description
        self.unit_roster = []
        
    def add_unit(self, 
                 unit : Unit,
                 quantity : int):
        
        self.unit_roster.append((unit, quantity))