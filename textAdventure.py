print("Welcome adventurer! Within these walls lies treasure... and a ferocious beast.")
print("Many have perished at the hands of the beast, will you be the next?")
print("Good luck.")

north = 0
west = 0
east = 0
player_inventory = []

def north_room():
    global west 
    west = 0
    global east
    east = 0
    global north 
    north = 0
    print("You enter a room gently lit by torchlight.")
    if "sword" not in player_inventory:
        print("You see a reflection of light off of something in the corner.")
        print("You move towards it...")
        print("It's a sword! You pick it up and head back to the entrance chamber.")
        player_inventory.append("sword")
    else:
        print("There's nothing else for you to collect in this room.")

def east_room():
    global east
    east = 0
    global north
    north = 0
    dragon_hp = 7
    if "key" not in player_inventory:
        print("You enter into the room and hear a roar and see a flash of light.")
        print("There is a dragon in the room!")
        if "sword" in player_inventory:
            print("You raise your sword and prepare for battle.")
            while True:
                if dragon_hp > 0:
                    swing = input("Press [A] to swing your sword!\n").upper()
                    if swing == "A":
                        dragon_hp += -1
                    else:
                        print("invalid input, please press [A] to attack")      
                else:
                    print("You defeated the dragon!")
                    print("You see a small metal object under it's tail.")
                    print("It's a key! You put the key in your pocket and leave.")
                    player_inventory.append("key")
                    break
        else:
            print("The dragon roasts you with his flames and eats you for lunch.")
            print("Game over...")
            print("One of the ancient gods takes pity on you and sends your soul back to the entrance chamber.")
            player_inventory.clear()
    else:
        print("There's nothing else for you to collect in here.")

def west_room():
    global west
    west = 0
    global north
    north = 0
    print("You come to a door. You try to turn the handle but it doesn't budge.")
    print("Looks like you need a key.")
    if "key" in player_inventory:
        print("You take the key out of your pocket and put it into the keyhole.")
        print("The lock clicks and the door opens with a creak.")
        print("The room is dimly lit")
        print("You look around and see a chest.")
        print("You open the chest and find its full of gold coins and gems!")
        player_inventory.append("treasure")
    else:
        print("You turn back.")


print("You enter a dark room. Which way do you choose to go?")
while True: 
    if "treasure" in player_inventory:
        print("Congratulations, You've won the game!")
        break
    steps = input("Please enter [S] for straight, [R] for right, or [L] for left: \n").upper()
    if steps == "S":
        north += 1
        print("Walking straight forward.")
        if north > 2:
            north_room()
    elif steps == "R":
        east += 1
        west += -1
        print("Walking towards the right side of the room.")
        if east > 2:
            east_room()
    elif steps == "L":
        west += 1
        east += -1
        print("Walking towards the left side of the room.")
        if west > 2:
            west_room()
    else:
        print("invalid input")