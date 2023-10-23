class Tile:   
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value
    def get_letter(self):
        return self.letter
    def get_value(self):
        return self.value
    def set_letter(self, new_letter):
        self.letter = new_letter
