from game.cell import Cell
from game.tiles import *

class Board:
    def __init__(self):
        self.grid = [
            [ Cell(None,None,1, '') for _ in range(15) ]
            for _ in range(15)
        ]
    def validate_word_inside_board(self, word, location, orientation):
        self.word = word
        self.orientation = orientation
        self.position_row = location[0]
        self.position_col = location[1] 
        if orientation == 'H' and len(self.word)<=15-self.position_col:
            return True
        elif orientation == 'V' and len(self.word)<=15-self.position_row:
            return True
        else:
            return False
        
    def empty(self):
        if self.grid[7][7].letter == None:
            self.is_empty = True
        else:
            self.is_empty = False
   
    def validate_word_place_board(self, word, location, orientation):
        valid = self.validate_word_inside_board(word, location, orientation)
        self.empty()
        if self.is_empty == False:
            if valid == True:
                if orientation == "H":
                    for i in self.word:
                        index = self.position_col
                        if self.grid[self.position_row][index].letter is not None:
                            if i != self.grid[self.position_row][index].letter.letter:
                                return False
                        self.position_col += 1
                    return True
                else:
                    for i in self.word:
                        index = self.position_row
                        if self.grid[index][self.position_col].letter is not None:
                            if i != self.grid[index][self.position_col].letter.letter:    
                                return False
                        self.position_row += 1
                    return True
        else:
            if valid == True:
                for i in self.word:
                    if orientation == "H":
                        index = self.position_col
                        if self.position_row == 7 and index == 7:
                            return True
                        self.position_col += 1 
                    else:
                        index = self.position_row
                        if self.position_col == 7 and index == 7:
                            return True
                        self.position_row += 1 
                return False
        
            