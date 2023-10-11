from game.board import Board
from game.player import Player
from game.bag_tiles import BagTiles
from game.dictionary import Dictionary
from game.tiles import Tile
class end_game(Exception):
    pass
class end_turn(Exception):
    pass
class ScrabbleGame:
    def __init__(self, players_count: int):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players:list[Player] = []
        self.dictionary = Dictionary('dictionaries/dictionary.txt')
        self.last_word=[]
        self.current_player = 0
        self.game_state=None
        for _ in range(players_count):
            self.players.append(Player())
        
    def next_turn(self):
        if self.current_player == 0:
            self.current_player = self.players[0]
        else:
            index = self.players.index(self.current_player) + 1
            if index < len(self.players): 
                self.current_player = self.players[index]
            else:
                self.current_player = self.players[0]
    def validate_dictionary_word(self, word):
        word = word.lower()
        return(self.dictionary.has_word(word))
    def show_board(self): 
     print('\n  |' + ''.join([f' {str(row_index).rjust(2)} ' for row_index in range(15)]))
     for row_index, row in enumerate(self.board.grid):
        print(
            str(row_index).rjust(2) +
            '| ' +
            ' '.join([repr(square) for square in row])
        )        
    def check_first_turn(self):
        self.board.empty()
        return self.board.is_empty
   # def play_turn(self):
   #     word = input("Give a word to enter: ").lower()
   #     row = int(input("starting position row: "))
   #     column = int(input("starting position column: "))
   #     location=(row,column)
   #     direction = input("Select direction (H or V: )")
   #     word = self.players[self.current_player].give_requested_tiles(word)
   #     self.board.put_word(word, location, direction)
   #     self.players[self.current_player].forfeit_tiles(word)
   #     self.players[self.current_player].increse_score(word_score(self.last_word))
   #     self.next_turn()
    
    def full_board(self):
        for row in self.board.grid:
            for cell in row:
                if cell.letter == None:
                    return False
        return True
    
    def end_game(self):
        full_board = self.full_board()
        if full_board==True:
            raise end_game
        elif len(self.bag_tiles.tiles)==0:
                if len(self.current_player.tiles)==0:
                    raise end_game
        else:
            pass  
    def show_current_player(self):
        print(f"Turno del jugador {self.current_player.name}")
    #def fill_current_player_tiles(self):
    #    self.current_player.tiles.extend(self.bag_tiles.take(7-len(self.current_player.tiles)))  
    #def show_tiles(self):
    #    lista=self.current_player.tiles
    #    for i in lista:
    #        print(i.get_letter(), end=" , ")
    #    print(" ")    
    def show_score(self):
        print("su puntaje es :",self.current_player.score)  
    #def exchange_index_tile(self):
    #    index_exchange = int(input(f"Ingrese indice de ficha a cambiar (0-{len(self.current_player.tiles)-1}): "))
    #    tile_exchange = self.current_player.tiles[index_exchange]
    #    self.current_player.exchange_tile(tile_exchange ,self.bag_tiles)  
    def end_current_turn(self):
        raise end_turn  
                
    #def actual_turn(self):
    #    self.fill_current_player_tiles()
    #    while True:
    #        option = int(input(
    #            "Indique un número:\n"
    #            "0. Colocar palabra\n"
    #            "1. Mostrar Tiles\n"
    #            "2. Mostrar Tablero\n"
    #            "3. Mostrar Puntaje\n"
    #            "4. Intercambiar Fichas\n"
    #            "5. Terminar turno\n"
    #            "6. Salir\n"
    #            "= "
    #        ))
    #        try:
    #            if option == 0:   
    #                word=input("Coloque la palabra").upper()
    #                first_row=int(input("coloque la fila"))
    #                first_col=int(input("coloque la columna"))
    #                orientation=input("colocar orientacion H O V").upper()
    #                location=(first_row,first_col)
    #                self.current_player.give_requested_tiles(word)
    #                self.dictionary.has_word(word)
    #                self.board.put_word(word,location,orientation)
#
    #            elif option == 1:
    #                self.show_tiles()                
    #            elif option == 2:
    #                self.show_board()
    #            elif option == 3:
    #                self.show_score() 
    #            elif option == 4:
    #                tile_changes = int(input("Indique la cantidad de cambios a realizar: "))
    #                for _ in range(tile_changes):
    #                    self.exchange_index_tile()
    #                    self.show_tiles()
    #                self.end_current_turn() 
    #            elif option == 5:
    #                self.end_current_turn()
    #            elif option == 6:
    #                raise end_game  
    #            else:
    #                pass
    #        except end_turn:
    #            print("Fin del turno")
    #            break
#
    