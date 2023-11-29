def choice(round_score, my_score, opponent_score):
    if (my_score >= 71) or (opponent_score >= 71):
        return round_score >= (100 - my_score)
    else:
        return round_score >= (21 + round(abs(my_score - opponent_score)/8))

# Meant to be 99.1% Optimal
