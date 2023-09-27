from game.tiles import *

class Player:
    def __init__(self):
        self.tiles = []
    def has_letters(self, tiles1):
        comparacion=len(tiles1)
        for i in tiles1:
            for j in self.tiles:
                if i.letter == j.letter:
                 comparacion -=1
        if comparacion==0:
            return True
        else:
            return False        
        
     
         
