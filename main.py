import random

class Game:
    outs = 0
    inning = 0


class Score: 
    home_hits, away_hits, home_runs, away_runs = 0

def roll(n=2, d_side=6):
    return [random.randint(1,d_side) for i in range(n)]

r = roll(d_side=100)
