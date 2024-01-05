def choice(round_score, my_score, opponent_score):
    if my_score + round_score >= 100 or opponent_score >= 100:
        return False

    elif my_score + round_score >= 71 or opponent_score >= 71:
        return True

    else:
        if my_score + round_score >= 21 + abs(my_score - opponent_score) / 8:
            return False
        else:
            return True
