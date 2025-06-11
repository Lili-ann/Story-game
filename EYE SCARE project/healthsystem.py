#Creating class for player's Health system (HP)
class HealthSystem:
#Defining the player's HP which is 100 and maximum health = 100
#player's HP wont exceed 100  
    def __init__(self, name, health=100, maxhealth = 100): 
        
#Initialize the player's name 
        self.name = name
        self.maxhealth = maxhealth
#initialize player's current health
        self.health = health

#function for player healing, if the player gets increased HP,
#then we make use of this function to increase Player's HP
#when we call this function we can increase the player's HP, by a specific amount.
    def heal(self, amount):         
        self.health += amount
        if self.health > self.maxhealth:
            self.health = self.maxhealth
        print(f"\nYour anklet beeps: {self.name} healed {amount}% health and now has {self.health}% HP!")

#function for player DAMAGE, if the player gets decreased HP,
#then we make use of this function to decrease Player's HP  
#when we call this function we can decrease the player's HP, by a specific amount.
    def damage(self, amount):         
        self.health -= amount
#setting for if player's health is less than 0 then assign 0 to player's HP
        if self.health < 0:
            self.health = 0
            return self.health
        print(f"\nYour anklet beeps: {self.name} took {amount}% damage and now has {self.health}% HP!")
 #EXAMPLE         Your anklet beeps: {lilian} took {40}% damage and now has {60}% HP!
            
    def itemused(self, item):            # Items / scenarios that would inc/dec HP
    #CHECKS IF ITEM CALLED IS "PHYSICAL EXERTION"
        if item == "Physical Exertion": 
            # DAMAGES THE PLAYER BY -10 HP    
            self.damage(10)                       # numbers gets passed into damage function as amount parameter   
        if item == "Monster Attack":                 # Check if item called is "monster Attack"
            #DAMAGES THE PLAYER BY -12 HP
            self.damage(12)
        if item == "Critical Attack":
            self.damage(20)
        if item == "Bandage":
            #HEALS THE PLAYER BY +10 HP
            self.heal(15)
        if item == "HP_pay":
            self.damage(25)
     
     #function for resetting Player's HP       
    def resethealth(self):          # Reset HP to max
        #setting player's HP to 74
        self.health = 74
        return self.health      #returns the player's health       

#To check if a player is alive 
    def alive(self):            # Player alive as long as health > 0
        return self.health > 0
 
 
    def __str__(self):          # Display health
        return f"\n{self.name} has {self.health}% HP."


# main()