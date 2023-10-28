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
            
    
    def end_current_turn(self):
        raise EndTurnException        
    
