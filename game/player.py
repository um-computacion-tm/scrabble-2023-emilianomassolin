from game.tiles import*

class Player:
    def __init__(self):
        self.name=""
        self.score=0
        self.tiles = []
    def get_score(self):
        return self.score
    def get_tiles(self):
        return self.tiles
        
        
    def increse_score(self,amount):
        self.amount=amount
        self.score+=amount
    
    def take_tiles_from_the_bagtiles(self,bag:BagTiles,amount):
        self.tiles.extend(bag.take(amount)) 
    
    def exchange_tile(self, tile, bag:BagTiles):
        for i in range(len(self.tiles)):
            if self.tiles[i] == tile:
                popped = self.tiles.pop(i)
                bag.put([popped])
                break
        self.tiles.extend(bag.take(1))      
    
    def find_letter_in_tiles(self, letter):
        for tile in self.tiles:
            if tile.get_letter() == letter.upper():
                return tile.get_letter()
        return None  
   
    def give_requested_tiles(self, word):
        letters = []
        for letter in word:
            tile = self.find_letter_in_tiles(letter)
            if tile is not None:
                letters.append(tile)
            else:
                print(f"Letter '{letter}' not found in player's tiles")
                return None
        return letters
   
        
     
         
