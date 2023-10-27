from game.cell import  Cell
from game.tiles import Tile
from game.bag_tiles import BagTiles

class Board:
    def __init__(self):        
        self.grid = [
            [ Cell(None,True,1, '') for _ in range(15) ]for _ in range(15)]
        self.is_empty=None
    #diagonales triple palabra, doble palabra, triple letra, doble letra,
    def add_bonus(self):
        TRIPLE_WORD_SCORE = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14),(7, 14), (14,14))
        DOUBLE_WORD_SCORE = ((1,1),(2,2),(3,3),(4,4),(10,10),(11,11),(12,12),(13,13),(1,13),(2,12),(3,11), (4,10),(7,7),(13,1),(12,2),(11,3),(10,4))
        TRIPLE_LETTER_SCORE = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
        DOUBLE_LETTER_SCORE = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11), (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))
        for i in TRIPLE_WORD_SCORE:
            self.grid[i[0]][i[1]] = Cell(None,'activate',3,'W')
        for j in TRIPLE_LETTER_SCORE:
            self.grid[j[0]][j[1]] = Cell(None,'activate',3,'L')
        for k in DOUBLE_WORD_SCORE:
            self.grid[k[0]][k[1]] = Cell(None,'activate',2,'W')
        for l in DOUBLE_LETTER_SCORE:
            self.grid[l[0]][l[1]] = Cell(None,'activate',2,'L')
    def validate_word_inside_board(self, word, location, orientation):
        if isinstance(word, list): 
                for i in word:
                    self.word = [letter.upper() for letter in word]
        else:
            self.word = word.upper()
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
    def validate_word_place_board_is_empty(self, orientation):
        for i in self.word:
            if self.position_row == 7 and self.position_col == 7:
                return True
            if orientation == "H":
                self.position_col += 1
            elif orientation == "V":
                self.position_row += 1
        return False      
    
    def validate_word_place_board_is_not_empty(self, orientation):
        for i in self.word:
            cell = self.grid[self.position_row][self.position_col]
            if cell.letter is not None and i != cell.letter.letter:
                return False
            if cell.letter is not None and cell.letter.letter == i:
                if isinstance(self.missing_letters,list):
                    self.missing_letters = [letter for letter in self.missing_letters if letter != i]
                else:
                    self.missing_letters = self.missing_letters.replace(i, "")
            if orientation == "H":
                self.position_col += 1
            elif orientation == "V":
                self.position_row += 1
        return True
    
    def validate_word_place_board(self, word, location, orientation):
        if isinstance(word, list): 
                for i in word:
                    word = [letter.upper() for letter in word]
        else:
            word = word.upper()
        valid = self.validate_word_inside_board(word, location, orientation)
        self.empty()
        self.missing_letters = word
        if valid==True:
            if self.is_empty==True:
                return self.validate_word_place_board_is_empty(orientation)
            else:
                return self.validate_word_place_board_is_not_empty(orientation)
        return False

                    
