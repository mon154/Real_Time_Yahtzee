### Player Class and functions that regulate individual player turns

from matplotlib.style import available
from dice_reader import validate_dice
from score_helper import score_aces, score_twos, score_threes, score_fours, score_fives, score_sixes
from score_helper import score_three_kind, score_four_kind, score_full_house, score_smstraight, score_lgstraight, score_yahtzee, score_chance
from computer_helper import get_unique_counts
# Controls the player turn
class player:
  def __init__(self, player_num):
    self.player_num = player_num
    self.upper_section = {"Ones":None,"Twos":None,"Threes":None,"Fours":None,"Fives":None,"Sixes":None}
    self.lower_section = {"3 of a kind":None,"4 of a kind":None,"Full House":None,"SM Straight":None,"LG Straight":None,"Yahtzee":None,"Chance":None}
    self.yahtzee_bonus = 0

  # Runs the player turn
  def take_turn(self):
    turn_rerolls = 0
    want_reroll = True
    input("Please roll the dice and press enter when ready.")
    print("Reading dice....")
    print("")
    dice_counts = validate_dice()
    print("These are the dice you rolled: ", end = ' ')
    print(", ".join(map(str, dice_counts)))
    print("")
    while turn_rerolls < 2 and want_reroll:
      turn_rerolls += 1
      valid_reroll_input = False
      while not valid_reroll_input:
        reroll = input("Would you like to reroll: ")
        if reroll in ["Yes", "yes", "y", "Y"]:
          valid_reroll_input = True
          input("Please reroll desired dice and press enter when ready.")
          dice_counts = validate_dice()
          print("These are the dice you rolled: ", end = ' ')
          print(", ".join(map(str, dice_counts)))
          print("")
        elif reroll in ["No", "no", "n", "N"]:
          valid_reroll_input = True
          print("")
          want_reroll = False
        else: 
          print("Please enter Yes or No")
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
    bonus_yahtzee = False
    if len(set(dice_counts)) == 1 and self.lower_section["Yahtzee"] == 50:
      print("You have scored a bonus Yahtzee!")
      print("You get 100 bonus points and get to fill an additional box.")
      bonus_yahtzee = True
      self.yahtzee_bonus += 100
    valid_box_choice = False
    while not valid_box_choice:
      box_choice = input("Which box would you like to fill: ")
      if box_choice in available:
        valid_box_choice = True
      else:
        print("Please enter one of the availble boxes. These are case sensitive.")
    if box_choice == "Ones":
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
      unique_counts = get_unique_counts(dice_counts)
      score_full_house(self, dice_counts,unique_counts, bonus_yahtzee)
    elif box_choice == "SM Straight":
      score_smstraight(self, dice_counts, bonus_yahtzee)
    elif box_choice == "LG Straight":
      score_lgstraight(self, dice_counts, bonus_yahtzee)
    elif box_choice == "Yahtzee":
      score_yahtzee(self, dice_counts)
    elif box_choice == "Chance":
      score_chance(self, dice_counts)