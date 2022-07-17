from score_helper import score_aces, score_twos, score_threes, score_fours, score_fives, score_sixes
from score_helper import score_three_kind, score_four_kind, score_full_house, score_smstraight, score_lgstraight, score_yahtzee, score_chance

def check_lower_scores(dice_scores, available, unique_counts):
    available.reverse()
    if 'Chance' in available:
        available.remove("Chance")
    ### Check for yahtzee
    for box in available:
        if box == "Yahtzee":
            if len(set(dice_scores)) == 1:
                return "Yahtzee"
            else:
                pass
        elif box == "LG Straight":
            if (len(set(dice_scores))) == 5:
                if dice_scores[0] == 1 and dice_scores[3] == 5:
                    return "LG Straight"
                elif dice_scores[0] == 2 and dice_scores[4] == 6:
                    return "LG Straight"
                elif dice_scores[0] == 1 and dice_scores[4] == 5:
                    return "LG Straight"
            else:
                pass
        elif box == "SM Straight":
            if (len(set(dice_scores))) >= 4:
                if dice_scores[0] == 1 and dice_scores[3] == 4 and dice_scores[1] != dice_scores[2]:
                    return "SM Straight"   
                elif dice_scores[0] == 2 and dice_scores[3] == 5 and dice_scores[1] != dice_scores[2]:
                    return "SM Straight"
                elif dice_scores[0] == 2 and dice_scores[4] == 5 and dice_scores [2] == dice_scores[3]  :
                    return "SM Straight"
                elif dice_scores[0] == 2 and dice_scores[4] == 5 and dice_scores [1] == dice_scores[2]  :
                    return "SM Straight"
                elif dice_scores[0] == 3 and dice_scores[3] == 6:
                    return "SM Straight"
            else:
                pass
        elif box == "Full House":
            if (len(set(dice_scores))) == 2:
                if dice_scores[0] != dice_scores[3] and max(unique_counts.values()) != 4:
                    return "Full House"
            else:
                pass 
        elif box == "4 of a kind": 
            aces = 0
            twos = 0
            threes = 0
            fours = 0
            fives = 0
            sixes = 0
            for i in dice_scores:
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
                return "4 of a kind"
            else:
                pass
        elif box == "3 of a kind":
            aces = 0
            twos = 0
            threes = 0
            fours = 0
            fives = 0
            sixes = 0
            for i in dice_scores:
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
                return "3 of a kind"
            else:
                pass
    return "None"

