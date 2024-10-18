import sys
import pandas as pd
from entity.Game import Game
from entity.Fighter import Fighter

def check_power_of_two(n: int):
    if n <= 0:
        return False
    
    if((n & ~(n-1)) == n):
        return True
    
    return False

#main function for the program. It receives one argument with the excel
#containing fighters data
if __name__ == "__main__":
    args = sys.argv

    if len(args) <= 1:
        print("not enough arguments provided.")
    else:
        fighters_file = args[1]
        
        try:
            print("#"*30)
            print("reading files...")
            fighters_df = pd.read_excel(fighters_file)
            valid_n_tournament_participants = check_power_of_two(len(fighters_df))

            print(f'n participants -> {len(fighters_df)}')
            print(f'participant number {"valid" if valid_n_tournament_participants else "invalid"}')
            print("#"*30)

            fighters = {}

            for index, row in fighters_df.iterrows():
                fighters[f"fighter{index}"] = Fighter(**row)

        except Exception as e:
            print("-->Error while reading file")
            print(e)
            sys.exit(1) 

        try:
            if(valid_n_tournament_participants):
                    print("\nlaunching game...")
                    game = Game(fighters=fighters)
                    game.start_game()

        except Exception as e:
            print("--> Error while executing game")
            print(e)
            sys.exit(1)