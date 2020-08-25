import sys

# Create a Pokémon class. The __init__() method of our Pokémon class created variables to keep track of the Pokémon’s:
# name, level, type (for example "Fire" or "Water"), maximum health, current health, 
# and whether or not the Pokémon was knocked out. In our implementation, the maximum health was determined by the Pokémon’s level.
class Pokemon:
    def __init__(self, name, level):
        self.name = name
        self.level = level                  
        self.health = level * 5
        self.max_health = level * 5
        self.is_knocked_out = False
    
# this is used to return infortmation in english, without this we would only retrieve a memory address
    def __repr__(self):
        return "Pokemon name: {name}, current level: {level}, type: {type}, max health: {max_health}, current health: {health}\n".format(name = self.name, level = self.level, type = self.type, max_health = self.max_health, health = self.health)

# create method to handle a pokemon being knocked out of the game
    def knocked_out(self):
        self.is_knocked_out = True
        print("Knock Out!!!  {name} Leave's The Game!".format(name = self.name))
       
# create a method that allows a pokemon to be revived (this will be called when a potion is used in the trainer class)
    def rejuvenate(self):
        if self.is_knocked_out == True:
            self.is_knocked_out = False
            self.health = self.max_health # ADDED LAST NIGHT
            print("{name} has been revived and is back in the game!!!".format(name = self.name))
        else:
            self.health = self.max_health
            print("{name} has regained health, their health now equates to {health}".format(name = self.name, health = self.health))

