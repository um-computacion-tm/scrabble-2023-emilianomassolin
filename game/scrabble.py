from game.board import Board
from game.player import Player
from game.tiles import BagTiles

class ScrabbleGame:
    def __init__(self, players_count: int):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players:list[Player] = []
        for _ in range(players_count):
            self.players.append(Player())
        
        self.current_player = None
    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        else:
            index = self.players.index(self.current_player) + 1
            if index < len(self.players): 
                self.current_player = self.players[index]
            else:
                self.current_player = self.players[0]
    #def validate_word(self, word, location, orientation):
    #    '''
    #    1- Validar que usuario tiene esas letras
    #    2- Validar que la palabra entra en el tablero
    #    '''
    #    self.board.validate_word_inside_board(word, location, orientation)
    #
    #def get_words():
    #    '''
    #    Obtener las posibles palabras que se pueden formar, dada una palabra, ubicacion y orientacion 
    #    Preguntar al usuario, por cada una de esas palabras, las que considera reales
    #    '''
    #
    #def put_words():
    #    '''
    #    Modifica el estado del tablero con las palabras consideradas como correctas
    #    '''