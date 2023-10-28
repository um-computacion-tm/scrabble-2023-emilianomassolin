import os
from game.scrabble import *


def clean_terminal():
    os.system('clear')

def players_to_play():
    while True:
        try: 
            player = int(input("Enter the number of players(2-4): "))
            if player <= 1 or player > 4:
                raise ValueError
            return player
        except ValueError:
            print("Invalid number")
            



class ScrabbleCli:
    def __init__(self, players):
        self.game = ScrabbleGame(players)

    def name_players(self, players):
        for i in range(players):
            name = str(input(f"Enter name of player {i+1}: " ))
            self.game.players[i].name = name
                        
    def show_score(self):
        print(self.game.current_player.score)
    
    def show_tiles(self):
        print(self.game.current_player.tiles)
        
    def show_current_player(self):
        print(f"Turn of player {self.game.current_player.name}")
        
    def exchange_index_tile(self):
        index_exchange = int(input(f"Enter index of tile to change (0-{len(self.game.current_player.tiles)-1}): "))
        tile_exchange = self.game.current_player.tiles[index_exchange]
        self.game.current_player.exchange_tile(self.game.bag_tiles ,tile_exchange)
        
    def choose_wildcard(self):
        wildcard = self.game.check_wildcard()
        if wildcard:
            for i in self.game.current_player.tiles:
                if i.value == 0:
                    letter_for_wild = str(input("Enter letter for wildcard:"))
                    letter_for_wild = letter_for_wild.upper()
                    i.set_letter(letter_for_wild)
            
    def get_row(self):
        while True:
            try:
                row = int(input("Enter row(0-14): "))
                if row < 0 or row >= 15:
                    raise ValueError
                return row
            except ValueError:
                print("Invalid number of row")

    def get_col(self):
        while True:
            try:
                col = int(input("Enter col(0-14): "))
                if col < 0 or col >= 14:
                    raise ValueError
                return col
            except ValueError:
                print("Invalid number of col")
            
    def get_orientation(self):
        while True:
            try:
                orientation = str(input("Enter orientation(H/V): "))
                orientation = orientation.upper()
                if orientation == "H" or orientation == "V":
                    return orientation
                raise ValueError
            except ValueError:
                print("Invalid orientation")
                

    #        
    def end_current_turn(self):
        raise EndTurnException        
    
  
    def show_results(self):
        print("The Game has ended")
        leaderboard = self.game.sort_players_by_score()
        print(leaderboard)
        print(f"The winner is: {leaderboard[0][0]}")