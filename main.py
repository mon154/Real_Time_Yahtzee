### File that contains the functions that run the game in the terminal

from rules import print_rules
from player_class import player
from computer_class import computer_player

# Displays selected users scorecard
def display_scorecard(current_player):
  pass
# Calculates final score of given player
def calculate_score(current_player):
  pass

# Calculates final score, and determines/displays the winner
def final_scores(players, computer):
    for i in players:
        calculate_score(i)
    calculate_score(computer)

# Runs the game    
def run_game():
  computer = computer_player()
  players = []
  player_count = int(input("How many players are playing? "))
  for i in range (1,player_count+1): 
    players.append(player(i))
  for i in range(1):
    for i in players: 
      i.take_turn()
    computer.take_turn()
  final_scores(players, computer)

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
