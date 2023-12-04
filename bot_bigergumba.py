def choice(round_score, my_score, opponent_score):
    if ((round_score + my_score) >= 100):
        return False
    else:
        if (my_score >= 71) or (opponent_score >= 71):
            return True
        else:
            if (round_score < (21 + (abs(my_score - opponent_score)/8))):
                return True
            else:
                return False
# 0.9% Disadvantage against Optimal Play. Read the Wikipedia article on Pig for more info.
