import spells
import enemies

DEBUG = True
if DEBUG == True:
    debug = spells.killspell("debug", "debug", "insta-kill", "testing purposes", "kills the target")


#Spells
Fireball = spells.Fireball("Fireball", "Offensive", "A simple projectile, a ball of flame collected and thrown at an enemy.", "The most basic spell, nearly every mage across the globe can perform it. It is among the first taught to a class of aspiring magei, and has become a staple of the magical world.", "Deals moderate damage and sets the target on fire.")
Eldritch_Blast = spells.Eldritch_Blast("Eldritch Blast", "Offensive", "A beam of arcane energy. The more skilled you are the more you can fire at once.", "A very basic spell, often used to mark a mage's growth in power due to it's simple relationship to said power.", "Deals moderate damage and fires an additional beam for every spell level.")
Radiance = spells.Radiance("Radiance", "Support", "Calls on the power of a targets soul to give them strength.", "A basic but relatively new spell based off of various ecclesiarchal arcana. Calls upon your own soul as if it's a god.", "Grants a minor buff to all stats...unless you're a demon.")
Psychic_Shriek = spells.Psychic_Shriek("Psychic Shriek", "Offensive", "Actualizes your latent psychic power in a telepathic shriek.", "One of the first spells formed during ealry studies on the relationship between the psychic and magical worlds.", "Bypasses durability to deal damage and reduces stamina.")



def spell_info(spell):
    print(spell.name)
    print(spell.type)
    print(spell.effect)
    print(spell.description)
    print(spell.lore)

def print_spells():
    print("Spells:")
    print("Fireball")
    print("Eldritch Blast")
    print("Radiance")
    print("Psychic Shriek")
    print("")

def print_targets():
    print("Targets:")
    print("Ogre")
    print("Imp")
    print("Zombie")
    print("Skeleton")
    print("Lesser Angel")
    print("Mindflayer")
    print("Arch-Demon")

def leveling():
    valid = False
    while valid == False:
        try:
            level = int(input("Please input your mage level. (1-20): "))
        except ValueError:
            print("Not within bounds.")
            print("")
            continue
        if level > 20 or level < 1:
            print("Not within bounds.")
            print("")
            continue
        else:
            valid = True
            return level

def spell_selection(level):
    change_spell = "Y"
    while change_spell == "Yes" or change_spell == "yes" or change_spell == "y" or change_spell == "Y":
        print_spells()
        selection = input("Select a Spell: ")
        if selection == "Fireball" or selection == "fireball":
            spell = Fireball
        elif selection == "Eldritch Blast" or selection == "eldritch blast" or selection == "Eldritch blast" or selection == "eldritch Blast":
            spell = Eldritch_Blast
        elif selection == "Radiance" or selection == "radiance":
            spell = Radiance
        elif selection == "Psychic Shriek" or selection == "psychic shriek" or selection == "Psychic shriek" or selection == "psychic Shriek":
            spell = Psychic_Shriek
        elif selection == "debug":
            spell = debug
        else:
            print("")
            print("Please pick a listed spell.")
            continue
        spellwork(spell, level)
        change_spell = input("Do you want to try a different spell? Y/N: ")

def spellwork(spell, level):
        spell_info(spell)
        cast = input("Cast this spell? Y/N: ")
        if cast == "Yes" or cast == "Y" or cast == "yes" or cast == "y":
            active_enemy = "Y"
            while active_enemy == "Yes" or active_enemy == "yes" or active_enemy == "y" or active_enemy == "Y":
                print_targets()
                target = input("Choose a Target: ")
                if target == "Ogre" or target == "ogre":
                    Ogre = enemies.Enemies("Ogre", 50, 5, 50, 30, 120)
                    test_time(spell, Ogre, level)
                elif target == "Imp" or target == "imp":
                    Imp = enemies.Demon("Imp", 5, 30, 5, 50, 10)
                    test_time(spell, Imp, level)
                elif target == "Zombie" or target == "zombie":
                    Zombie = enemies.Undead("Zombie", 20, 7, 20, 80, 40)
                    test_time(spell, Zombie, level)
                elif target == "Skeleton" or target == "skeleton":
                    Skeleton = enemies.Undead("Skeleton", 10, 20, 15, 25, 30)
                    test_time(spell, Skeleton, level)
                elif target == "Lesser Angel" or target == "lesser angel" or target == "Lesser angel" or target == "lesser Angel":
                    Lesser_Angel = enemies.Holy("Lesser Angel", 20, 40, 30, 100, 1000)
                    test_time(spell, Lesser_Angel, level)
                elif target == "Mindflayer" or target == "Mind Flayer" or target == "mindflayer" or target == "mind flayer" or target == "Mind flayer" or target == "mind Flayer":
                    Mindflayer = enemies.Psychic("Mindflayer", 20, 15, 40, 50, 90)
                    test_time(spell, Mindflayer, level)
                elif target == "Arch-Demon" or target == "Arch-demon" or target == "arch-demon" or target == "arch-Demon" or target == "archdemon" or target == "Archdemon" or target == "Arch Demon" or target == "Arch demon" or target == "arch demon" or target == "arch Demon":
                    Arch_Demon = enemies.Demon("Arch-Demon", 70, 40, 90, 60, 300)
                    test_time(spell, Arch_Demon, level)
                else:
                    print("")
                    print("Please pick a listed target.")
                    continue
                active_enemy = input("Do you want to continue testing with this spell? Y/N: ")

def test_time(spell, enemy, level):
    another_cast = input("Cast? Y/N: ")
    while another_cast == "Yes" or another_cast == "Y" or another_cast == "yes" or another_cast == "y":
        spell.cast(enemy, level)
        print(f"The {enemy.name} has {enemy.vitality} health remaining!")
        enemy.is_exhausted()
        if enemy.is_alive() == False:
            break
        another_cast = input("Again? Y/N: ")


print("Virtual Grimoire")
print("Version 0.0.1")
print("")
print("-------------------------------------------------------------------------------")
print("")

level = leveling()

spell_selection(level)

print("Thank you for trying out the Virtual Grimoire!")

