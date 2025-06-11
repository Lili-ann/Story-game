import time
from choicesystem import handle_choice, get_weaponchoice
from choicedisplay import player_choice_1, get_choicesstart, player_choice_2, player_choice_3

def slow_text(text, delay= 0.051
              ):        # Delay is how long its slowed down
    # Printing text with a delay between each character (fast)
    for char in text:
        print(char, end="", flush=True)     # Flush is to slow down each character being printed (buffered)
        time.sleep(delay)
    print()

def slow_text_name(text, delay= 0.3):
    # Printing text with a delay between each character (slow)
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

#prints title of the game
def title_name():
    # Title  
    slow_text_name("\n\\\\Eye Scare\\\\")
    print("Answers are case sensitive, please follow the instructions carefully.\n\n")
    time.sleep(1)

def intro():
    # Introduction
    slow_text("\n\nYou wake up in a dark and gloomy room. As your eyes adjusted to the dim light filtering through the cracks in the wooden walls,"
              "\nyou realized your hands were tightly bound with a rope."
              "\nYou scanned the room, the house was old, creaking in silence,"
              "\nDust floated in the thick air, around you,"
              "\nold and filthy furniture loomed like ghostly shadows:"
              "\na broken rocking chair swayed slightly in the corner, and a crumbling cabinet"
              "\nleaned against the wall as if moved by an unseen force."
              "\nWhen you shifted slightly, you realized there was a metallic anklet device clasped tightly around your leg"
              "\nA glowing number 74 displayed on it,"
              "\nStill unsure of what it means, you tried tugging at it, but the device didn't budge.")
# this pause the program from running for 1 seecond
    time.sleep(1)

def intro2():
    # Introduction part 2
    slow_text("\n\nAfter a while of tugging at the anklet, frustration and fatigue began to set in."
              "\nYou reached for one of the broken glass pieces on the floor to cut the rope."
              "\nThen you move towards the door, it was locked."
              "\nSo, you think to find the key first to leave the room."
              "\nAs your eyes swept the room, something caught your attention"
              "\na piece of paper lying on the overturned table, as you got closer, the object became clear:")
    time.sleep(1)

def letter(player_name):
    # Letter 1
    slow_text(f"\n\"Welcome {player_name}\"") 
    slow_text("\n\"You are not here by chance. The device on your ankle is your lifeline, your health."
              "\nThe number you see will drop with every wrong move, and when it reaches zero…\nSo will you..."
              "\n\nThis house is alive, watching, and unforgiving. To escape, you must uncover its secrets."
              "\nBut beware! it feeds on your fear, and it will test you at every turn."
              "\nThere are no allies here, only choices. Choose wisely, or the house will choose for you."
              "\nNot all who play survive."
              "\nEscape if you can...\""
              "\n\nThe anklet device flickered briefly, Then a voice  came from the anklet:"
              "\n\"Game Start.\""
              "\nAnother beep followed and the device grew still again. As if daring you to make your first move.")

    time.sleep(1)

#function for game conclusion
def conclusion(player_name):
    # Conclusion
    slow_text("\nThe story ends with the realization that every obstacle symbolized a piece of the player's trauma and guilt."
              "\nThe illusionary horrors were their subconscious mind's way of processing their struggles."
              "\nUltimately, the player's choice to face or avoid these challenges determines their emotional state upon waking:")
    slow_text_name("\n\"Hopeful and ready to heal, or burdened by unresolved pain.\"")
    slow_text_name(f"\nCongratulations {player_name}!")

def main():
    # importing all other modules and functions here 
    start = 'y'
    while start == 'y': #loop for users to retry a different ending
        player_name = input("\n\n\nEnter Your name: ")        #gets Player name 
        title_name()   #prints game Title
        intro()        #prints intro
        intro2()       #prints the folloeing scene (the letter)
        slow_text_name("A LETTER")
        slow_text("You opened the letter and met with the writing.")
        letter(player_name)
        handle_choice(player_name)
        conclusion(player_name)   #prints game conclusion
        start = input("Would you like to play again? (y/n): ")      
        # If user wants to retry
    else:
        print(f"\n\n\nThanks for playing {player_name}")
        exit()

main()