### Computer logic if our roll fits one of the lower section boxes other than chance
def found_a_box(comp_player, dice_counts, turn_rerolls, found_box, top_available, unique_counts):
    key_list = list(unique_counts.keys())
    val_list = list(unique_counts.values())

    if turn_rerolls != 2:
        another_reroll_availble = True
    else:
        another_reroll_availble = False

    if found_box == "Yahtzee": 
        score_yahtzee(comp_player, dice_counts)
        return None
    elif found_box == "LG Straight":
        score_lgstraight(comp_player, dice_counts, False)
        return None
    elif found_box == "SM Straight":
        score_smstraight(comp_player, dice_counts, False)
        return None
    elif found_box == "Full House":
        Three_val = val_list.index(3)
        Three_category = key_list[Three_val]
        Two_val = val_list.index(2)
        Two_category = key_list[Two_val] 

        if Three_category in top_available:
            if another_reroll_availble:
                rerolls = []
                if Three_category == "Ones":
                    for i in dice_counts:
                        if i != 1:
                            rerolls.append(i)
                elif Three_category == "Twos":
                    for i in dice_counts:
                        if i != 2:
                            rerolls.append(i)
                elif Three_category == "Threes":
                    for i in dice_counts:
                        if i != 3:
                            rerolls.append(i)
                elif Three_category == "Fours":
                    for i in dice_counts:
                        if i != 4:
                            rerolls.append(i)
                elif Three_category == "Fives":
                    for i in dice_counts:
                        if i != 5:
                            rerolls.append(i)
                elif Three_category == "Sixes":
                    for i in dice_counts:
                        if i != 6:
                            rerolls.append(i)
                return rerolls
            else:
                if Three_category == "Ones":
                    score_aces(comp_player, dice_counts)
                elif Three_category == "Twos":
                    score_twos(comp_player, dice_counts)
                elif Three_category == "Threes":
                    score_threes(comp_player, dice_counts)
                elif Three_category == "Fours":
                    score_fours(comp_player, dice_counts)
                elif Three_category == "Fives":
                    score_fives(comp_player, dice_counts)
                elif Three_category == "Sixes":
                    score_sixes(comp_player, dice_counts)
                return None
        else:
            if Two_category in top_available:
                if another_reroll_availble:
                    rerolls = []
                    if Two_category == "Ones":
                        for i in dice_counts:
                            if i != 1:
                                rerolls.append(i)
                    elif Two_category == "Twos":
                        for i in dice_counts:
                            if i != 2:
                                rerolls.append(i)
                    elif Two_category == "Threes":
                        for i in dice_counts:
                            if i != 3:
                                rerolls.append(i)
                    elif Two_category == "Fours":
                        for i in dice_counts:
                            if i != 4:
                                rerolls.append(i)
                    elif Two_category == "Fives":
                        for i in dice_counts:
                            if i != 5:
                                rerolls.append(i)
                    elif Two_category == "Sixes":
                        for i in dice_counts:
                            if i != 6:
                                rerolls.append(i)
                    return rerolls
                else:
                    score_full_house(comp_player, dice_counts, False)
                    return None
            else:
                score_full_house(comp_player, dice_counts, False)
                return None 
        
    elif found_box == "4 of a kind":
        Four_val = val_list.index(4)
        Four_category = key_list[Four_val]

        if Four_category in top_available:
            if another_reroll_availble:
                rerolls = []
                if Four_category == "Ones":
                    for i in dice_counts:
                        if i != 1:
                            rerolls.append(i)
                elif Four_category == "Twos":
                    for i in dice_counts:
                        if i != 2:
                            rerolls.append(i)
                elif Four_category == "Threes":
                    for i in dice_counts:
                        if i != 3:
                            rerolls.append(i)
                elif Four_category == "Fours":
                    for i in dice_counts:
                        if i != 4:
                            rerolls.append(i)
                elif Four_category == "Fives":
                    for i in dice_counts:
                        if i != 5:
                            rerolls.append(i)
                elif Four_category == "Sixes":
                    for i in dice_counts:
                        if i != 6:
                            rerolls.append(i)
                return rerolls
            else:
                if Four_category == "Ones":
                    score_aces(comp_player, dice_counts)
                elif Four_category == "Twos":
                    score_twos(comp_player, dice_counts)
                elif Four_category == "Threes":
                    score_threes(comp_player, dice_counts)
                elif Four_category == "Fours":
                    score_fours(comp_player, dice_counts)
                elif Four_category == "Fives":
                    score_fives(comp_player, dice_counts)
                elif Four_category == "Sixes":
                    score_sixes(comp_player, dice_counts)
                return None
        else:
           score_four_kind(comp_player, dice_counts)
           return None 

    elif found_box == "3 of a kind":
        Three_val = val_list.index(3)
        Three_category = key_list[Three_val]

        if Three_category in top_available:
            if another_reroll_availble:
                rerolls = []
                if Three_category == "Ones":
                    for i in dice_counts:
                        if i != 1:
                            rerolls.append(i)
                elif Three_category == "Twos":
                    for i in dice_counts:
                        if i != 2:
                            rerolls.append(i)
                elif Three_category == "Threes":
                    for i in dice_counts:
                        if i != 3:
                            rerolls.append(i)
                elif Three_category == "Fours":
                    for i in dice_counts:
                        if i != 4:
                            rerolls.append(i)
                elif Three_category == "Fives":
                    for i in dice_counts:
                        if i != 5:
                            rerolls.append(i)
                elif Three_category == "Sixes":
                    for i in dice_counts:
                        if i != 6:
                            rerolls.append(i)
                return rerolls
            else:
                if Three_category == "Ones":
                    score_aces(comp_player, dice_counts)
                elif Three_category == "Twos":
                    score_twos(comp_player, dice_counts)
                elif Three_category == "Threes":
                    score_threes(comp_player, dice_counts)
                elif Three_category == "Fours":
                    score_fours(comp_player, dice_counts)
                elif Three_category == "Fives":
                    score_fives(comp_player, dice_counts)
                elif Three_category == "Sixes":
                    score_sixes(comp_player, dice_counts)
                return None
        else:
           score_three_kind(comp_player, dice_counts)
           return None                      
