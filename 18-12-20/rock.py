def rock(p1, p2):
    if p1 == "rock":
        if p2 == "paper":
            return "P2"
        elif p2 == "scissors":
            return "P1"
        elif p2 == "rock":
            return "tie"
        else:
            return "WRONG INPUT BY P2"
    elif p1 == "scissors":
        if p2 == "rock":
            return "P2"
        elif p2 == "paper":
            return "P1"
        elif p2 == "scissors":
            return "tie"
        else:
            return "WRONG INPUT BY P2"
    elif p1 == "paper":
        if p2 == "scissors":
            return "P2"
        elif p2 == "rock":
            return "P1"
        elif p2 == "paper":
            return "tie"
        else:
            return "WRONG INPUT BY P2"
    else:
        return "WRONG INPUT BY P1"
