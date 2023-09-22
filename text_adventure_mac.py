#import os to clear console
#import time for slow_print
import os
import time 
os.system('clear')
import time

def slow_print(text, delay=0.04):
    lines = text.splitlines()  # Split the text into lines
    for i, line in enumerate(lines):
        if i > 0:
            print()
        line = line.lstrip()  # Add a newline before each line except the first
        for char in line:
            print(char, end='', flush=True)
            time.sleep(delay)
    print() #adds line break between messages



#Welcome message
welcome_message = """Welcome brave adventurer! 
Within these walls lies treasure... 
and a ferocious beast.
Many have perished at the hands of the beast, will you be the next?
Good luck."""
slow_print(welcome_message)

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
    enter_north = "You enter a room gently lit by torchlight."
    slow_print(enter_north)
    #checks to see if player has already visited the room
    if "sword" not in player_inventory:
        found_sword = """You see light reflect off of something in the corner.
        You move towards it..."""
        slow_print(found_sword)
        print("""

         />_________________________________
[########[]_________________________________>
         \>
 
      
        """)
        collect_sword = """It's a sword! You pick it up and head back to the entrance chamber."""
        slow_print(collect_sword)
        player_inventory.append("sword") #adds sword to inventory
    #lets player know they've already visited this room
    else:
        no_items = "There's nothing else for you to collect in this room."
        slow_print(no_items)

#east room function
def east_room():
    #sets north and east steps back to zero
    global east
    east = 0
    global north
    north = 0
    #hit points counter for dragon battle
    dragon_hp = 5
    #checks to see if player has already visited the room
    if "key" not in player_inventory:
        dragon = """You enter into the room, hear a roar and see a flash of light.
        There is a dragon in the room!"""
        slow_print(dragon)
        #checks to see if player has the sword to battle the dragon
        if "sword" in player_inventory:
            battle = "You raise your sword and prepare for battle."
            slow_print(battle)
            #dragon battle action, for each swing of sword dragon loses hp. 
            while True:
                if dragon_hp > 0: #checks for remaining hp
                    swing = input("Press [A] to swing your sword!\n").upper()
                    if swing == "A":
                        dragon_hp += -1
                    else:
                        invalid = "invalid input, please press [A] to attack"
                        slow_print(invalid)      
                else: #sequence for when dragon hp is at 0
                    os.system('clear')
                    dragon_slayer = """You defeated the dragon!
                    You see a small metal object under it's tail."""
                    slow_print(dragon_slayer)
                    print("""

     8 8 8 8                     ,ooo.
     8a8 8a8                    oP   ?b
    d888a888zzzzzzzzzzzzzzzzzzzz8     8b
     `""^""'                    ?o_o_oP'



                    """)
                    found_key = "It's a key! You put the key in your pocket and leave."
                    slow_print(found_key)
                    player_inventory.append("key") #adds key to inventory
                    break
        else: #dragon defeats player if they haven't got the sword to battle
            os.system('clear')
            bbq = """The dragon roasts you with his flames and eats you for lunch.
            Game over...
            One of the ancient gods takes pity on you and sends your soul back to the entrance chamber."""
            slow_print(bbq)
            player_inventory.clear() #clears inventory and sends player back to start
    #lets player know they've already visited this room
    else: 
        nothing_else = "There's nothing else for you to collect in here."
        slow_print(nothing_else)

#west room function
def west_room():
    #sets west and north steps back to zero
    global west
    west = 0
    global north
    north = 0
    need_key = """You come to a door. You try to turn the handle but it doesn't budge.
    Looks like you need a key."""
    slow_print(need_key)
    #checks to see if key is in inventory
    if "key" in player_inventory:
        unlock = """You take the key out of your pocket and put it into the keyhole.
        The lock clicks and the door opens with a creak.
        The room is dimly lit.
        You look around and see a chest."""
        slow_print(unlock)
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
        open_chest = "You open the chest and find its full of gold coins and gems!"
        slow_print(open_chest)
        player_inventory.append("treasure") #adds treasure to inventory to trigger win game sequence
    #player is unable to open the door until they've collected the key
    else:
        turn_back = "You turn back."
        slow_print(turn_back)

#main game sequence
main_seq = "You enter a dark room. Which way do you choose to go?"
slow_print(main_seq)
while True: 
    if "treasure" in player_inventory: #win game sequence, must have treasure
        congrats = "Congratulations, You've won the game!"
        slow_print(congrats)
        break #ends program because player has won
    #prompt user to choose direction
    steps = input("Please enter [S] for straight, [R] for right, or [L] for left: \n").upper()
    if steps == "S":
        north += 1 #adds to appropriate step counter
        walk_forward = "Walking straight forward."
        slow_print(walk_forward)
        if north > 2: #triggers north room sequence at 3 steps forward
            os.system('clear')
            north_room()
    elif steps == "R":
        east += 1 
        west += -1 #subtracts from opposite step counter for more realistic travel
        walk_right = "Walking towards the right side of the room."
        slow_print(walk_right)
        if east > 2: 
            os.system('clear')
            east_room()
    elif steps == "L":
        west += 1
        east += -1
        walk_left = "Walking towards the left side of the room."
        slow_print(walk_left)
        if west > 2:
            os.system('clear')
            west_room()
    else:
        print("invalid input")