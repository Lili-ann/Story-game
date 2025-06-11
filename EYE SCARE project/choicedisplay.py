#import TIME module to call SLEEP function
#SLEEP function used for creating delay
import time
# from rich import print #rich library for nice text formatting

#This function is used to print text with a delay between each character
#here we set the delay to 0.01sec
def slowtext(text, delay = 0.025):           # Delay is how long the text slows down
    # printing text with delay between each character (fast)
    for char in text:     #iterate over each character in the given text
        print(char, end="", flush = True)    
        # Flush is to slow down each character with a delay beween them, as they are being printed (buffered)
       #e.g: makes the code appear like it's being typed out
        time.sleep(delay)
    print() #allows us to move to the next line
    
# function for BEGINNING choice 1, 2, 3
def get_choicesstart(): 
    #defining the choices for the player
    choice1 = "1. Check for more clues to escape the room."
    choice2 = "2. Scream for help in hopes for someone to save you."
    choice3 = "3. Accept your faith and Stay in the room."
    #prints the choices
    print("\nWhat will you do?")
    print(choice1)
    print(choice2)
    print(choice3)
    #checking if player's choice is valid
    while True:
        #telling the player to input their choice
        opt = int(input("Enter your Choice: "))
        if opt == 1 or opt == 2 or opt == 3:
            #returns player choice
            return opt
        else:
            print("Invalid choice. Please Input 1 or 2 or 3..")
            continue
    
   
                
# function for handling player choice 1.1, if the player picks 1.
def player_choice_1():
    #prints this text if player choice = 1
    slowtext("\nYou search the wardrobes and drawers, finding them empty only filled with dust."
             "\nYou reach into the dark space beneath the bed."
             "\nAs your hand touches the metallic object - A KEY."
             "\nBut as you grip it, suddenly the air around your hand feels thick."
             "\nYou dare not move."
             "\nThe breathing grows heavier, and then… silence…")
    #prints the players next choice.
    print("\nWhat will you do?")
    print("1. Try to pull your hand back while gripping the key.")
    print("2. Take a look at what is lurking in the shadows.")
    #checking if player's choice is valid
    while True:
        choice1 = int(input("Choice (1 or 2 only): ")) #allow player to input their choice
        if choice1 == 1 or choice1 == 2:                #if player choice is not 1 or 2
            return choice1
        else:
            print("Invalid choice. Please Input 1 or 2.")   #it prints this
            continue

#function for printing the outcome for if player choice = 1 
#choice outcome 1.1
def player_choice_1_1():
    slowtext("\nYou begin to pull your hand back slowly, until a low growl erupts from beneath the bed." 
             "\nYou rush to the door and with a burst of adrenaline, you push the wardrobe down,"
             "\nblocking the creature's path. The Creature's piercing shriek erupts and begins to tremble violently."
             "\nYou sprint to the door, your fingers fumbling to insert the key. "
             "\nThe lock clicks and the door creaks open."
             "\nJust as you step into the hallway,")
    
#function for printing the outcome for if player choice = 2
# choice outcome 1.2
def player_choice_1_2():
    slowtext("\nYou lean down cautiously, the growl growing louder as your eyes adjust to the darkness."
             "\nTwo glowing red dots eyes stare back at you"
             "\nA metallic scraping sound echoes, and you realize the creature is moving closer."
             "\nScrambling back, you trip and fall onto a table. On it are a few items:"
             "\nA flashlight, and A Crowbar " )
 

# function for player weapon choice
def get_weaponchoice():   
    print("\nPlayer supply selection: Choose only one. Be warned your choice will shape your path.")
    print("- Flashlight")
    print("- Crowbar")
    print("- Both items")
    #checking if player's choice is valid
    while True:
        weaponchoice = input("Enter your choice: ").lower()   #lower() : helps ignore lowercase and uppercase text
        if weaponchoice in ["flashlight", "crowbar", "both items"]:  #check if player's weapon choice is valid
            return weaponchoice
        else:
            print("Invalid Input!!. Please input choice again....")
            continue

# function to print monster scence
def monster_2 ():
    slowtext("\nAs you move down the hallway, the air grows colder."
             "\nA low growl echoes behind you."
             "\nTurning slowly, you see the shadowy figure from before creeping toward you,"
             "\nits claws\nscraping against the walls."
             "\nYou decide to fight the monster…")
 
