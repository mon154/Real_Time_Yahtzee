### File that contains the functions that run the game in the terminal

from rules import print_rules
from player_class import player
from computer_class import computer_player

# Displays selected users scorecard
def display_scorecard(current_player):
  aces = current_player.upper_section["Ones"]
  twos = current_player.upper_section["Twos"]
  threes = current_player.upper_section["Threes"]
  fours = current_player.upper_section["Fours"]
  fives = current_player.upper_section["Fives"]
  sixes = current_player.upper_section["Sixes"]
  three_of_a_kind = current_player.lower_section["3 of a kind"]
  four_of_a_kind = current_player.lower_section["4 of a kind"]
  full_house = current_player.lower_section["Full House"]
  sm_straight = current_player.lower_section["SM Straight"]
  lg_straight = current_player.lower_section["LG Straight"]
  yahtzee = current_player.lower_section["Yahtzee"]
  chance = current_player.lower_section["Chance"]
  bonus = current_player.yahtzee_bonus
  print("-----------------------------------------")
  print(f"| Player {current_player.player_num}    ")
  print("-----------------------------------------")
  print("| Upper Section                          ")
  print("-----------------------------------------")
  print(f"| Aces: {aces}                          ")
  print(f"| Twos: {twos}                          ")
  print(f"| Threes: {threes}                      ")
  print(f"| Fours: {fours}                        ")
  print(f"| Fives: {fives}                        ")
  print(f"| Sixes: {sixes}                        ")
  print("-----------------------------------------")
  print("| Lower Section                          ")
  print("-----------------------------------------")
  print(f"| 3 of a kind: {three_of_a_kind}        ")
  print(f"| 4 of a kind: {four_of_a_kind}         ")
  print(f"| Full House: {full_house}              ")
  print(f"| SM Straight: {sm_straight}            ")
  print(f"| LG Straight: {lg_straight}            ")
  print(f"| Yahtzee: {yahtzee}                    ")
  print(f"| Chance: {chance}                      ")
  print(f"| Yahtzee Bonus: {bonus}")
  print("-----------------------------------------")
# Calculates final score of given player
def calculate_score(current_player):
  upper_score = sum(current_player.upper_section.values())
  if upper_score >= 63:
    upper_score_bonus = 35
  else:
    upper_score_bonus = 0
  lower_score = sum(current_player.lower_section.values()) + (current_player.yahtzee_bonus)
  total_score = upper_score  + upper_score_bonus + lower_score
  return total_score

# Calculates final score, and determines/displays the winner
def final_scores(players, computer_player):
    final_scores = {}
    for i in players:
        player_score = calculate_score(i)
        final_scores[i] = player_score
        print(f"Player {i.player_num}: {player_score}")
    computer_score = calculate_score(computer_player)
    final_scores[computer_player] = computer_score
    print(f"Player {max(final_scores)} is the winner!") 

# Runs the game    
def run_game():
  comp = computer_player()
  players = []
  valid_input = False
  while not valid_input:
    try:
       player_count = int(input("How many players are playing? "))
       valid_input = True
    except ValueError:
      print("Not a valid integer, please try again.")
  for i in range (1,player_count+1): 
    players.append(player(i))
  for i in range(1,14):
    for x in players: 
      print("")
      print(f"Player {x.player_num}, Turn {i}:")
      x.take_turn()
      valid_display_input = False
      while not valid_display_input:
        display_card = input("Would you like to see your scorecard? ")
        if display_card in ["Yes", "yes", "y", "Y"]:
          valid_display_input = True
          display_scorecard(x)
        elif display_card in ["No", "no", "n", "N"]:
          valid_display_input = True
        else: 
          print("Please enter Yes or No")
    print(f"JARVIS, Turn {i}:")
    comp.take_turn()
    display_scorecard(comp)
  final_scores(players, comp)

# Prints main menu that allows user to start, exit, or leave the game
def main_menu():
  while True:
    print('\n1. Start Game')
    print('2. View Rules')
    print('3. Exit Game')
    main_menu_input = input("Please Select an Option: ")
    if main_menu_input == "1":
      run_game()
      break
    elif main_menu_input == "2":
      print_rules()
    elif main_menu_input == "3":
      break
    else:
      print("There was an issue with your input, please enter a number between 1 and 2")

# Runs the program
def main():
  print("Welcome to Yahtzee!")
  main_menu()
  print("Thank you for playing!")

if __name__ == "__main__":
    main()
