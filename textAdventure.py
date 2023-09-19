#Welcome message
print("Welcome adventurer! Within these walls lies treasure... and a ferocious beast.")
print("Many have perished at the hands of the beast, will you be the next?")
print("Good luck.")

#step counters and inventory
north = 0
west = 0
east = 0
player_inventory = []

#north room function
def north_room():
    #set steps back to zero (won't access unless i use global)
    global west 
    west = 0
    global east
    east = 0
    global north 
    north = 0
    print("You enter a room gently lit by torchlight.")
    #checks to see if player has already visited the room
    if "sword" not in player_inventory:
        print("You see a reflection of light off of something in the corner.")
        print("You move towards it...")
        print("It's a sword! You pick it up and head back to the entrance chamber.")
        player_inventory.append("sword") #adds sword to inventory
    #lets player know they've already visited this room
    else:
        print("There's nothing else for you to collect in this room.")

#east room function
def east_room():
    #sets north and east steps back to zero
    global east
    east = 0
    global north
    north = 0
    #hit points counter for dragon battle
    dragon_hp = 7
    #checks to see if player has already visited the room
    if "key" not in player_inventory:
        print("You enter into the room and hear a roar and see a flash of light.")
        print("There is a dragon in the room!")
        #checks to see if player has the sword to battle the dragon
        if "sword" in player_inventory:
            print("You raise your sword and prepare for battle.")
            #dragon battle action, for each swing of sword dragon loses hp. 
            while True:
                if dragon_hp > 0: #checks for remaining hp
                    swing = input("Press [A] to swing your sword!\n").upper()
                    if swing == "A":
                        dragon_hp += -1
                    else:
                        print("invalid input, please press [A] to attack")      
                else: #sequence for when dragon hp is at 0
                    print("You defeated the dragon!")
                    print("You see a small metal object under it's tail.")
                    print("It's a key! You put the key in your pocket and leave.")
                    player_inventory.append("key") #adds key to inventory
                    break
        else: #dragon defeats player if they haven't got the sword to battle
            print("The dragon roasts you with his flames and eats you for lunch.")
            print("Game over...")
            print("One of the ancient gods takes pity on you and sends your soul back to the entrance chamber.")
            player_inventory.clear() #clears inventory and sends player back to start
    #lets player know they've already visited this room
    else: 
        print("There's nothing else for you to collect in here.")

#west room function
def west_room():
    #sets west and north steps back to zero
    global west
    west = 0
    global north
    north = 0
    print("You come to a door. You try to turn the handle but it doesn't budge.")
    print("Looks like you need a key.")
    #checks to see if key is in inventory
    if "key" in player_inventory:
        print("You take the key out of your pocket and put it into the keyhole.")
        print("The lock clicks and the door opens with a creak.")
        print("The room is dimly lit")
        print("You look around and see a chest.")
        print("You open the chest and find its full of gold coins and gems!")
        player_inventory.append("treasure") #adds treasure to inventory to trigger win game sequence
    #player is unable to open the door until they've collected the key
    else:
        print("You turn back.")

#main game sequence
print("You enter a dark room. Which way do you choose to go?")
while True: 
    if "treasure" in player_inventory: #win game sequence, must have treasure
        print("Congratulations, You've won the game!")
        break #ends program because player has won
    #prompt user to choose direction
    steps = input("Please enter [S] for straight, [R] for right, or [L] for left: \n").upper()
    if steps == "S":
        north += 1 #adds to appropriate step counter
        print("Walking straight forward.")
        if north > 2: #triggers north room sequence at 3 steps forward
            north_room()
    elif steps == "R":
        east += 1 
        west += -1 #subtracts from opposite step counter for more realistic travel
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