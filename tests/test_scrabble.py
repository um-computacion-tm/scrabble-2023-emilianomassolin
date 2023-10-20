from io import StringIO
import unittest
from unittest.mock import patch
from game.scrabble import ScrabbleGame
from game.tiles import Tile
from game.player import Player
from game.dictionary import Dictionary
from game.scrabble import end_game
class TestScrabbleGame(unittest.TestCase):
    def test_init(self):
        scrabble_game = ScrabbleGame(3)
        self.assertIsNotNone(scrabble_game.board)
        self.assertEqual(
            len(scrabble_game.players),
            3,
        )
        self.assertIsNotNone(scrabble_game.bag_tiles)
    def test_next_turn_when_game_is_starting(self):
        #Validar que al comienzo, el turno es del jugador 0
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.next_turn()
        assert scrabble_game.current_player == scrabble_game.players[0]
    def test_next_turn_when_player_is_not_the_first(self):
        #Validar que luego del jugador 0, le toca al jugador 1
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[1]
        scrabble_game.next_turn()
        assert scrabble_game.current_player == scrabble_game.players[2]
    def test_next_turn_when_player_is_last(self):
        #Suponiendo que tenemos 3 jugadores, luego del jugador 3, le toca al jugador 1
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[2]
        scrabble_game.next_turn()
 
        assert scrabble_game.current_player == scrabble_game.players[0]
    def test_validate_diccionari_word(self):
       
       game=ScrabbleGame(3)
       self.assertTrue(game.validate_dictionary_word("auto"))
    def test_check_first_turn(self):
        game=ScrabbleGame(3)
        self.assertEqual(game.check_first_turn(),True)
    def test_end_game(self):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.bag_tiles.tiles = []
        scrabble_game.current_player = scrabble_game.players[0]
        with self.assertRaises(end_game) as context:
            scrabble_game.end_game()
            
    def test_end_game_fail(self):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.bag_tiles.tiles = [
            Tile(letter='H', value=3),
            Tile(letter='O', value=1)
            ]
        game_finish = scrabble_game.end_game()
        self.assertFalse(game_finish, False) 
        
    def test_full_board(self):
        scrabble_game = ScrabbleGame(players_count=2)
        for row in  scrabble_game.board.grid:
            for cell in row:
                cell.letter = Tile("A",1)
        complete_board = scrabble_game.full_board()
        self.assertEqual(complete_board,True) 
        with self.assertRaises(end_game):
          scrabble_game.end_game()    
        

    def test_fill_player_tiles(self):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.bag_tiles.tiles = [
            Tile(letter="H", value=3)  
            ]
        scrabble_game.fill_current_player_tiles()
        self.assertEqual(scrabble_game.current_player.tiles[0].letter, "H")
        self.assertEqual(scrabble_game.current_player.tiles[0].value, 3)  
    
   
   
   
   
    
if __name__ == '__main__':
    unittest.main()