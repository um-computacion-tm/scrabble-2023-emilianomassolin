import unittest
from game.board import Board
from game.tiles import Tile
from game.cell import Cell
class TestBoard(unittest.TestCase):
    def test_init(self):
        board = Board()
        self.assertEqual(
            len(board.grid),
            15,
        )
        self.assertEqual(
            len(board.grid[0]),
            15,
        )
    def test_board_cell_00(self):
        board = Board()
        board.add_bonus()
        cell = board.grid
        self.assertEqual(cell[0][0].multiplier,3 )
        self.assertEqual(cell[0][0].multiplier_type,'W' )
    def test_board_cell_33(self):
        board=Board()
        board.add_bonus()
        cell=board.grid
        self.assertEqual(cell[3][3].multiplier,2)
        self.assertEqual(cell[3][3].multiplier_type,'W')
    def test_word_inside_board(self):
         board= Board()
         word = "Facultad"
         location = (5, 4)
         orientation = "H"
         word_is_valid = board.validate_word_inside_board(word, location, orientation)
         assert word_is_valid == True
    def test_word_out_of_board(self):
        board = Board()
        word = "Facultad"
        location = (4, 14)
        orientation = "H"
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        assert word_is_valid == False
    def test_word_inside_board_vertical(self):
        board = Board()
        word = "FACULTAD"
        location = (5, 4)
        orientation = "V"
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        assert word_is_valid == True
    def test_board_is_empty(self):
        board = Board()
        board.empty()
        assert board.is_empty == True
    def test_board_is_not_empty(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1))
        board.empty()
        assert board.is_empty == False
    def test_place_word_empty_board_horizontal_fine(self):
         board = Board()
         word = "FACULTAD"
         location = (7, 4)
         orientation = "H"
         word_is_valid = board.validate_word_place_board(word, location, orientation)
         assert word_is_valid == True  
    def test_place_word_empty_board_horizontal_wrong(self):
         board = Board()
         word = "FACULTAD"
         location = (2, 4)
         orientation = "H"
         word_is_valid = board.validate_word_place_board(word, location, orientation)
         assert word_is_valid == False
    def test_place_word_empty_board_vertical_fine(self):
         board = Board()
         word = "FACULTAD"
         location = (4, 7)
         orientation = "V"
         word_is_valid = board.validate_word_place_board(word, location, orientation)
         assert word_is_valid == True  
    def test_place_word_empty_board_vertical_wrong(self):
         board = Board()
         word = "FACULTAD"
         location = (2, 4)
         orientation = "V"
         word_is_valid = board.validate_word_place_board(word, location, orientation)
         assert word_is_valid == False
    def test_place_word_not_empty_board_horizontal_fine(self):
         board = Board()
         board.grid[7][7].add_letter(Tile('C', 1))
         board.grid[8][7].add_letter(Tile('A', 1)) 
         board.grid[9][7].add_letter(Tile('S', 1)) 
         board.grid[10][7].add_letter(Tile('A', 1)) 
         word = "FACULTAD"
         location = (8, 6)
         orientation = "H"
         word_is_valid = board.validate_word_place_board(word, location, orientation)
         assert word_is_valid == True  
    def test_place_word_not_empty_board_horizontal_not_fine(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1))
        board.grid[8][7].add_letter(Tile('A', 1)) 
        board.grid[9][7].add_letter(Tile('S', 1)) 
        board.grid[10][7].add_letter(Tile('A', 1)) 
        word = "MISA"
        location = (8, 6)
        orientation = "H"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == False
    def test_place_word_not_empty_board_vertical_fine(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1))
        board.grid[7][8].add_letter(Tile('A', 1)) 
        board.grid[7][9].add_letter(Tile('S', 1)) 
        board.grid[7][10].add_letter(Tile('A', 1)) 
        word = "FACULTAD"
        location = (6, 8)
        orientation = "V"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == True
    def test_place_word_not_empty_board_vertical_not_fine(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1))
        board.grid[7][8].add_letter(Tile('A', 1)) 
        board.grid[7][9].add_letter(Tile('S', 1)) 
        board.grid[7][10].add_letter(Tile('A', 1)) 
        word = "MISA"
        location = (6, 8)
        orientation = "V"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == False  
    
 
    def test_check_word_left(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1))
        board.grid[7][8].add_letter(Tile('A', 1)) 
        board.grid[7][9].add_letter(Tile('S', 1)) 
        board.grid[7][10].add_letter(Tile('A', 1)) 
        word = board.check_word_left(row=7, col=11)
        self.assertEqual(word[0].get_tile().get_letter(),'C')
        self.assertEqual(word[1].get_tile().get_letter(),'A')
        self.assertEqual(word[2].get_tile().get_letter(),'S')
        self.assertEqual(word[3].get_tile().get_letter(),'A')
        
    
if __name__ == '__main__':
    unittest.main()