from game.tiles import Tile


class Cell:
    def __init__(self,letter,state,multiplier, multiplier_type):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter=letter
        self.state=state
        
        
    def add_letter(self, letter:Tile):
        self.letter = letter

    def calculate_value(self):
        if self.letter is None:
            return 0
        if self.multiplier_type == 'letter'and self.state==True:
            return self.letter.value * self.multiplier
        else:
            return self.letter.value
class calculate_word:
    def __init__(self,word) : 
        self.word=word       
    def calculate_word(self):
        value=0
        for letras in self.word:
            value_letra=Cell.calculate_value(letras)
            value+=value_letra
        for letras in self.word:
            if letras.multiplier_type == 'word' and letras.state == True:
                value = value * letras.multiplier
        return value    
    
        
              
        
        