import time
#creating a class for the collection of tools
class weapons:
    def __init__(self):     # Initializes attributes of object as an empty (list)
        self.tools = []     # self used to create an object which is an instance of a class
        #self.tools - so tools will be passed on to ther
    
    def add_tool(self, tool):           # Adding tools according to player's input and gets saved to the tool collection
        self.tools.append(tool)

    def get_tools(self):            # Returns the collection of tools the player inputs
        return self.tools
    
#Create an instance(obeject) for the Weapons class above
weapon = weapons()          # Setting weapon as object 

#function to print text using a delay between each character
def slow_text(text, delay=0.01):           # Delay is how long the text should slow down
    # Printing text with a delay between each character (fast)
    """Prints text with a delay between each character."""
    for char in text:
        print(char, end="", flush=True)         # Flush is to slow down each character being printed (buffered)
        time.sleep(delay)
    print()

#function for handling player's tool/weapon choice and
#for different scenarios upon user inputting tool of choice
def itemused(weapon_choice):            
    global weapon             # weapon variable taken from outside of the function
    while True:            # Control function to exit out of the loop when needed
#check if player chose Flashlight
        if weapon_choice == "flashlight":
            weapon.add_tool("Flashlight")         # Adds flashlight to the collection of tool (object)
#text for printing the player's tool choice         
            slow_text("\nYour Anklet beeps: ")
            slow_text("\n\"Flashlight acquired. But beware—your path is now dimly lit and fraught with unseen dangers.\"")
#check if player chose Crowbar
        elif weapon_choice == "crowbar":
            weapon.add_tool("Crowbar")          # Adds crowbar to object
            slow_text("\n\"Crowbar acquired. Strength will guide your path, but beware what you can't see may still harm you\"")
            slow_text("\nYou gain a weapon but lose the ability to see clearly, making navigation harder.")
#check if player chose both items
        elif weapon_choice == "both items":
            # prints text for ending 3
            slow_text("\nYou grab the flashlight first. Then, with your other hand, you reach for the crowbar."
            "\nThe moment your fingers curl around the crowbar, a loud alarm blares from your anklet."
            "\n\n\"Rule violated: One item only. Penalty: Immediate termination.\""
            "\n\nBefore you can react,the anklet emits a high-pitched whine and a searing pain shoots through your leg"
            "\nYou drop the crowbar and flashlight as your muscles seize."
            "\nThe pain spreads rapidly through your body, and your vision blurs"
            "\nThe room fades into darkness as the house claims its latest victim.")
            print("\n\nYou have unlocked ending 3/5.")
            return                  # Exiting from function, going back to choicesystem.py
        

        return              # Exiting from function, going back to choicesystem.py