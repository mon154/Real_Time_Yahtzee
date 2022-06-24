### Player Class and functions that regulate individual player turns
from dice_reader import read_dice, validate_dice

# Controls the player turn
class player:
  def __init__(self, player_num):
    self.player_num = player_num
    self.upper_section = {"Aces":None,"Twos":None,"Threes":None,"Fours":None,"Fives":None,"Sixes":None}
    self.lower_section = {"3 of a kind":None,"4 of a kind":None,"Full House":None,"SM Straight":None,"LG Straight":None,"Yahtzee":None,"Chance":None}
    self.upper_bonus = False
    self.yahtzee_bonus = []

  # Runs the player turn
  def take_turn(self):
    turn_rerolls = 0
    want_reroll = True
    input("Please roll the dice and press enter when ready.")
    dice_counts = validate_dice()
    while turn_rerolls < 2 and want_reroll:
      turn_rerolls += 1
      reroll = input("Would you like to reroll: ")
      if reroll in ["Yes", "yes", "y", "Y"]:
        input("Please reroll desired dice and press enter when ready.")
        dice_counts = validate_dice()
        print(dice_counts)
      elif reroll in ["No", "no", "n", "N"]:
        print("")
        want_reroll = False
    self.select_scorebox(dice_counts)
    
  # Shows player available score options, has them select a scorebox, and adds the score to the box
  def select_scorebox(self, dice_counts):
    print("These are your empty score boxes:")
    for k,v in self.upper_section.items():
      if self.upper_section[k] == None:
        print(k, end=" | ")
      else:
        pass
    for k,v in self.lower_section.items():
      if self.lower_section[k] == None:
        print(k, end=" | ")
      else:
        pass
    print("")
    print("This is what you rolled:")