import spells

class Enemies:
    def __init__(self, name, strength, speed, durability, stamina, vitality):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.durability = durability
        self.stamina = stamina
        self.vitality = vitality

    def is_alive(self):
        if self.vitality <= 0:
            print(f"The {self.name} died.")
            return False

#class demon
#class undead
#class holy
#class psychic


