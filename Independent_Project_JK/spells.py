import enemies

class Spells:
    def __init__(self, name, type, description, lore, effect):
        self.name = name
        self.type = type
        self.description = description
        self.lore = lore
        self.effect = effect

class Fireball(Spells):
    def cast(self, target, level):
        if target.speed < (level * 20):
            if (level * 20) - target.durability < 1:
                damage = 1
                target.vitality -= damage
            else:
                damage = (level * 20) - target.durability
                target.vitality -= damage
            print(f"You cast Fireball! {target.name} takes {damage} damage and is set on fire!")
        else:
            print("Fireball missed!")
        
      
#class Eldritch_Blast(Spells):
 #   def cast(self, target):
  #      if target.speed < 30





class DIEEEEEEEEEEE(Spells):
    def cast(self, target):
        damage = 1000000000000000
        target.vitality -= damage

