def choice(round_score, my_score, opponent_score):
    threshold = 20

    if round_score < threshold:
        return True
    else:
        return False
