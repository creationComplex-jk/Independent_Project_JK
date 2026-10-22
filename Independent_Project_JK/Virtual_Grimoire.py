import spells
import enemies

Fireball = spells.Fireball("Fireball", "Offensive", "A simple projectile, a ball of flame collected and thrown at an enemy.", "The most basic spell, nearly every mage across the globe can perform it. It is among the first taught to a class of aspiring magei, and has become a staple of the magical world.", "Deals moderate damage and sets the target on fire.")
debug = spells.DIEEEEEEEEEEE("debug", "debug", "insta-kill", "testing purposes", "kills the target")

Ogre = enemies.Enemies("Ogre", 50, 5, 50, 30, 120)

def spell_info(spell):
    print(spell.name)
    print(spell.type)
    print(spell.effect)
    print(spell.description)
    print(spell.lore)

def print_spells():
    print("Spells:")
    print("Fireball")
    #print(a whole buncha stuff)
    print("")

def print_targets():
    print("Targets:")
    print("Ogre")
    #print(a whole buncha stuff)

def spellwork(spell, level):
        spell_info(spell)
        cast = input("Cast this spell? Y/N: ")
        if cast == "Yes" or cast == "Y" or cast == "yes" or cast == "y":
            active_enemy = "Y"
            while active_enemy == "Yes" or active_enemy == "yes" or active_enemy == "y" or active_enemy == "Y":
                print_targets()
                target = input("Choose a Target: ")
                if target == "Ogre" or target == "ogre":
                    targeting(Ogre, level)
                else:
                    print("Please pick a listed target.")
                    continue
                active_enemy = input("Do you want to continue testing with this spell? Y/N: ")

def targeting(enemy, level):
    another_cast = input("Cast? Y/N: ")
    while another_cast == "Yes" or another_cast == "Y" or another_cast == "yes" or another_cast == "y":
        spell.cast(enemy, level)
        print(f"The {enemy.name} has {enemy.vitality} health remaining!")
        if enemy.is_alive() == False:
            break
        another_cast = input("Again? Y/N: ")


print("Virtual Grimoire")
print("Version 0.0.1")
print("")
print("-------------------------------------------------------------------------------")
print("")
level = int(input("Please input your mage level. (1-10): "))
change_spell = "Y"
while change_spell == "Yes" or change_spell == "yes" or change_spell == "y" or change_spell == "Y":
    print_spells()
    selection = input("Select a Spell: ")
    if selection == "Fireball" or selection == "fireball":
        spell = Fireball
    elif selection == "debug":
        spell = debug
    else:
        print("Please pick a listed spell.")
        continue
    spellwork(spell, level)
    change_spell = input("Do you want to try a different spell? Y/N: ")
print("Thank you for trying out the Virtual Grimoire!")
