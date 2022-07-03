def score_aces(cur_player, dice_rolls):
    ace_total = 0
    for i in dice_rolls:
        if i == 1:
            ace_total += 1
        else:
            pass
    cur_player.upper_section["Aces"] = ace_total

def score_twos(cur_player, dice_rolls):
    two_total = 0
    for i in dice_rolls:
        if i == 2:
            two_total += 1
        else:
            pass
    score = two_total * 2
    cur_player.upper_section["Twos"] = score

def score_threes(cur_player, dice_rolls):
    three_total = 0
    for i in dice_rolls:
        if i == 3:
            three_total += 1
        else:
            pass
    score = three_total * 3
    cur_player.upper_section["Threes"] = score

def score_fours(cur_player, dice_rolls):
    four_total = 0
    for i in dice_rolls:
        if i == 4:
            four_total += 1
        else:
            pass
    score = four_total * 4
    cur_player.upper_section["Fours"] = score

def score_fives(cur_player, dice_rolls):
    five_total = 0
    for i in dice_rolls:
        if i == 5:
            five_total += 1
        else:
            pass
    score = five_total * 5
    cur_player.upper_section["Fives"] = score

def score_sixes(cur_player, dice_rolls):
    six_total = 0
    for i in dice_rolls:
        if i == 6:
            six_total += 1
        else:
            pass
    score = six_total * 6
    cur_player.upper_section["Sixes"] = score

def score_three_kind(cur_player, dice_rolls):
    aces = 0
    ones = 0
    twos = 0
    threes = 0
    fours = 0
    fives = 0
    sixes = 0
    for i in dice_rolls:
        if i == 1:
            aces += 1
        elif i == 2:
            twos += 1
        elif i == 3:
            threes += 1
        elif i == 4:
            fours += 1
        elif i == 5:
            fives += 1
        else:
            sixes +=1
    if aces >= 3 or twos >= 3 or threes >= 3 or fours >= 3 or fives >= 3 or sixes >= 3: 
        score = sum(dice_rolls)
        cur_player.lower_section["3 of a kind"] = score  
    else:
        cur_player.lower_section["3 of a kind"] = 0
def score_four_kind(cur_player, dice_rolls):
    aces = 0
    ones = 0
    twos = 0
    threes = 0
    fours = 0
    fives = 0
    sixes = 0
    for i in dice_rolls:
        if i == 1:
            aces += 1
        elif i == 2:
            twos += 1
        elif i == 3:
            threes += 1
        elif i == 4:
            fours += 1
        elif i == 5:
            fives += 1
        else:
            sixes +=1
    if aces >= 4 or twos >= 4 or threes >= 4 or fours >= 4 or fives >= 4 or sixes >= 4: 
        score = sum(dice_rolls)
        cur_player.lower_section["4 of a kind"] = score  
    else:
        cur_player.lower_section["4 of a kind"] = 0

def score_full_house(cur_player, dice_rolls, bonus_yahtzee):
    dice_rolls.sort()
    if (len(set(dice_rolls))) != 2:
        cur_player.lower_section["Full House"] = 0
    elif dice_rolls[0] != dice_rolls[3] or dice_rolls[1] != dice_rolls[4]:
        cur_player.lower_section["Full House"] = 25
    elif bonus_yahtzee == True:
        cur_player.lower_section["Full House"] = 25
    else:
        cur_player.lower_section["Full House"] = 0
def score_smstraight(cur_player, dice_rolls, bonus_yahtzee):
    dice_rolls.sort()
    if (len(set(dice_rolls))) >= 4:
        if dice_rolls[0] == 1 and dice_rolls[3] == 4 and dice_rolls[1] != dice_rolls[2]:
            cur_player.lower_section["SM Straight"] = 30   
        elif dice_rolls[0] == 2 and dice_rolls[3] == 5 and dice_rolls[1] != dice_rolls[2]:
            cur_player.lower_section["SM Straight"] = 30
        elif dice_rolls[0] == 2 and dice_rolls[4] == 5 and dice_rolls [2] == dice_rolls[3]  :
            cur_player.lower_section["SM Straight"] = 30
        elif dice_rolls[0] == 2 and dice_rolls[4] == 5 and dice_rolls [1] == dice_rolls[2]  :
            cur_player.lower_section["SM Straight"] = 30
        elif dice_rolls[0] == 3 and dice_rolls[3] == 6:
            cur_player.lower_section["SM Straight"] = 30
        elif bonus_yahtzee == True:
            cur_player.lower_section["SM Straight"] = 30
        else: 
            cur_player.lower_section["SM Straight"] = 0
    else:
        cur_player.lower_section["SM Straight"] = 0  
def score_lgstraight(cur_player, dice_rolls, bonus_yahtzee):
    dice_rolls.sort()
    if (len(set(dice_rolls))) == 5:
        if dice_rolls[0] == 1 and dice_rolls[3] == 5:
            cur_player.lower_section["LG Straight"] = 0
        elif dice_rolls[0] == 2 and dice_rolls[4] == 6:
            cur_player.lower_section["LG Straight"] = 40
        elif dice_rolls[0] == 1 and dice_rolls[4] == 5:
            cur_player.lower_section["LG Straight"] = 40
        elif bonus_yahtzee == True:
            cur_player.lower_section["LG Straight"] = 40
        else:
           cur_player.lower_section["LG Straight"] = 0 
    else:
        cur_player.lower_section["LG Straight"] = 0       

def score_yahtzee(cur_player, dice_rolls):
    if len(set(dice_rolls)) == 1:
        cur_player.lower_section["Yahtzee"] = 50
    else:
        cur_player.lower_section["Yahtzee"] = 0

def score_chance(cur_player, dice_rolls):
    cur_player.lower_section["Chance"] = sum(dice_rolls)