### Computer logic if our roll does not fit one of the lower section boxes
def did_not_find_a_box(comp_player, dice_counts, turn_rerolls, all_available, unique_counts):
    rerolls = None
    if turn_rerolls != 2:
        another_reroll_availble = True
    else:
        another_reroll_availble = False

    sorted_tuples = sorted(unique_counts.items(), key=lambda item: item[1])
    sorted_unique_counts = {k: v for k, v in sorted_tuples}
    reversed_sorted_counts = dict(reversed(list(sorted_unique_counts.items())))
    for key, value in reversed_sorted_counts.items():
        if key in all_available:
            if another_reroll_availble:
                rerolls = []
                if key == "Ones":
                    for i in dice_counts:
                        if i != 1:
                            rerolls.append(i)
                elif key == "Twos":
                    for i in dice_counts:
                        if i != 2:
                            rerolls.append(i)
                elif key == "Threes":
                    for i in dice_counts:
                        if i != 3:
                            rerolls.append(i)
                elif key == "Fours":
                    for i in dice_counts:
                        if i != 4:
                            rerolls.append(i)
                elif key == "Fives":
                    for i in dice_counts:
                        if i != 5:
                            rerolls.append(i)
                elif key == "Sixes":
                    for i in dice_counts:
                        if i != 6:
                            rerolls.append(i)
                break
            else:
                if key == "Ones":
                    score_aces(comp_player, dice_counts)
                elif key == "Twos":
                    score_twos(comp_player, dice_counts)
                elif key == "Threes":
                    score_threes(comp_player, dice_counts)
                elif key == "Fours":
                    score_fours(comp_player, dice_counts)
                elif key == "Fives":
                    score_fives(comp_player, dice_counts)
                elif key == "Sixes":
                    score_sixes(comp_player, dice_counts)  
                break  
        else: ### if all the top boxes are full and don't have bottom box to fill
            if another_reroll_availble: ###Try for yahtzee
                highest_count = max(unique_counts)
                rerolls = []
                if highest_count == "Ones":
                    for i in dice_counts:
                        if i != 1:
                            rerolls.append(i)
                elif highest_count == "Twos":
                    for i in dice_counts:
                        if i != 2:
                            rerolls.append(i)
                elif highest_count == "Threes":
                    for i in dice_counts:
                        if i != 3:
                            rerolls.append(i)
                elif highest_count == "Fours":
                    for i in dice_counts:
                        if i != 4:
                            rerolls.append(i)
                elif highest_count == "Fives":
                    for i in dice_counts:
                        if i != 5:
                            rerolls.append(i)
                elif highest_count == "Sixes":
                    for i in dice_counts:
                        if i != 6:
                            rerolls.append(i)
                break
            else:
                if 'Chance'in all_available:
                    score_chance(comp_player, dice_counts)
                elif '4 of a kind' in all_available:
                    score_four_kind(comp_player, dice_counts)
                elif 'LG Straight' in all_available:
                    score_lgstraight(comp_player, dice_counts, False)
                elif 'Full House' in all_available:
                    score_full_house(comp_player, dice_counts, False)
                elif 'SM Straight' in all_available:
                    score_smstraight(comp_player, dice_counts, False)
                elif '3 of a kind' in all_available:
                    score_three_kind(comp_player, dice_counts)
                else:
                    score_yahtzee(comp_player, dice_counts)
    return rerolls            

def get_unique_counts(dice_counts):
    unique_counts= {'Ones': 0, 'Twos':0, 'Threes':0, 'Fours':0, 'Fives':0, 'Sixes':0}
    for i in dice_counts:
        if i == 1:
            unique_counts['Ones'] += 1
        elif i == 2:
            unique_counts['Twos'] += 1
        elif i == 3:
            unique_counts['Threes'] += 1
        elif i == 4:
            unique_counts['Fours'] += 1
        elif i == 5:
            unique_counts['Fives'] += 1
        else:
            unique_counts['Sixes'] += 1
    return unique_counts




            
        