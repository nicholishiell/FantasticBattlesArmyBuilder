from Trait import Trait
from Unit import Unit
from Army import Army


class Faction:
    
    def __init__(self, 
                 name : str, 
                 description : str,
                 racial_trait : Trait):
        
        self.name = name
        self.description = description
        self.racial_trait = racial_trait
        self.unit_roster = []
        self.armies = []
        
    def add_unit(self, 
                 unit : Unit):
        
        self.unit_roster.append(unit)