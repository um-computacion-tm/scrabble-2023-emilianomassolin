from game.cell import *
from game.tiles import *
class NoCenterLetterException(Exception):
    pass


class Board:
    def __init__(self):
        
        self.grid = [
            [ Cell(None,None,1, '') for _ in range(15) ]
            for _ in range(15)
        ]
        self.add_bonus()
    #diagonales triple palabra, doble palabra, triple letra, doble letra,
    def add_bonus(self):
        
        TRIPLE_WORD_SCORE = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
        DOUBLE_WORD_SCORE = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10))
        TRIPLE_LETTER_SCORE = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
        DOUBLE_LETTER_SCORE = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11), (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))

        for i in TRIPLE_WORD_SCORE:
            self.grid[i[0]][i[1]] = Cell(None,'activate',3,'word')
        for j in TRIPLE_LETTER_SCORE:
            self.grid[j[0]][j[1]] = Cell(None,'activate',3,'letter')
        for k in DOUBLE_WORD_SCORE:
            self.grid[k[0]][k[1]] = Cell(None,'activate',2,'word')
        for l in DOUBLE_LETTER_SCORE:
            self.grid[l[0]][l[1]] = Cell(None,'activate',2,'letter')
 

    
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
        self.word = word
        valid = self.validate_word_inside_board(word, location, orientation)
        self.empty()
        if valid==True:
            if self.is_empty==True:
                for i in self.word:
                    if (self.position_row == 7 and self.position_col == 7) or \
                    (self.position_col == 7 and self.position_row == 7):
                        return True
                    if orientation == "H":
                        self.position_col += 1
                    elif orientation == "V":
                        self.position_row += 1
                return False
            else:
                for i in self.word:
                    cell = self.grid[self.position_row][self.position_col]
                    if cell.letter is not None and i != cell.letter.letter:
                        return False

                    if orientation == "H":
                        self.position_col += 1
                    elif orientation == "V":
                        self.position_row += 1

        return True
    def put_word(self,word:list[Cell],location:tuple,orientation):
        self.empty()
        valid=self.validate_word_place_board(word,location,orientation)
        
        if self.is_empty==False and valid==True:            
         for i in range(len(word)):
             if orientation == "H":
                 self.grid[location[0]][location[1]+i]= word[i].letter.get_letter()
                  
             if orientation== "V":
                 self.grid[location[0]+i][location[1]]=word[i].letter.get_letter()  
        if self.is_empty==True: #primer palabra
            center_position = (7,7)
            if center_position == location and valid==True:
                for i in range(len(word)):
                 if orientation == "H":
                  self.grid[location[0]][location[1]+i]= word[i].letter.get_letter()       
                 if orientation== "V":
                    self.grid[location[0]+i][location[1]]=word[i].letter.get_letter() 
            if center_position!=location and valid==False:
             raise NoCenterLetterException('not center')
 
    #def print_board(self):
    #    for row in self.grid:
    #        row_str = " ".join(str(cell) for cell in row)
    #        print(row_str)      
                
    