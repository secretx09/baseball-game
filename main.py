import random
from field import Field
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Score: 
    def __init__(self):
        self.home_hits, self.away_hits, self.home_runs, self.away_runs = 0, 0, 0, 0

    def update_runs(self, player):
        if player == 1:
            self.home_runs += 1
        else:
            self.away_runs += 1

    def display_score(self, player1_name, player2_name):
        print(f"""|Scoreboard:                 |
|{player1_name} - Runs: {self.home_runs} | Hits: {self.home_hits}|
|{player2_name} - Runs: {self.away_runs} | Hits: {self.away_hits}|\n""")

innings = int(input("How many innings would you like to play? >> "))
player1_name = input("Enter name for Player 1: ")
player2_name = input("Enter name for Player 2: ")

class Game:
    def __init__(self, player1_name, player2_name):
        self.outs = 0
        self.inning = 1
        self.field = Field()
        self.score = Score()
        self.current_player = 1
        self.bases = [False, False, False] #First, Second, Third
        self.player1_name = player1_name
        self.player2_name = player2_name

    def roll(self):
        return sorted([random.randint(1, 6), random.randint(1, 6)])

    def advance_runners(self, bases_to_advance):
        for i in reversed(range(3)):
            if self.bases[i]:
                new_pos = i + bases_to_advance
                if new_pos >= 3:
                    self.bases[i] = False
                    self.score.update_runs(self.current_player)
                    print(f"{self.player1_name if self.current_player == 1 else self.player2_name} scored!")
                else:
                    self.bases[new_pos] = True
                    self.bases[i] = False

    def handle_hit(self, bases_hit):
        # Advance current runners
        self.advance_runners(bases_hit)
        # Place batter on base according to hit
        if bases_hit <= 3:
            self.bases[bases_hit -1] = True

    def handle_out(self, out_type="Out"):
        self.outs += 1
        print(f"{out_type}! Outs: {self.outs}")
        if self.outs >= 3:
            self.end_inning()

    def end_inning(self):
        print(f"Inning {self.inning} over.")
        self.outs = 0
        self.bases = [False, False, False]
        self.field.empty_base(0)
        self.current_player = 2 if self.current_player == 1 else 1
        if self.current_player == 1:
            self.inning += 1  
        self.score.display_score(self.player1_name, self.player2_name)
        self.field.display()
        # After requested amount of innings pass, game should end
        if self.inning > innings:
            if self.score.home_runs != self.score.away_runs:
                winner = 1 if self.score.home_runs > self.score.away_runs else 2
                print(f"Game over! {self.player1_name if winner == 1 else self.player2_name} won after {self.inning - 1} innings.")
                exit(0)

    def attempt_steal(self):
        # Check if there are runners on any base
        if not any(self.bases):
            print("No runners to steal.")
            return

        if self.bases[0]:
            print("Attempting to steal from 1st base.")
            steal_roll = random.randint(1, 6)
            if steal_roll == 1 or steal_roll == 3 or steal_roll == 5:
                print("Steal from 1st successful!")
                self.bases[1] = True
                self.bases[0] = False
            else:
                print("Steal from 1st failed. Runner out.")
                self.bases[0] = False
                self.handle_out("Steal Out")
        
        if self.bases[1]:
            print("Attempting to steal from 2nd base.")
            steal_roll = random.randint(1, 6)
            if steal_roll == 2 or steal_roll == 5:
                print("Steal from 2nd successful!")
                self.bases[2] = True 
                self.bases[1] = False
            else:
                print("Steal from 2nd failed. Runner out.")
                self.bases[1] = False
                self.handle_out("Steal Out")
        
        if self.bases[2]:
            print("Attempting to steal from 3rd base.")
            steal_roll = random.randint(1, 6)
            if steal_roll == 4:
                print("Steal from 3rd successful! Player scores!")
                self.score.update_runs(self.current_player)
                self.bases[2] = False
            else:
                print("Steal from 3rd failed. Runner out.")
                self.bases[2] = False
                self.handle_out("Steal Out")

        self.update_bases_on_field()


    def update_bases_on_field(self):
        if self.bases[0]:
            self.field.fill_base(1)
        else:
            self.field.empty_base(1)
        if self.bases[1]:
            self.field.fill_base(2)
        else:
            self.field.empty_base(2)
        if self.bases[2]:
            self.field.fill_base(3)
        else:
            self.field.empty_base(3)
        self.field.display()

    def handle_roll(self):
        r = self.roll()
        print(f"Dice rolled: {r}")
        # Specific outcomes based on sorted dice roll
        if r == [1, 1] or r == [6, 6]:
            print("Homerun!")
            self.handle_hit(4)
            if self.current_player == 1:
                self.score.home_hits += 1
                self.score.home_runs += 1
                if self.field.fill_base(1):
                    self.score.home_runs += 2
                if self.field.fill_base(2):
                    self.score.home_runs += 3
                if self.field.fill_base(3):
                    self.score.home_runs += 4
            else:
                self.score.away_hits += 1
                self.score.away_runs += 1
                if self.field.fill_base(1):
                    self.score.away_runs += 2
                if self.field.fill_base(2):
                    self.score.away_runs += 3
                if self.field.fill_base(3):
                    self.score.away_runs += 4
            self.field.empty_base(0)
            self.update_bases_on_field()
            return "Homerun"

        elif r == [1, 2] or r == [2, 1] or r == [5, 5]:
            print("Double!")
            self.handle_hit(2)
            if self.current_player == 1:
                self.score.home_hits += 1
            else:
                self.score.away_hits += 1
            self.update_bases_on_field()
            return "Double"

        elif r == [1, 3] or r == [3, 1]:
            self.handle_out("Fly Out")
            return "Fly Out"

        elif r == [1, 4] or r == [4, 1]:
            print("Walk!")
            # Batter takes first base, force runners to advance if needed
            if self.bases[0]:
                if self.bases[1]:
                    if self.bases[2]:
                        # Runner on third scores
                        self.score.update_runs(self.current_player)
                        print(f"Player {self.current_player} scored from walk!")
                    self.bases[2] = self.bases[1]
                self.bases[1] = self.bases[0]
            self.bases[0] = True
            if self.current_player == 1:
                self.score.home_hits += 1
            else:
                self.score.away_hits += 1
            self.update_bases_on_field()
            return "Walk"

        elif r == [1, 5] or r == [5, 1] or r == [4, 5] or r == [5, 4]:
            self.handle_out("Pop Out")
            return "Pop Out"

        elif r == [1, 6] or r == [6, 1]:
            print("Single!")
            self.handle_hit(1)
            if self.current_player == 1:
                self.score.home_hits += 1
            else:
                self.score.away_hits += 1
            self.update_bases_on_field()
            return "Single"

        elif r == [2, 2]:
            # Double play
            if self.outs < 2 and self.bases[0] or self.bases[1] or self.bases[2]:
                print("Double Play!")
                self.handle_out("Out 1 (Double Play)")
                self.handle_out("Out 2 (Double Play)")
                return "Double Play"
            else: 
                self.handle_out("Groundout")
                return "Groundout"
  

        elif r == [2, 3] or r == [3, 2]:
            self.handle_out("Groundout")
            return "Groundout"

        elif r == [2, 4] or r == [4, 2] or r == [2, 6] or r == [6, 2]:
            # Handle dropped third strike chance 50%
            if random.random() < 0.5:
                print("Dropped Third Strike!")
                return "Dropped Third Strike"
            else:
                self.handle_out("Strikeout")
                return "Strikeout"

        elif r == [3, 4] or r == [4, 3]:
            print("Triple!")
            self.handle_hit(3)
            if self.current_player == 1:
                self.score.home_hits += 1
            else:
                self.score.away_hits += 1
            self.update_bases_on_field()
            return "Triple"

        elif r == [5, 6] or r == [6, 5]:
            self.handle_out("Sacrifice Fly")
            # Advance runner from third if any
            if self.bases[2]:
                self.bases[2] = False
                self.score.update_runs(self.current_player)
                print(f"Player {self.current_player} scored on Sacrifice Fly!")
            self.update_bases_on_field()
            return "Sacrifice Fly"

        elif r == [4, 6] or r == [6, 4]:
            # Pickoff attempt, 50% success
            if self.bases[0]:
                if random.random() < 0.5:
                    print("Pickoff! Runner on first out.")
                    self.bases[0] = False
                    self.handle_out("Pickoff")
                else:
                    print("Pickoff attempt failed.")
            else:
                print("No runner to pick off.")
            self.update_bases_on_field()
            return "Pickoff"

        elif r == [3, 5] or r == [5, 3]:
            print("Passed Ball!")
            # Advance all runners one base if any
            self.advance_runners(1)
            self.update_bases_on_field()
            return "Passed Ball"

        elif r == [3, 6] or r == [6, 3]:
            print("Strike!")
            # Optionally count strikes here
            return "Strike"

        elif r == [2, 5] or r == [5, 2]:
            print("Ball!")
            # Optionally count balls here
            return "Ball"

        elif r == [3, 3] or r == [4, 4]:
            print("Bunt!")
            # On bunt, treat as single but force runners advance
            self.handle_hit(1)
            if self.current_player == 1:
                self.score.home_hits += 1
            else:
                self.score.away_hits += 1
            self.update_bases_on_field()
            return "Bunt"

        else:
            print("Unknown roll.")
            return "Unknown"

    def run_game(self):
        while True:
            print(f"{self.player1_name if self.current_player == 1 else self.player2_name}'s turn. Outs: {self.outs}, Inning: {self.inning}")
            action = input("Do you want to 'roll' or 'steal'? ").strip().lower()
            if action == "roll":
                result = self.handle_roll()
            elif action == "steal":
                self.attempt_steal()
                result = "Steal attempt"
            else:
                print("Invalid action. Please type 'roll' or 'steal'.")
                continue
            clear_screen()

            print(f"Result: {result}")
            self.score.display_score(self.player1_name, self.player2_name)
            self.field.display()

            if self.outs >= 3:
                print("Inning over.")
                self.end_inning()

# Main execution
if __name__ == "__main__":
    game = Game(player1_name, player2_name)
    game.run_game()