class UnitBase:
    
    def __init__(self):
        self.name = None
        self.points_base = 0
        self.movement_base = 0
        self.melee_base = 0 
        self.shooting_short_base = 0
        self.shooting_long_base = 0
        self.resolve_base = 0
        self.defense_base = 0
    
    def __str__(self):
        return f'{self.name}'
    
    @classmethod
    def from_dict(cls, data):
        unit = cls()
        
        unit.name = data['name']
        unit.points_base = data['Pts']
        unit.movement_base = data['profile']['Mov']
        unit.melee_base = data['profile']['Mel']
        unit.shooting_short_base = data['profile']['Sht-s'] 
        unit.shooting_long_base = data['profile']['Sht-l']
        unit.resolve_base = data['profile']['Res']
        unit.defense_base = data['profile']['Def']
        
        return unit