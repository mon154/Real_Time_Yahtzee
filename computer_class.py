### Computer player Class and functions that regulate the computer's turn
from dice_reader import validate_dice
from computer_helper import check_lower_scores, found_a_box, did_not_find_a_box, get_unique_counts
class computer_player:
  def __init__(self):
    self.upper_section = {"Ones":None,"Twos":None,"Threes":None,"Fours":None,"Fives":None,"Sixes":None}
    self.lower_section = {"3 of a kind":None,"4 of a kind":None,"Full House":None,"SM Straight":None,"LG Straight":None,"Yahtzee":None,"Chance":None}
    self.yahtzee_bonus = 0
    self.player_num = 'Jarvis'
  # Runs the computers turn
  def take_turn(self):
    ###Currently this will check for one of the lower boxes and if a match is found, then it will score for the lower box
    ###Otherwise it will use both rerolls and reroll all but the most frequent, or if 5 different dice, the highest value still available in the upper section (or in general if all filled first)
    ###At the end it picks the box that gives the highest score
    turn_rerolls = 0
    want_reroll = True
    print("")
    input("Please roll the dice and press enter when ready.")
    print("Reading dice....")
    print("")
    dice_counts = validate_dice()
    bot_available = self.get_availble_lower_boxes()
    top_available = self.get_available_upper_boxes()
    all_available = top_available + bot_available
    unique_counts= get_unique_counts(dice_counts)
    found_box = check_lower_scores(dice_counts, bot_available,unique_counts)
    if found_box != "None":
      rerolls = found_a_box(self,dice_counts, turn_rerolls, found_box, top_available, unique_counts)
      if rerolls == None:
        want_reroll = False
    else:
      rerolls = did_not_find_a_box(self,dice_counts, turn_rerolls, all_available, unique_counts)
      if rerolls == None:
        want_reroll = False  
    while turn_rerolls < 2 and want_reroll:
      turn_rerolls += 1
      ### How to pick what to reroll
      print("Please reroll the ", end = ' ')
      print(", ".join(map(str, rerolls)))
      print("")
      input("Please reroll requested dice and press enter when ready.")
      dice_counts = validate_dice()
      bot_available = self.get_availble_lower_boxes()
      top_available = self.get_available_upper_boxes()
      all_available = top_available + bot_available
      unique_counts= get_unique_counts(dice_counts)
      found_box = check_lower_scores(dice_counts, bot_available, unique_counts)
      if found_box != "None":
        rerolls = found_a_box(self,dice_counts, turn_rerolls, found_box, top_available, unique_counts)
        if rerolls == None:
          want_reroll = False
      else:
        rerolls = did_not_find_a_box(self,dice_counts, turn_rerolls, all_available, unique_counts)
        if rerolls == None:
          want_reroll = False
  ### Allows us to see empty score boxes
  def get_availble_lower_boxes(self):
    bot_available = []
    for k,v in self.lower_section.items():
      if self.lower_section[k] == None:
        bot_available.append(k)
      else:
        pass
    return bot_available 
  def get_available_upper_boxes(self):
    top_available = []
    for k,v in self.upper_section.items():
      if self.upper_section[k] == None:
        top_available.append(k)
      else:
        pass
    return top_available
  