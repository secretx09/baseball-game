import random

class Score: 
    def __init__(self):
        self.home_hits, self.away_hits, self.home_runs, self.away_runs = 0, 0, 0, 0

class Game:
    def __init__(self):
        self.outs = 0
        self.inning = 0
    
        #0 means empty
        self.base_1 = 0

    def roll():
        return [random.randint(1, 6) for i in range(2)] #ex: [4,2]
    



    def handle_roll(self):
        r = self.roll()
        if r == [1, 1] or r == [6, 6]:
            return "Homerun"

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

class Team:
    def __init__(self):
        self.runs = 0 
        #self.bench = ["player4", ]