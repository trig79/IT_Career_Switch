import random
import sys

money = 100

#Checks that player has sufficent funds in account to play.
def balance_check(bet):
    if money <= 0 or (money - bet) < 0:
      print("Sorry You Are Out of Funds")
      print("Please deposit more money to continue playing")
      sys.exit()

# -----------------------Heads and Tails-------------------------------

def coin_flip(guess, bet):
  balance_check(bet)
  print ("You are playing Heads or Tails, you have choosen", guess)
  randomNumber = random.randint(1, 2)
  # headOrTails varible created to allow streamlining of 'if' statement and inclusion into a concatenated statement
  headOrTails = 'heads' if randomNumber == 1 else 'tails'
  # guessConvert removes failure risk due to user input error.  e.g Heads, HEaDS HEADS etc
  guessConvert = guess.lower()

  if guessConvert == 'heads' and randomNumber == 1 or guessConvert == 'tails' and randomNumber == 2:
    print("Its", headOrTails)
    print("Congratulations you won:",str(bet))
    return bet
  elif not guessConvert == 'heads' and not guessConvert == 'tails':  #if it DOES NOT equal odds or evens then there must be a user input error
    print("Error! you must enter either Heads or Tails to play")
    return 0 
  else:
    print("You Lose!")
    return -bet


# --------------------------Cho-Han-------------------------------

def chohan(guess, bet):
  balance_check(bet)
  print ("You are playing Cho Han, you have choosen", guess)
  dice = random.randint(1, 6) + random.randint(1, 6)
  # oddsOrEvens varible created to allow streamlining of 'if' statement and inclusion into a concatenated statement
  oddsOrEvens = 'evens' if dice % 2 == 0 else 'odds'
  # guessConvert removes failure risk due to user input error.  e.g Heads, HEaDS HEADS etc
  guessConvert = guess.lower()

  if guessConvert == 'odds' and oddsOrEvens == 'odds'or guessConvert == 'evens' and oddsOrEvens == 'evens':
    print("Its", dice, "....", oddsOrEvens)
    print("Congratulations you won:",str(bet))
    return bet
  elif not guessConvert == 'odds' and not guessConvert == 'evens':  #if it DOES NOT equal odds or evens then there must be a user input error
    print("Error! you must enter either Odds or Evens to play")
    return 0 
  else:
    print("You Lose!")
    return -bet

# --------------------------Higher Card Wins-------------------------------
# the project didnt ask for user input, so instead I have simulated the game using random on a single suit of cards, numbered 1-14.
def higher_card(bet):
  balance_check(bet)
  print ("You are playing Higher Card Wins")
  player1 = random.randint(1, 14)
  player2 = random.randint(1, 14)
  
  if player1 > player2:
    print("Player 1 drew a", str(player1),".....")
    print("Player 2 drew a", str(player2),".....")
    print("Player 1 Wins!")
    return bet
  elif player1 < player2:
    print("Player 1 drew a", str(player1),".....")
    print("Player 2 drew a", str(player2),".....")
    print("Player 2 Wins!")
    return -bet
  else: 
    print("Player 1 drew a", str(player1),".....")
    print("Player 2 drew a", str(player2),".....")
    print("Result is a Draw!")
    return 0

#ADD BET ODDS TO CALCULATIONS
# --------------------------Roulette-------------------------------
# For this exercise I have taken the European Wheel which contains numbers 0-36
# Bets that i have captured below are:
#       Odds or Evens, Black or Red;     Payout 1 to 1
#       Any single number.               Payout 35 to 1

def roulette(betPlaced, bet):
  balance_check(bet)
  rouletteNumber = random.randint(0, 36)
  #Defines roulette color/number combinations and returns color value to color variable
  blackNumbers = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
  redNumbers = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
  color = 'black' if rouletteNumber in blackNumbers else 'red' if rouletteNumber in redNumbers else 'green'
  #Defines whether off or even has been rolled
  oddEven = 'evens' if rouletteNumber % 2 == 0 else 'odds'
  betPlaced = betPlaced

  # function for placing an odd even bet
  def odd_even(guess, bet):
    print ("You are playing Roulette, you have choosen", guess)
    if betPlaced == 'odds' and oddEven == 'odds' or betPlaced == 'evens' and oddEven == 'evens':
      print("Its", oddEven)
      print("Congratulations you won:",str(bet))
      return bet
    else:
      print("Its", oddEven)
      print("You Lose!")
      return -bet

  # function for placing an color bet
  def color_bet(guess, bet):
    print ("You are playing Roulette, you have choosen", guess)
    if betPlaced == 'black' and color == 'black' or betPlaced == 'red' and color == 'red' or betPlaced == 'green' and color == 'green':
      print("Its", color)
      print("Congratulations you won:",str(bet))
      return bet
    else:
      print("Its", color)
      print("You Lose!")
      return -bet

  # function for placing an single number bet
  def single_number(guess, bet):
    print ("You are playing Roulette, you have choosen", guess)
    if betPlaced == rouletteNumber:
      print("Its", rouletteNumber)
      print("Congratulations you won:",str(bet))
      return (bet * 35)
    else:
      print("Its", rouletteNumber)
      print("You Lose!")
      return -bet

  # Checks for correct input of string or int. 
  # Implements lower case to string input.
  # Calls relevant function for the bet type placed.
  if type(betPlaced) == str:
    betPlaced = betPlaced.lower()
    if betPlaced =='odds' or betPlaced == 'evens':
      odd_even(betPlaced, bet)
    elif betPlaced == 'black' or betPlaced == 'red' or betPlaced == 'green':
      color_bet(betPlaced, bet)
    else:
      print("Input Error, please resubmit using Odds or Evens, Black or Red or a whole number 0 - 36 inclusive")
    return 0
  elif type(betPlaced) == int and betPlaced >= 0 and betPlaced < 37:
    betPlaced = betPlaced
    single_number(betPlaced, bet)
    return 0
  else:
    print("Input Error, please resubmit using Odds or Evens, Black or Red or a whole number 0 - 36 inclusive")
    return 0


#----------Call your game of chance functions here---------------

money += coin_flip("heads", 10)     # enter heads or tails and the amount you wish to bet
money += chohan("Evens", 10)        # enter odds or evens and the amount you wish to bet
money += higher_card(10)            # choose a card 1 - 14 inclusive
money += roulette(10, 10)           # enter odds or evens / red or black / or single int between 0-36 inclusive and the amount you wish to bet
money += roulette('black', 10)      # enter odds or evens / red or black / or single int between 0-36 inclusive and the amount you wish to bet
money += roulette('odds', 10)       # enter odds or evens / red or black / or single int between 0-36 inclusive and the amount you wish to bet

print("Your remaining balance is",str(money))
