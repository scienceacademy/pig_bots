def choice(round_score, my_score, opponent_score):
    if (myscore >= 71):
        return True
    else (myscore < 71) and (round_score < (21 + round(abs(my_score - opponent_score)/8))):
        return False

# 0.9% Disadvantage against Optimal Play. Read the Wikipedia article on Pig for more info.