# function for box scene  AND choice 1.2.1 
def box_room ():
    slowtext("\nExhausted from your encounter with the creature, you stumble into another room."
             "\nThe door slams shut behind you, and the air feels heavy, almost suffocating."
             "\nThe room is bare, except for a small box, locked with a strange lock needing a password."
             "\nBeside it lies a torn note written in a hurried scrawl:"
             "\nThe key to this door lies within the box. But beware—the box demands a price.")
    print("\nWhat will you do?")
    print("1. Search the room for the answer.")
    print("2. Pay the price to open the box.")
    #checking if player's choice is valid
    while True:
        choice1_2_1 = int(input("Enter your Choice: "))
        if choice1_2_1 == 1 or choice1_2_1 == 2:   #if player choice is not 1 or 2
            return choice1_2_1
        else:
            print("Invalid choice. Please Input 1 or 2..")   #it prints this
            continue
               

#function for choice 1.2.1 outcome
def player_choice1_2_1():
    slowtext("\nYou continue to search and you notice an old photo frame facing downwards."
             "\nPicking it up, you see that the faces in the photo have been scratched out,"
             "\nleaving only the year 1988 visible. The sight fills you with uneasiness."
             "\nYou reach for the box and use the picture clue to open the box."
             "\nThe lid opens, and inside, you find a rusted key…" )
 
# functio for choice 1.2.2 outcome
def player_choice1_2_2():
    slowtext("\nAs you rush to the next door, you stumble across a picture frame, picking it up,"
             "\nyou see that the faces in the photo have been scratched out, leaving only the year 1988 visible."
             "\nThe sight fills you with uneasiness.")

# function for the next scene
def ending1():
    slowtext("\nBut, something felt off, you went back to the picture frame, and noticed…"
             "\nThat date was 10 years ago when you were still a child and were left in an orphanage by your parents."
             "\nYou look closer to the picture and notice the picture shows the same locket you have."
             "\n\"This can't be a coincidence? Can it?\""
             "\nYour thoughts get caught off by inhuman sounds coming from the previous door,"
             "\nyou quickly rush to the next door in panic"
             "\nfumbling with the key, you turn around and a more twisted and mangled creature appear."
             "\nPanicking, you push the door open and slam it shut behind you.")
    
# function for scene continuation part 2 from choices 1.1.1/1.1.2/1.2.1/1.2.2
def ending1_2():
    slowtext("\nEventually, you reach a massive door, with your name etched into it and a writing engraved on it."
             "\n\"You've survived this far. But survival is not enough. To truly escape, you must confront the truth.\""
             "\nYou slowly enter the room and the door shuts back immediately."
             "\nYou find yourself in a room with a mirror covered with a black cloth,"
             "\nand at the center lies a single folded letter and a picture faced down."
             "\nYou pick up the letter with trembling hands."
             "\nThe letter reads:")
  
    
# function for letter 2 scence AND choice 1.3.1 / 1.3.2
def letter2():
    slowtext("\n\"To the one who walks this path of shadows,"
             "\nWhat you see before you are fragments of yourself, pieces you buried to survive."
             "\nThe monsters you feared, the halls you wandered, the challenges you faced, they were never truly enemies."
             "\nThey were echoes of your past."
             "\nYour mind, fractured by pain, created this world to shield you from the truth. The truth you must now face.\""
             "\nYour gaze shifts to the covered mirror. You feel drawn to it, but your body hesitates…")
    print("\nWhat will you do?")
    print("1. Remove the black cloth from the mirror")
    print("2. Look at the picture on the table.")
    #checking if player's choice is valid
    while True:
        choice_ending1 = int(input("Enter your Choice: "))
        if choice_ending1 == 1 or choice_ending1 == 2:
            return choice_ending1
        else:
            print("Invalid choice. Please Input 1 or 2..")
            continue


# outcome 1.3.1
def player_choice1_3_1():
    slowtext("\nYou approach the large mirror, partially covered by a black cloth,"
             "\nheart racing, and you pull away the black cloth with trembling hands. "
             "\nInstead of a simple reflection, you see fractured versions of yourself,"
             "\npain, anger, fear, guilt staring back. "
             "\n\"This is the truth you buried.\"")

# outcome 1.3.2
def player_choice1_3_2():
    slowtext("\nUnable to face the mirror, you turn toward the picture on the table. "
             "\nIt's an old photo of your family, you stared in shock. "
             "\nBeneath it, a locket lies, similar to yours"
             "\nThe sight brings a rush of memories:"
             "\ntheir warmth, their absence, and the hollow ache of abandonment."
             "\n\"This was the moment it began, wasn't it? The pain you carry started here.\"")
  
