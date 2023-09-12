from game.cell import Cell

class Board:
    def __init__(self):
        self.grid = [
            [ Cell(None,None,1, '') for _ in range(15) ]
            for _ in range(15)
        ]
    def validate_word_inside_board(self, word, location, orientation):
        self.word = word
        self.orientation = orientation
        self.position_x = location[0]
        self.position_y = location[1] 
        if orientation == 'H' and len(self.word)<=15-self.position_x:
            for i in self.word:
                index = self.position_x
                self.grid[index][self.position_y] = i
                self.position_x += 1 
            return True
        elif orientation == 'V' and len(self.word)<=15-self.position_y:
            for i in self.word:
                index = self.position_y
                self.grid[self.position_x][index] = i
                self.position_y += 1 
            return True
        else:
            return False