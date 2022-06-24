### Computer player Class and functions that regulate the computer's turn
from dice_reader import read_dice, validate_dice

class computer_player:
  def __init__(self):
    self.upper_section = {"Ones":None,"Twos":None,"Threes":None,"Fours":None,"Fives":None,"Sixes":None}
    self.lower_section = {"3 of a kind":None,"4 of a kind":None,"Full House":None,"SM Straight":None,"LG Straight":None,"Yahtzee":None,"Chance":None}
    self.upper_bonus = False
    self.yahtzee_bonus = []
  # Runs the computers turn
  def take_turn(self):
    pass