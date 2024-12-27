import json

from Trait import Trait
from UnitBase import UnitBase
from Unit import Unit

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class UnitBuilder:
    
    def __init__(self):
        self.traits_dict = self.load_traits()
        self.unit_base_dict = self.load_unit_base()
        
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    def load_traits(self):  
        with open('resources/game-data/traits.json', 'r') as file:
            traits_data = json.load(file)
            
        traits_dict = {}
        
        for trait in traits_data:
            traits_dict[trait['trait_name']] = Trait.from_dict(trait)
                
        return traits_dict
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    def load_unit_base(self):
        with open('resources/game-data/unit-types.json', 'r') as file:
            unit_base_data = json.load(file)
            
        unit_base_dict = {}
        
        for unit_type in unit_base_data:
            unit_base_dict[unit_type['name']] = UnitBase.from_dict(unit_type)
            
        return unit_base_dict

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    def create_unit(self, unit_name, unit_description, unit_type, racial_trait, company_trait_1, company_trait_2, company_trait_3):
                
        return Unit(unit_name=unit_name, 
                    unit_description=unit_description, 
                    unit_type=self.unit_base_dict[unit_type], 
                    racial_trait=self.traits_dict[racial_trait], 
                    company_trait_1=self.traits_dict[company_trait_1], 
                    company_trait_2=self.traits_dict[company_trait_2], 
                    company_trait_3=self.traits_dict[company_trait_3])
