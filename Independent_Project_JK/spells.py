import enemies
#add stamina mechanics


class Spells:
    def __init__(self, name, type, description, lore, effect):
        self.name = name
        self.type = type
        self.description = description
        self.lore = lore
        self.effect = effect

    def dodged(target_stamina, target_speed):
            target_stamina = int(target_stamina / target_speed)
            return target_stamina

class Fireball(Spells):
    def cast(self, target, level):
        if target.speed < (level * 20):
            if target.is_fireproof == False:
                defense_damage = level * 5
                target.durability -= defense_damage
                if (level * 20) - target.durability < 1:
                    damage = 1
                    target.vitality -= damage
                else:
                    damage = (level * 20) - target.durability
                    target.vitality -= damage
                print(f"You cast Fireball! {target.name} takes {damage} damage and is set on fire! Their durability has fallen {defense_damage} points!")
            else:
                print("The enemy is fireproof!")
        else:
            target.stamina = Spells.dodged(target.stamina, target.speed)
            print(f"{self.name} missed! {target.name} lost stamina!")
      
class Eldritch_Blast(Spells):
    def cast(self, target, level):
        if target.speed < 5 * (2 ** level):
            if (level * 30) - target.durability < 1:
                damage = level
                target.vitality -= damage
            else:
                damage = (level * 30) - target.durability
                target.vitality -= damage
            print(f"You cast Eldritch Blast! {level} beam(s) and they all strike true, dealing {damage} damage!")
        else:
            target.stamina = Spells.dodged(target.stamina, target.speed)
            print(f"{self.name} missed! {target.name} lost stamina!")

class Radiance(Spells):
    def cast(self, target, level):
        value = 5 * level
        if target.is_demon == True:
            target.strength -= value
            target.speed -= value
            target.durability -= value
            target.stamina -= value
            target.vitality -= value
            print(f"{target.name}'s stats fell by {value}!")
        elif target.is_undead == True:
            print("This creature doesn't have a soul!")
        elif target.is_holy == True:
            target.strength += value * 2
            target.speed += value * 2
            target.durability += value * 2
            target.stamina += value * 2
            target.vitality += value * 2
            print(f"{target.name}'s stats increased by {value * 2}!")
        else:
            target.strength += value
            target.speed += value
            target.durability += value
            target.stamina += value
            target.vitality += value
            print(f"{target.name}'s stats increased by {value}!")

class Psychic_Shriek(Spells):
    def cast(self, target, level):
        if target.is_psychic == True:
            print(f"The {target.name} repelled the attack!")
        else:
            damage = 15 * level
            target.vitality -= damage
            target.stamina -= 40
            print(f"The {target.name}'s mind has been struck and it has been sent reeling!")



class killspell(Spells):
    def cast(self, target):
        damage = 1000000000000000
        target.vitality -= damage

