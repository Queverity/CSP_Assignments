import random

global decision
global exit
global health
decision = ""
exit = ""
health = 0
Fighter = {"Strength": 15, "Dexterity": 10, "Constitution": 10, "Magic": 10}
Rouge = {"Strength": 10, "Dexterity": 15, "Constitution": 10, "Magic": 10}
Tank = {"Strength": 10, "Dexterity": 10, "Constitution": 15, "Magic": 10}
Wizard = {"Strength": 10, "Dexterity": 10, "Constitution": 10, "Magic": 15}
global Inventory
Inventory = ["Sword: It's a sword.", "Arcane Focus: You get to choose what it is.", "Shield: Tis' a shield."]
global Stats
Stats = {}

# Health = 1.5 X Const
# Damage Bonus = 0.25 X Strength
# Dodge Chance = 3 X Dex
# Magic Damage Bonus = 0.25 X Magic
def inventory(Inventory, exit):
    print(str(Inventory))
    exit = input("Type 'Exit' when you would like to return to the game.")
    if exit == "Exit":
        print("placeholder")
    else:
        print("placeholder")

def stats(Stats, exit):
    print(str(Stats))
    exit = input("Type 'Exit' when you would like to return to the game.")
    if exit == "Exit":
        print("placeholder")
    else:
        print("placeholder")


def entranceroom(decision):
    print("You wake up in a small, cold room, unaware of your whereabouts. You don't know how you got here, or how to get out. Behind you, you see what appears to be a blocked off exit - or entrance, which it is, you are not sure of. To your left and right, you see doorframes without a door leading to adjoining rooms. In front of you, you see a sign that reads 'Welcome to the Dungeon.'.")
    print("Health: " + str(health))
    decision = input("What do you want to do? Make sure to enter in your decisions as shown. \nGo Right \nGo Left \nCheck Stats \nOpen Inventory")
    if decision == "Open Inventory":
        inventory(Inventory, exit)
    elif decision == "Check Stats":
        stats(Stats, exit)
    else:
        return decision

while True:
    print("Stat Explanation")
    print("Strength (Fighter): Determines damage bonus. \nDexterity (Rouge): Determines dodge chance. \nConstitution (Tank): Determines health. \nMagic (Wizard): Determines magical damage." )
    Class = input("Welcome to my text adventure game! \nYou can choose between four different classes, each with different stats. Would you like to play the Fighter, Rouge, Tank, or Wizard?")
    if Class == "Fighter":
        Stats = Fighter
        health += 1.5 * Stats["Constitution"]
    elif Class == "Rouge":
        Stats = Rouge
        health += 1.5 * Stats["Constitution"]
    elif Class == "Tank":
        Stats = Tank
        health += 1.5 * Stats["Constitution"]
    elif Class == "Wizard":
        Stats = Wizard
        health += 1.5 * Stats["Constitution"]
    entranceroom(decision)
    if decision == "Go Right":
        print("placeholder")
    elif decision == "Go Left":
        print("placeholder")

    