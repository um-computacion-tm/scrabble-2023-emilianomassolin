import unittest
from game.player import Player
from game.tiles import *


class TestPlayer(unittest.TestCase):
    def test_init(self):
        player_1 = Player()
        self.assertEqual(
            len(player_1.tiles),
            0,   
        )
        self.assertEqual(player_1.score,0)
    def test_increase_score(self):
        player_1=Player()
        player_1.increse_score(2)
        self.assertEqual(player_1.score,2)
    
    def test_take_tiles_from_the_bag(self):
        Player1=Player()
        bag=BagTiles()
        Player1.take_tiles_from_the_bagtiles(bag,2)
        self.assertEqual(len(Player1.tiles),2)        
    def test_player_exchange(self):
        player = Player()
        bag = BagTiles()
        player.take_tiles_from_the_bagtiles(bag, 2)
        tile = player.tiles[0]
        player.exchange_tile(player.tiles[0], bag)
        self.assertFalse(tile == player.tiles[0])    
        
        
    def test_validate_user_has_letters(self):
        bag_tile = BagTiles()
        bag_tile.tiles = [
            Tile(letter='H', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
            Tile(letter='C', value=1),
            Tile(letter='U', value=1),
            Tile(letter='M', value=1),
        ]
        player1 = Player()
        for i in bag_tile.tiles:
            player1.tiles.append(i)
        tiles = [
            Tile(letter='H', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
        ]
        is_valid = player1.has_letters(tiles)
        self.assertEqual(is_valid, True)

    def test_validate_fail_when_user_has_not_letters(self):
           bag_tile = BagTiles()
           bag_tile.tiles = [
            Tile(letter='P', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
            Tile(letter='C', value=1),
            Tile(letter='U', value=1),
            Tile(letter='M', value=1),
        ]
           player1 = Player()
           for i in bag_tile.tiles:
            player1.tiles.append(i)
           tiles = [
            Tile(letter='H', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
        ]

           is_valid = player1.has_letters(tiles)
           self.assertEqual(is_valid, False)

            
            
if __name__ == '__main__':
    unittest.main()