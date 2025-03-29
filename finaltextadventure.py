import random

global decision1, decision2
global exit
global health
decision1 = ""
decision2 = ""
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
global Room
Room = 0

# Health = 1.5 X Const
# Damage Bonus = 0.25 X Strength
# Dodge Chance = 3 X Dex
# Magic Damage Bonus = 0.25 X Magic

def entranceroom(decision1,Stats,Inventory,Room):
    Room = 1
    print("You wake up in a small, cold room, unaware of your whereabouts. You don't know how you got here, or how to get out. Behind you, you see what appears to be a blocked off exit - or entrance, which it is, you are not sure of. To your left and right, you see doorframes without a door leading to adjoining rooms. In front of you, you see a sign that reads 'Welcome to the Dungeon.'.")
    print("Health: " + str(health))
    while Room == 1:
        decision1 = input("What do you want to do? Make sure to enter in your decisions as shown. \nGo Right \nGo Left \nCheck Stats \nOpen Inventory")
        if decision1 == "Open Inventory":
            print(str(Inventory))
        elif decision1 == "Check Stats":
            print(str(Stats))
        elif decision1 == "Go Right" or decision1 == "Go Left":
            return decision1
            break
        else:
            print("You have entered an invalid answer.")

def room2(decision2,Stats,Inventory,Room):
    Room = 2
    print("Walking into the room on the left, it appears similar to the room you just came from, though there are a few differences. First off, you cann see what appears to be a small, possibly locked chest sitting in the back of the room, as far away from the door as can be. As well as that, you can see a door to your right, though you cannot see very far into it.")
    print("Health: " + str(health))
    while Room == 2:
        decision2 = input("what do you want to do? Make sure to enter in your decisions as shown. \nGo Right \nCheck Chest \nCheck Stats \nOpen Inventory")
        if decision2 == "Open Inventory":
                print(str(Inventory))
        elif decision2 == "Check Stats":
            print(str(Stats))
        elif decision2 == "Go Right":
            return decision2
            break
        else:
            print("You have entered an invalid answer.")

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
    entranceroom(decision1,Stats,Inventory,Room)
    if entranceroom == "Go Right":
        print("placeholder")
    elif entranceroom == "Go Left":
        room2(decision2,Stats,Inventory,Room)

    