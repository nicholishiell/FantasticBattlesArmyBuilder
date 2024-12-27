from utils import *

# =============================================================================

class Trait:
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    def __init__(self):
        
        self.trait_name = None
        self.description_text = None
        self.isPassive = None
        self.incompatible_traits = []
        
        self.profile_adjustments_dict = {   "Res":  "0",
                                            "Mov":  "0",
                                            "Mel":  "0",
                                            "Pts":  "0",
                                            "Sht-s": "0",
                                            "Sht-l": "0",
                                            "Def":  "0"}
        
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    def __str__(self):
        return self.trait_name
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    def __repr__(self):
        return self.trait_name
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    @classmethod
    def from_dict(cls, trait_dict):
        
        trait = cls()
        
        trait.trait_name = trait_dict['trait_name']
        trait.description_text = trait_dict['description_text']
        trait.isPassive = trait_dict['is_passive']
        trait.incompatible_traits = trait_dict['incompatible_traits']
        
        trait.profile_adjustments_dict = trait_dict['profile_adjustments']
        
        return trait
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    def get_attribute_adjustment(   self,
                                    attribute : str):
        
        return self.profile_adjustments_dict[attribute]
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
    
    def check_compatibility(self, 
                            other_trait):
        return self.trait_name not in other_trait.incompatible_traits
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    