#importing funtions from specific modules we created
from choicedisplay import player_choice_1, get_choicesstart, player_choice_2, player_choice_3, player_choice_1_1
from choicedisplay import player_choice_1_2, get_weaponchoice, monster_2, box_room, player_choice1_2_1, player_choice1_2_2,letter2
from choicedisplay import player_choice1_3_1, player_choice1_3_2, player_choice1_4_1, player_choice1_4_2, ending1, ending2, ending1_2
from healthsystem import HealthSystem
from itemsystem import weapon, itemused

#function for operating player's choices
def handle_choice(player_name):
    player = HealthSystem(player_name) # Creating object from class HealthSystem
    while True:                         # Control function to exit out of the loop when needed
        choicesstart = get_choicesstart() # Set variable for input from user for choice 1/2/3

        if choicesstart == 1:  # choice 1
            begin_choice = player_choice_1()  # Set variable for input from user for choice 1.1 / 1.2
            if begin_choice == 1:
                player_choice_1_1() # Scenario 1.1 
                item = "Physical Exertion"
                player.itemused(item)   # Decrease in HP function from healthsystem
                print("\nAt the center of the hallway there were items laid on a table: a flashlight, and crowbar.")
                print()
                weapon_choice = get_weaponchoice()  # Tools choice
                itemused(weapon_choice)     # Scenario for each tool choice
                if weapon_choice == 'both items':    # ending 3
                    player.resethealth()    # Reset health to max after ending 
                    return      # Exiting from function, going back to maingame.py
                            
            if begin_choice == 2:   
                player_choice_1_2()    # Scenario 1.2               
                print()                
                weapon_choice = get_weaponchoice()   # Tools choice
                itemused(weapon_choice)         # Scenario for each tool choice 
                if weapon_choice == 'both items':       # ending 3
                    player.resethealth()    # Reset health to max after ending
                    return              # Exiting from function, going back to maingame.py
                
            monster_2()  # Monster scenario if crowbar OR flashlight
            print(f"You used {weapon_choice} to fight the monster..")
            
            if weapon_choice == 'crowbar':      # Scenario if crowbar
                print(f"You grip the {weapon_choice} tightly, bracing yourself as the creature charges.",
                        "You swing with all your might, striking its head.",
                        "The creature snarls and claws at you, but a second blow knocks it to the ground.")
                item = "Monster Attack"
                player.itemused(item)   # Decrease in HP function from healthsystem
                
            elif weapon_choice == 'flashlight':     # Scenario if flashlight
                print(f"You flick on the {weapon_choice} and shine it directly at the creature's face.",
                        "It screeches, shielding its eyes as it stumbles backward. Taking the chance, you sprint down the hallway.")
                item = "Critical Attack"
                player.itemused(item)   # Decrease in HP function from healthsystem
                                    
            optstart = box_room()          # Box room scenario AND choice 1.2.1 / 1.2.2                    
            if optstart == 1:              # Choice 1.2.1
                print("You search the room and underneath a pile of rubble in the corner, you find a bandage.")
                item = "Bandage"
                player.itemused(item)       # Increase in HP function from healthsystem
                player_choice1_2_1()    # Scenario 1.2.1
                print() 
                            
            if optstart == 2:          # Choice 1.2.2
                print("\nYou tap your anklet and with a soft click the lid opens. Inside,")
                print("you find a rusted key… and suddenly, the anklet on your leg beeps sharply,", 
                      "signaling a change in your HP.")
                item = "HP_pay"
                player.itemused(item)       # Decrease in HP function from healthsystem
                player_choice1_2_2()        # Scenario 1.2.2
                print() 
            ending1()       # Continuation regardless of path 1.2.1 or 1.2.2
            ending1_2()     # Continuation
            print()
            endingbegin = letter2()            # Choice 1.3.1 / 1.3.2
            if endingbegin == 1:           
                player_choice1_3_1()           # Scenario 1.3.1
                print()           
            if endingbegin == 2:           
                player_choice1_3_2()            # Scenario 1.3.2
                print()
                
            storygameend = ending2()            # Continuation regardless of path 1.3.1 or 1.3.2 AND Choice 1.4.1 / 1.4.2
            if storygameend == 1:
                player_choice1_4_1()        # Ending 4
                print("\n\nYou have unlocked ending 4/5.")
                player.resethealth()        # Reset health to max after ending
                return                      # Exiting function going back to maingame.py
            if storygameend == 2:
                player_choice1_4_2()        # Ending 5
                print("\n\nYou have unlocked ending 5/5.")
                player.resethealth()        # Reset health to max after ending
                return                      # Exiting function going back to maingame.py
           
        elif choicesstart == 2:             # Choice 2
            player_choice_2()               # Ending 1
            print("\n\nYou have unlocked ending 1/5.")
            player.resethealth()            # Reset health to max after ending
            return                          # Exiting function going back to maingame.py
        elif choicesstart == 3:             # Choice 3
            player_choice_3()               # Ending 2
            print("\n\nYou have unlocked ending 2/5.")
            player.resethealth()            # Reset health to max after ending
            return                          # Exiting function going back to maingame.py



# ending 1: choice 2
# ending 2: choice 3
# ending 3: choice 1, choice 1.1 or 1.2, weapon flashlight AND crowbar
# ending 4: choice 1, choice 1.1 or 1.2, weapon flashlight OR crowbar, choice 1.1.1 or 1.2.1, choice 1.3.1 or 1.3.2, choice 1.4.1 
# ending 5: choice 1, choice 1.1 or 1.2, weapon flashlight OR crowbar, choice 1.1.1 or 1.2.1, choice 1.3.1 or 1.3.2, choice 1.4.2