import random

class Score: 
    home_hits, away_hits, home_runs, away_runs = 0, 0, 0, 0

class Game:
    def roll():
        return [random.randint(1, 6) for i in range(2)] #ex: [4,2]
    
    r = roll()

    outs = 0
    inning = 0

    if r == [1, 1] or r == [6, 6]:
        print("Homerun")

    elif r == [1, 2] or r == [2, 1] or r == [5, 5]:
        print("Double")

    elif r == [1, 3] or r == [3, 1] or r == [3, 6] or r == [6, 3]:
        print("Fly Out")

    elif r == [1, 4] or r == [4, 1] or r == [3, 3] or r == [4, 4]:
        print("Walk")

    elif r == [1, 5] or r == [5, 1] or r == [4, 5] or r == [5, 4]:
        print("Pop Out")

    elif r == [1, 6] or r == [6, 1] or r == [2, 5] or r == [5, 2]:
        print("Single")

    elif r == [2, 2]:
        print("Double Play")

    elif r == [2, 3] or r == [3, 2] or r == [3, 5] or r == [5, 3]:
        print("Groundout")
    
    elif r == [2, 4] or r == [4, 2] or r == [2, 6] or r == [6, 2] or r == [4, 6] or r == [6, 4]:
        print("Strikeout")

    elif r == [3, 4] or r == [4, 3]:
        print("Triple")

    elif r == [5, 6] or r == [6, 5]:
        print("Sacrifice Fly")