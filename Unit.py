from utils import *
from Trait import Trait
from UnitBase import UnitBase

# =============================================================================

class Unit:
    
    def __init__(   self,
                    unit_name: str,
                    unit_description: str,
                    unit_type : UnitBase,
                    racial_trait : Trait,
                    company_trait_1 : Trait,
                    company_trait_2 : Trait,
                    company_trait_3 : Trait):
        
        self.name = unit_name
        self.description = unit_description
        
        self.unit_type = unit_type
                    
        self.racial_trait = racial_trait
        
        self.company_trait_1 = company_trait_1
        self.company_trait_2 = company_trait_2
        self.company_trait_3 = company_trait_3
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 

    def __str__(self):
        return f'{self.name}, {self.resolve}, {self.movement}, {self.melee}, {self.shooting_short}/{self.shooting_long}, {self.defense}, {self.points}pts, {self.racial_trait}, {self.company_trait_1}, {self.company_trait_2}'

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
    @property
    def traits(self):
        return [self.racial_trait, 
                self.company_trait_1, 
                self.company_trait_2, 
                self.company_trait_3]
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        
    @property
    def trait_strings(self):
        
        trait_strings = ''
        for trait in self.traits:
         
            if trait.trait_name != 'None':
                trait_strings += trait.trait_name + ',' 
        
        return trait_strings[:-1]
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        
    @property
    def points(self):
        
        return self.get_adjusted_attribute(self.unit_type.points_base, 'Pts')
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    @property
    def resolve(self):     
        return self.get_adjusted_attribute(self.unit_type.resolve_base, 'Res')
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    @property
    def movement(self):
        return self.get_adjusted_attribute(self.unit_type.movement_base, 'Mov')
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
    @property
    def melee(self):
        return self.get_adjusted_attribute(self.unit_type.melee_base, 'Mel')
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
    @property
    def shooting_short(self):
            return self.get_adjusted_attribute(self.unit_type.shooting_short_base, 'Sht-s')
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                    
    @property
    def shooting_long(self):
        return self.get_adjusted_attribute(self.unit_type.shooting_long_base, 'Sht-l')
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   
    @property
    def defense(self):
        return self.unit_type.defense_base
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
    def get_adjusted_attribute( self,
                                base_value : str,
                                attribute : str):
        
        adjusted_value = int(base_value)
        
        for trait in self.traits:
            
            adjustment = trait.get_attribute_adjustment(attribute)
            
            if adjustment[0] == '+':
                adjusted_value += int(adjustment[1:])
            elif adjustment[0] == '-':
                adjusted_value -= int(adjustment[1:])
            else:
                adjusted_value = int(adjustment[1:])
                break
        
        return adjusted_value

# =====================================

class Character(Unit):
    
    def __init__(self):
        super().__init__()
        self.relic = None
        
# =============================================================================
        
class MagicUser(Character):
    
    def __init__(self):
        super().__init__()
        self.spells = []
        self.spell_points = 3
        
    def add_spell(self, spell):
        self.spells.append(spell)
        
# =============================================================================

class Spell:
    
    def __init__(self):
        self.name = None
        self.difficulty = None
        self.description = None
        self.level = None