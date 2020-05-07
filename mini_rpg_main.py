"""
Mini text-based role-playing game for practising OOP programming concepts.

Aim of this game to get 3 friends, most of the time you have to fight with them to become friendly. 
Possible commands to move the player from room to room are north, south, west, east. Other commands talk, fight, check, backpack.
"""
# import Room, Items and Characters for the game
from mini_rpg_room import Room
from mini_rpg_items import Items
from mini_rpg_characters import Characters
from mini_rpg_characters import Enemy
from mini_rpg_characters import Friend

# Set the basic properties of rooms
kitchen = Room("Kitchen")
kitchen.set_description(
    "Nice, cosy warm place with a fireplace. Freshly baked bread is smelling"
)

# print(kitchen.get_description())

dininghall = Room("Dining Hall")
dininghall.set_description(
    "Small room with a table and 12 seats. It is really crowded."
)

ballroom = Room("Ballroom")
ballroom.set_description("Huge room with mirrors and windows.")

garden = Room("Garden")
garden.set_description("Huge garden with a lof of flowers")

kitchen.link_room(dininghall, "south")
dininghall.link_room(kitchen, "north")
dininghall.link_room(ballroom, "west")
ballroom.link_room(dininghall, "east")
garden.link_room(ballroom, "south")
ballroom.link_room(garden, "north")

# kitchen.describe()
# kitchen.get_details()
# dininghall.get_details()
# ballroom.get_details()

# Add characters to the game
dave = Characters("Dave", "A chef")
# dave.describe()
kitchen.set_character(dave)
dave.set_conversation("Hello, are you hungry?")

fred = Enemy("Fred", "Angry and hungry Cat")
fred.set_conversation("Mrrr, Mheeew")
fred.weakness = "cheese"
dininghall.set_character(fred)

bred = Enemy("Bred", "Enormous, frigtening dog")
bred.set_conversation("Wuffff")
bred.set_weakness("sausage")
ballroom.set_character(bred)

jim = Friend("Jim", "6 years old boy")
jim.set_interest("apple pie")
garden.set_character(jim)

# Add items to the game

apple_pie = Items("apple pie")
ballroom.set_item(apple_pie)

cheese = Items("cheese")
kitchen.set_item(cheese)

sausage = Items("sausage")
dininghall.set_item(sausage)

flower = Items("Flower")
garden.set_item(flower)

# Set the starting point of the game and add possibilty to act
current_room = kitchen
backpack = []
friend = 0

while friend < 3:
    print("Number of friends: " + str(friend))
    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

        if isinstance(inhabitant, Friend) == True:
            friend += 1
            print("You have a new friend")

    local_item = current_room.get_item()

    if local_item is not None:
        local_item.describe()

    command = input("> ")
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)

    elif command == "talk":
        inhabitant.talk()
    elif command == "check":
        if current_room.item is not None:
            # print(local_item.name)
            backpack.append(local_item.name)
            current_room.set_item(None)
            print(backpack)
        else:
            print("Nothing left")

    elif command == "backpack":
        print(backpack)

    elif command == "fight":
        print(backpack)
        if backpack == []:
            print("You are not able to fight")

        else:
            fight_with = input("What would you like to use?>")
            inhabitant.fight(fight_with)
            if fight_with == inhabitant.weakness:
                # backpack.pop()
                friend += 1
                inhabitant.description = "Friendly and nice"
    else:
        print(
            "Please write valid command: north, south, east, west, talk, check, fight, backpack"
        )

else:
    print("You won the game")
