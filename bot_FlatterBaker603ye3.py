tim = 0

def choice(round_score, my_score, opponent_score):
    fun = 0.5
    set_fun = fun
    if round_score + my_score == my_score:
        tim = 0

    tim += 1
    dif = opponent_score - my_score

    if (dif >= 20):
        fun += 0.055
        if (dif >= 35):
            fun += 0.11
            if (dif >= 45):
                fun += 0.22
    elif (dif <= -26):
        fun -= 0.055
        if (dif <= -41):
            fun -= 0.11
            if (dif <= -51):
                fun -= 0.22
    else:
        fun = set_fun

    if round_score < dif or round_score < 20:
        if fun > random():
            if 4*(2**(-tim/2)) < random():
                tim = 0
                return False
            else:
                return True
