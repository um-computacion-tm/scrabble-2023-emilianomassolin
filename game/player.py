from game.tiles import *

class Player:
    def __init__(self):
        self.name=""
        self.score=0
        self.tiles = []
        
    def increse_score(self,amount):
        self.amount=amount
        self.score+=amount
        
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
        
     
         
