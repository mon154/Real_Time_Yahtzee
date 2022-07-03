def check__lower_scores(dice_scores, available):
    dice_scores = dice_scores.sort()
    ### Check for yahtzee
    for box in available.reverse():
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
                if dice_scores[0] != dice_scores[3] or dice_scores[1] != dice_scores[4]:
                    return "Full House"
            else:
                pass 
        elif box == "4 of a kind": 
            aces = 0
            ones = 0
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
            ones = 0
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
                        
    