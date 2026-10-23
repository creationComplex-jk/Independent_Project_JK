import spells

class Enemies:

    is_demon = False
    is_undead = False
    is_holy = False
    is_psychic = False

    is_fireproof = False
    is_flying = False


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

    def is_exhausted(self):
        if self.stamina == 0:
            self.stamina = -1
            self.speed = 0
            print(f"{self.name} is exhausted! It can no longer dodge!")

class Demon(Enemies):
    def __init__(self, name, strength, speed, durability, stamina, vitality):
        super().__init__(name, strength, speed, durability, stamina, vitality)
        self.is_demon = True
        self.is_fireproof = True

class Undead(Enemies):
    def __init__(self, name, strength, speed, durability, stamina, vitality):
        super().__init__(name, strength, speed, durability, stamina, vitality)
        self.is_undead = True

class Holy(Enemies):
    def __init__(self, name, strength, speed, durability, stamina, vitality):
        super().__init__(name, strength, speed, durability, stamina, vitality)
        self.is_holy = True

class Psychic(Enemies):
    def __init__(self, name, strength, speed, durability, stamina, vitality):
        super().__init__(name, strength, speed, durability, stamina, vitality)
        self.is_psychic = True


