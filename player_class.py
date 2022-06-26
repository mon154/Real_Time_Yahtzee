### Player Class and functions that regulate individual player turns
from matplotlib.style import available
from dice_reader import validate_dice
from score_helper import score_aces, score_twos, score_threes, score_fours, score_fives, score_sixes
from score_helper import score_three_kind, score_four_kind, score_full_house, score_smstraight, score_lgstraight, score_yahtzee, score_chance
# Controls the player turn
class player:
  def __init__(self, player_num):
    self.player_num = player_num
    self.upper_section = {"Aces":None,"Twos":None,"Threes":None,"Fours":None,"Fives":None,"Sixes":None}
    self.lower_section = {"3 of a kind":None,"4 of a kind":None,"Full House":None,"SM Straight":None,"LG Straight":None,"Yahtzee":None,"Chance":None}
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
    available = []
    print("These are your empty score boxes:")
    for k,v in self.upper_section.items():
      if self.upper_section[k] == None:
        print(k, end=" | ")
        available.append(k)
      else:
        pass
    for k,v in self.lower_section.items():
      if self.lower_section[k] == None:
        print(k, end=" | ")
        available.append(k)
      else:
        pass
    print("")
    print("This is what you rolled: ", end = ' ')
    print(", ".join(map(str, dice_counts)))
    print("")
    box_choice = input("Which box would you like to fill: ")
    print(box_choice)
    if (box_choice in available):
      if box_choice == "Aces":
        score_aces(self, dice_counts)
      elif box_choice == "Twos":
        score_twos(self, dice_counts)
      elif box_choice == "Threes":
        score_threes(self, dice_counts)
      elif box_choice == "Fours":
        score_fours(self, dice_counts)
      elif box_choice == "Fives":
        score_fives(self, dice_counts)
      elif box_choice == "Sixes":
        score_sixes(self, dice_counts)
      elif box_choice == "3 of a kind":
        score_three_kind(self, dice_counts)
      elif box_choice == "4 of a kind":
        score_four_kind(self, dice_counts)
      elif box_choice == "Full House":
        score_full_house(self, dice_counts)
      elif box_choice == "SM Straight":
        score_smstraight(self, dice_counts)
      elif box_choice == "LG Straight":
        score_lgstraight(self, dice_counts)
      elif box_choice == "Yahtzee":
        score_yahtzee(self, dice_counts)
      elif box_choice == "Chance":
        score_chance(self, dice_counts)