# choice 1.4.1 / 1.4.2
def ending2():
    slowtext("\nTears stream down your face as the moment of realization hits, you begin to get flashbacks of your past."
             "\n\n\"The orphanage you grew up in was a place of horror."
             "\nUntil one fateful day in 1988 when everything changed."
             "\nYou remember the blood, the screams, and the lives you took in an attempt to escape your torment.\""
             "\n\n\"This necklace binds you to the past. The truth is undeniable, this place is a manifestation of your fractured mind.\""
             "\n\nThe mirror begins to glow, and the voice urges:"
             "\n\"Now, choose.\"")
    print("\nWhat will you do?")
    print("1. Keep the necklace")
    print("2. Break the Necklace and the Mirror")
    #checking if player's choice is valid
    while True:
        choice_ending2 = int(input("Enter your Choice: "))
        if choice_ending2 == 1 or choice_ending2 == 2:
            return choice_ending2
        else:
            print("Invalid choice. Please Input 1 or 2..")
            continue

# outcome 1.4.1 AND ending 4
def player_choice1_4_1 ():
    slowtext("\nClutching the necklace tightly, you face the mirror and whisper,\"I accept the truth.\""              
             "\nThe mirror shines brightly, enveloping you in light."
             "\nWhen you awaken, youre in a hospital bed, surrounded by loved ones."
             "\nThe beeping of the anklet transforms into the steady rhythm of a heart monitor."
             "\nA Nurse speaks: \"You've been in a coma, fighting for your life.\""
             "\nYou lay there in shock, unsure of what to believe. \"Was it all an illusion?\"")   

# outcome 1.4.2 AND ending 5
def player_choice1_4_2 ():
    slowtext("\nIn a surge of anger, you destroy the necklace, severing your connection to the past."
             "\nYou stride toward the mirror and you smash the mirror in rage."
             "\nThe room starts to collapse, your anklet beeps..signaling low HP, suddenly, spikes emerge, piercing your leg."
             "\nPain shoots through your body as the room distorts violently, and you fall into darkness."
             "\nA blinding light engulfs you as the room collapses."
             "\n\nYou find yourself before two doors: one old and riddled with holes, the other pure and pristine."
             "\nWithout hesitation, you choose the white door."
             "\n\nAs you step through, the light fades, replaced by endless darkness."
             "\nLaughter echoes as the monsters from your mind emerge, chasing you down."
             "\nYour screams are drowned out as they rip you apart slowly, leaving nothing but silence."
             "\nYour mind is lost, bound forever to the illusions you created.")


#choice 2 AND ending 1
def player_choice_2():
    slowtext("\nYou scream as loudly as you can, HELP!! Your voice echoes through the room"
             "\nFor a moment, there's nothing but dreadful silence. "
             "\nThen a sharp noise comes from the vent in the corner of the room. "
             "\nThe sound grows, louder and faster, a rhythmic dragging that is unmistakably coming toward you. "
             "\n\nYou scream more desperately, but your voice falters as the noise grows even closer."
             "\nYou feel a presence behind you.\nSomething large.\nSomething hungry."
             "\n\nYou turn to look, but you're too late."
             "\nA cold, leathery hand shoots out from the shadows and grabs you by the throat"
             "\nIt\'s grip impossibly strong. You gasp, the air crushed from your lungs,"
             "\nand the room spins as the creature's hot breath fills your ears. "
             "\nYou try to scream again, but your voice is swallowed by the overwhelming pressure"
             "\nand the darkness consumes you. "
            )

# choice 3  AND ending 2
def player_choice_3():
    slowtext("\nYou close your eyes and accept your fate. "
             "\nYou remain frozen, too terrified to move. The only sound is the faint scratching from the walls,"
             "\ngrowing louder as if something is digging its way closer to you."
             "\n\nThe maggots on the floor crawl over your legs"
             "\nbut you don't dare to brush them away. Your breathing becomes shallow, your pulse racing."
             "\n"
             "\nThen unexpectedly parts of the ceiling collapses."
             "\nThe brink of your life was on edge when you saw the monster enter the room."
             "\nIt\'s sharp claws sank inside the calves of your legs and "
             "\ndragged you away from the original room to the vents it came from.")
    



# ending 1: choice 2
# ending 2: choice 3
# ending 3: choice 1, choice 1.1 or 1.2, weapon flashlight AND crowbar
# ending 4: choice 1, choice 1.1 or 1.2, weapon flashlight OR crowbar, choice 1.1.1 or 1.2.1, choice 1.3.1 or 1.3.2, choice 1.4.1 
# ending 5: choice 1, choice 1.1 or 1.2, weapon flashlight OR crowbar, choice 1.1.1 or 1.2.1, choice 1.3.1 or 1.3.2, choice 1.4.2