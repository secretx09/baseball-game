import random

class Score: 
    home_hits, away_hits, home_runs, away_runs = 0, 0, 0, 0

class Game:
    def roll():
        return [random.randint(1, 6) for i in range(2)] #ex: [4,2]
    
    r = roll()

    outs = 0
    inning = 0
    
    if r == [1, 5]:
        print("test success")
