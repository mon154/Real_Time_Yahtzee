### Functions related to displaying game rules

def game_basics():
  print("\nYahtzee is a 13 round game where players try to create dice combinations to get the highscore.")
  print("Each round, players will roll 5 dice and can either mark their scorecard or reroll up to two times.")
  print("During either reroll, players can reroll any of their dice they wish to try and create a dice combo")
  print("After the final reroll, the player must choose which score box to fill.")
  print("If a player's roll doesn't match any of the boxes, they must fill in a box of their choice with a zero.")
  print("")
def score_categories():
  print("\nThere are two score box sections:")
  print("The Upper Section:")
  print("The Upper Section scores the total of the same dice from 1 to 6 in your roll. For example, if a player rolled four threes, they would mark 12 in the threes box")
  print("If needed, you can just count a single die as it's better than a zero")
  print("Pro-Tip: If you get over 63 points in this section, you get a bonus 35 points!")
  print("\nThe Lower Section:")
  print("The Lower Section scores the various dice combos. They are as follows:")
  print("3 of a Kind: 3 of the same dice. The score is the total of the face values of all five dice.")
  print("4 of a Kind: 4 of the same dice. The score is the total of the face values of all five dice.")
  print("Full House: Any 3 of a Kind and any Pair. 25 points")
  print("Small Straight: 4 consecutive dice (ex. 1,2,3,4). 30 points")
  print("Large Straight: 5 consecutive dice. 40 points")
  print("Chance: No combo, it's a safety net if you don't have anything else. The score is the total of the face values of all five dice.")
  print("Yahtzee: 5 of a Kind. 50 points")
  print("")
def yahtzee_bonus():
  print("\nIf a player gets lucky and happens to roll Yahtzee multiple times in a game they will be able to get extra points.")
  print("When a bonus yahtzee is rolled, a player will get an extra 100 points by marking off the Yahtzee bonus box and will also fill in an additional box on the scorecard.\n")
  print("The additional box to be filled is determined by the following methods:")
  print("Score the total of the dice in the appropriate upper section box.")
  print("If that box is full, fill in either the 3 of a Kind or 4 of a Kind boxes with the dice total.")
  print("If those are also full, use you dice total in chance or one of the other dice combos in the lower section (score those as normal).")
  print("However, if you have already scored a zero in the Yahtzee box, you cannot get the yahtzee bonus however you still get to fill in the additional box as described above.")
  print("")
def tips_and_tricks():
  print("\nKeep in mind that some dice combos are harder to roll than others. It can be helpful to try to roll for some of the harder ones first.")
  print("Try to make sure you get 63 points in the upper section to get the 35 bonus points.")
  print("Try to save the chance roll until later in the game when score options are more limited")
  print("")
def print_rules():
  info = ("Yahtzee Game Guide:\n1. Game Basics\n2. Dice Combination Info\n3. Yahtzee Bonus Information\n4. Tips and Tricks\n5. Return to Main Menu")
  print("")
  print(info)
  while True:
    rule_category_input = input("Please Select an Option: ")
    if (rule_category_input) == "1":
      game_basics()
      print(info)
    elif rule_category_input == "2":
      score_categories()
      print(info)
    elif rule_category_input == "3":
      yahtzee_bonus()
      print(info)
    elif rule_category_input == "4":
      tips_and_tricks()
      print(info)
    elif rule_category_input == "5":
      break
    else: 
      print("There was an issue with your input, please enter a number between 1 and 4")