# create a method to calculate loss of health following an attack. (this will be called in the attack method),
# the differing level of damage are shown below.    
    def lose_health(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.knocked_out()
        else:
            print("{name} new health level is {health}".format(name = self.name, health = self.health))

# recommended to use 3 types if cards:
    # ref...https://pokemondb.net/type
    # Fire      --> Water    = Ineffective 50% Damage x
    # Fire      --> Electric = Normal 100% Damage 
    # Water     --> Fire     = Effective 200% Damage x
    # Water     --> Electric = Normal 100% Damage
    # Electric  --> Fire     = Normal 100% Damage
    # Electric  --> Water    = Effective 200% Damage x
    # Did not captured No effect = 0%, as i have not selected any of those combinations, instead i created failsafe to prevent entry of non-defined cards

# define an attack method that checks for for conditions as per above table and inflicts damage by calling lose_health on other player
    def attack(self,other_player):
        if self.is_knocked_out == True:
            return print("Can not play, this pokemon has already been knocked out")
        if self.type == 'Water' and other_player.type == 'Fire' or self.type == 'Electric' and other_player.type == 'Water':
            print("{name} has attacked {other_player} with {type}".format(name = self.name, other_player = other_player.name, type = self.type))
            print("{name} has caused damage of {damage}!!!".format(name = self.name, damage = self.level * 2))
            other_player.lose_health(self.level * 2)
        elif self.type == 'Fire' and other_player.type == 'Water' or self.type == other_player.type:
            print("{name} has attacked {other_player} with {type}".format(name = self.name, other_player = other_player.name, type = self.type))
            print("{name} has caused damage of {damage}!!!".format(name = self.name, damage = self.level * 0.5))
            other_player.lose_health(self.level * 0.5)
        elif self.type == 'Fire' and other_player.type == 'Electric' or self.type == 'Water' and other_player.type == 'Electric' or self.type == 'Electric' and other_player.type == 'Fire':       
            print("{name} has attacked {other_player} with {type}".format(name = self.name, other_player = other_player.name, type = self.type))
            print("{name} has caused damage of {damage}!!!".format(name = self.name, damage = self.level))
            other_player.lose_health(self.level)
        else:
            print("Error Card Combination has not been created or you are trying to attack yourself?")

# Super is being used for inheirance of parent class (simplified coding introduce in python3).
# this could be simplified into one class, but i was keen to prevent other non-defined 'types' being called.
# it also provides building blocks to expand the game and define special features for the differing types of pokemon.

class FireType(Pokemon):
    def __init__(self, name, level = 5):          
        super().__init__(name, level)
        self.type = 'Fire'

class ElectricType(Pokemon):
    def __init__(self, name, level = 5):          
        super().__init__(name, level)
        self.type = 'Electric'

class WaterType(Pokemon):
    def __init__(self, name, level = 5):          
        super().__init__(name, level)
        self.type = 'Water'

# Creation of pokemon cards that will be played in this game
tepig = FireType('tepig', 3)
reshiram = FireType('Reshiram', 5)
ducklett = WaterType('Ducklett', 7)
samurott = WaterType('Samurott', 5)
zekrom = ElectricType('Zekrom', 6)
thundurus = ElectricType('Thundurus', 5)    
 
# create trainer class. A Trainer can have up to 6 pokemon cards, which we stored in list, 
# the trainer also requires a name, number of potions they have and current_active_card represented as number 
class Trainer:
    def __init__(self, name, pokemons, potions):
        self.name = name
        self.pokemons = pokemons
        self.potions = potions
        self.current_card_active = 0

        if len(self.pokemons) > 6:
            print("{name} you have selcted too many cards, you are only allowed a maximum of 6".format(name = self.name))
    
    def __repr__(self):
        print("'{name}' has the following 3 pokemon: {list}".format(name = self.name, list = self.pokemons))
        return "'{name}' current active card is {active}\n".format(name = self.name, active = self.pokemons[self.current_card_active])


# create method to allow use of potion on current card in play.
# this checks that current player has enough potions before applying the rejuventate function
    def use_potion(self):
        if self.potions > 0:
            print("{name} has used a potion".format(name = self.name))
            self.pokemons[self.current_card_active].rejuvenate()
            self.potions -= 1
            print("{name} has {potions} remaining".format(name = self.name, potions = self.potions))
        else:
            print("your do not have enough potions to revive your pokemon")

# create method to allow trainer to attack other trainer  
# prior to attacking this checks whether the attacking players card is active
# it then checks whther the player being attack has a valid card and if not then it call new_card() and assigns one if available.  
    def attack_other_player(self, other_player):
        if self.pokemons[self.current_card_active].is_knocked_out:
            print("The chosen pokemon has already been knocked out")
        elif other_player.pokemons[other_player.current_card_active].is_knocked_out: 
            other_player.new_card()
        self.pokemons[self.current_card_active].attack(other_player.pokemons[other_player.current_card_active])

# create a method to allow the player to switch cards
# check that the card is in play prior to allowing the switch
    def switch(self, index):
        if self.pokemons[self.current_card_active].is_knocked_out:
            print("The chosen pokemon has already been knocked out")
        else:
            self.current_card_active = index
        print("you have changed cards to {pokemon}".format(pokemon = self.pokemons[self.current_card_active]))

 # If the player being attacked is holding a knocked out card, then this function will automatically switch to next available card.
 # if all cards are 'knocked out' the process stops.   
    def new_card(self):
        card = -1
        active = False
        while card < len(self.pokemons):
            card += 1  
            if self.pokemons[card].is_knocked_out == False:
                self.current_card_active = card
                print("your new card is {pokemon}".format(pokemon = self.pokemons[self.current_card_active]))
                active = False
                break
            else:
                active = True
                break
        if active == True:
            print("The other player has no cards left you win the game!!!")
            sys.exit()


playerA = Trainer('Martin', [tepig, samurott, thundurus, tepig, samurott, thundurus, tepig, samurott, thundurus], 2)
playerB = Trainer('2nd Player', [ducklett, tepig, zekrom], 2) 



# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   TEST SCRIPTS   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
 
# # <<<TEST SCRIPTS CHECK VARIABLES>>>
# print(tepig, samurott, ducklett, reshiram, zekrom, thundurus)
# print(playerB, playerA)

# # <<<TEST SCRIPTS ATTACK>>>
# print("<<TEST>> current active pokemon playerA.....", playerA.pokemons[playerA.current_card_active])
# print("<<TEST>> current active pokemon playerB.....", playerB.pokemons[playerB.current_card_active])
# # <<<Test 1>>>
# # Fire to Water = 50% damage = 50% of playerA level.
# # playerA = tepig level 3 should cause 1.5 damage
# playerA.attack_other_player(playerB)
# # Water to Fire = 200% damage = 200% of playerB level.
# # playerB = Ducklette level 7 should cause 14 damage
# playerB.attack_other_player(playerA)

# #<<<Test 2>>>
# playerA.switch(1)
# playerB.switch(2)
# print("<<TEST>> current active pokemon playerA.....", playerA.pokemons[playerA.current_card_active])
# print("<<TEST>> current active pokemon playerB.....", playerB.pokemons[playerB.current_card_active])
# # Water to Electric = 100% damage = 100% of playerA level.
# # playerA = Samurott level 5 should cause 5 damage
# playerA.attack_other_player(playerB)
# # Electric to Water = 200% damage = 200% of playerA level.
# # playerB = zekrom level 2 should cause 4 damage
# playerB.attack_other_player(playerA)

# # <<<Test 3>>>
# # players attacking themselves should throw error message
# playerB.attack_other_player(playerB)


# <<<TEST SCRIPTS KNOCK-OUT>>>
# playerA should knock out playerB in 2 rounds, playerB should then not be able to use the same pokemon in return attack
# playerA.switch(1)
# playerB.switch(2)
# print("<<TEST>> current active pokemon playerA.....", playerA.pokemons[playerA.current_card_active])
# print("<<TEST>> current active pokemon playerB.....", playerB.pokemons[playerB.current_card_active])
# playerA.attack_other_player(playerB)
# playerA.attack_other_player(playerB)
# playerB.attack_other_player(playerA)

# # <<<TEST SCRIPTS END GAME>>>
# # removals of all cards should end game
# playerB.switch(2)
# print("<<TEST>> current active pokemon playerA.....", playerA.pokemons[playerA.current_card_active])
# print("<<TEST>> current active pokemon playerB.....", playerB.pokemons[playerB.current_card_active])
# playerB.attack_other_player(playerA)
# playerB.attack_other_player(playerA)
# playerB.attack_other_player(playerA)
# playerB.attack_other_player(playerA)
# playerB.attack_other_player(playerA)
# playerB.attack_other_player(playerA)
# playerB.attack_other_player(playerA)
# playerB.attack_other_player(playerA)
# playerB.attack_other_player(playerA)
# playerB.attack_other_player(playerA)
# playerB.attack_other_player(playerA)
# playerB.attack_other_player(playerA)
# playerB.attack_other_player(playerA)
# playerB.attack_other_player(playerA)
# playerB.attack_other_player(playerA)
# playerB.attack_other_player(playerA)


# # <<<TEST SCRIPTS POTION>>>
# # 3 Calls should return no potions left to use
# playerA.use_potion()
# playerA.use_potion()
# playerA.use_potion()

# playerB.use_potion()
# playerB.use_potion()
# playerB.use_potion()


# # <<<TEST SCRIPTS SWITCH>>>
# playerA.switch(1)
# print("<<TEST>> list pokemons.....", playerA.pokemons)
# print("<<TEST>> index of current active card", playerA.current_card_active)
# print("<<TEST>> index of current active card", playerA.current_card_active)
# playerA.switch(2)
# print("<<TEST>> list pokemons.....", playerA.pokemons)
# print("<<TEST>> index of current active card", playerA.current_card_active)
# print("<<TEST>> index of current active card", playerA.current_card_active)
# playerA.switch(0)
# print("<<TEST>> list pokemons.....", playerA.pokemons)
# print("<<TEST>> index of current active card", playerA.current_card_active)
# print("<<TEST>> index of current active card", playerA.current_card_active)
# playerB.switch(1)
# print("<<TEST>> list pokemons.....", playerA.pokemons)
# print("<<TEST>> index of current active card", playerA.current_card_active)
# print("<<TEST>> index of current active card", playerA.current_card_active)
# playerB.switch(2)
# print("<<TEST>> list pokemons.....", playerA.pokemons)
# print("<<TEST>> index of current active card", playerA.current_card_active)
# print("<<TEST>> index of current active card", playerA.current_card_active)
# playerB.switch(0)
# print("<<TEST>> list pokemons.....", playerA.pokemons)
# print("<<TEST>> index of current active card", playerA.current_card_active)
# print("<<TEST>> index of current active card", playerA.current_card_active)

