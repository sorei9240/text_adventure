#import os to clear console
#import time for delayed text
import os
import time 
os.system('cls')#clears console

#Welcome message
print("Welcome brave adventurer! Within these walls lies treasure... and a ferocious beast.")
time.sleep(1.5)#delays text for more immersive experience
print("Many have perished at the hands of the beast, will you be the next?")
time.sleep(1.5)
print("Good luck.")
time.sleep(2)

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
    time.sleep(1.5)
    #checks to see if player has already visited the room
    if "sword" not in player_inventory:
        print("You see a reflection off of something in the corner.")
        time.sleep(1.5)
        print("You move towards it...")
        time.sleep(1.5)
        print("""

         />_________________________________
[########[]_________________________________>
         \>
 
      
            """)
        print("It's a sword! You pick it up and head back to the entrance chamber.")
        time.sleep(1.5)
        player_inventory.append("sword") #adds sword to inventory
    #lets player know they've already visited this room
    else:
        print("There's nothing else for you to collect in this room.")
        time.sleep(1.5)

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
        print("You enter into the room, hear a roar and see a flash of light.")
        time.sleep(1.5)
        print("There is a dragon in the room!")
        time.sleep(1.5)
        #checks to see if player has the sword to battle the dragon
        if "sword" in player_inventory:
            print("You raise your sword and prepare for battle.")
            time.sleep(1.5)
            #dragon battle action, for each swing of sword dragon loses hp. 
            while True:
                if dragon_hp > 0: #checks for remaining hp
                    swing = input("Press [A] to swing your sword!\n").upper()
                    if swing == "A":
                        dragon_hp += -1
                    else:
                        print("invalid input, please press [A] to attack")      
                else: #sequence for when dragon hp is at 0
                    os.system('cls')
                    print("You defeated the dragon!")
                    time.sleep(1.5)
                    print("You see a small metal object under it's tail.")
                    time.sleep(1.5)
                    print("""

     8 8 8 8                     ,ooo.
     8a8 8a8                    oP   ?b
    d888a888zzzzzzzzzzzzzzzzzzzz8     8b
     `""^""'                    ?o_o_oP'



                    """)
                    print("It's a key! You put the key in your pocket and leave.")
                    time.sleep(1.5)
                    player_inventory.append("key") #adds key to inventory
                    break
        else: #dragon defeats player if they haven't got the sword to battle
            os.system('cls')
            print("The dragon roasts you with his flames and eats you for lunch.")
            time.sleep(1.5)
            print("Game over...")
            time.sleep(2)
            print("One of the ancient gods takes pity on you and sends your soul back to the entrance chamber.")
            time.sleep(1.5)
            player_inventory.clear() #clears inventory and sends player back to start
    #lets player know they've already visited this room
    else: 
        print("There's nothing else for you to collect in here.")
        time.sleep(1.5)

#west room function
def west_room():
    #sets west and north steps back to zero
    global west
    west = 0
    global north
    north = 0
    print("You come to a door. You try to turn the handle but it doesn't budge.")
    time.sleep(1.5)
    print("Looks like you need a key.")
    time.sleep(1.5)
    #checks to see if key is in inventory
    if "key" in player_inventory:
        print("You take the key out of your pocket and put it into the keyhole.")
        time.sleep(1.5)
        print("The lock clicks and the door opens with a creak.")
        time.sleep(1.5)
        print("The room is dimly lit")
        time.sleep(1.5)
        print("You look around and see a chest.")
        time.sleep(1.5)
        print("""

         __________                                      
        /\____;;___\                                     
       | /         /    
       `. ())oo() .                                      
        |\(%()*^^()^\       
       %| |-%-------|                                    
      % \ | %  ))   |                                    
      %  \|%________|                                    
      

        """)
        print("You open the chest and find its full of gold coins and gems!")
        time.sleep(1.5)
        player_inventory.append("treasure") #adds treasure to inventory to trigger win game sequence
    #player is unable to open the door until they've collected the key
    else:
        print("You turn back.")
        time.sleep(1.5)

#main game sequence
print("You enter a dark room. Which way do you choose to go?")
time.sleep(1.5)
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
            os.system('cls')
            north_room()
    elif steps == "R":
        east += 1 
        west += -1 #subtracts from opposite step counter for more realistic travel
        print("Walking towards the right side of the room.")
        if east > 2: 
            os.system('cls')
            east_room()
    elif steps == "L":
        west += 1
        east += -1
        print("Walking towards the left side of the room.")
        if west > 2:
            os.system('cls')
            west_room()
    else:
        print("invalid input")