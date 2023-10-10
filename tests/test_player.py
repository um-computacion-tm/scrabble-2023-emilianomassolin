import unittest
from game.player import Player
from game.bag_tiles import BagTiles
from game.tiles import Tile
class TestPlayer(unittest.TestCase):
    def test_init(self):
        player_1 = Player()
        self.assertEqual(
            len(player_1.tiles),
            0,   
        )
        self.assertEqual(player_1.score,0)
    def test_get_score(self):
        player=Player()
        score=player.get_score()
        print(score)
        self.assertEqual(score,0)
    def test_get_tiles(self):
        player=Player()
        tiles=player.get_tiles()
        self.assertEqual(tiles,[])    
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
    def test_find_letter_in_tiles(self):
        player = Player()
        player.tiles = [Tile('A', 1), Tile('B', 3), Tile('C', 1)]
        letra = player.find_letter_in_tiles('B')
        self.assertEqual(letra,"B")
    def test_not_find_letter_in_tiles(self):
        player=Player()
        player.tiles=[Tile('A', 1), Tile('B', 3), Tile('C', 1)] 
        resultado=player.find_letter_in_tiles("x")
        self.assertEqual(resultado,None)    
    def test_give_requested_tiles(self):
        player=Player()
        player.tiles=  [
            Tile(letter='H', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
        ]  
        valid=player.give_requested_tiles('HOLA')
        list=['H','O','L','A']
        self.assertEqual(valid,list)  
    def test_not_give_request_tiles(self):
        player=Player() 
        player.tiles=  [
            Tile(letter='H', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
        ]       
        valid=player.give_requested_tiles('holas')
        list=['H','O','L','A','S']
        self.assertEqual(valid,None)
    def test_get_name (self):
        player=Player()
        player.name="emi"
        self.assertEqual(player.get_name(),"emi")   
    def test_set_name (self):
        player=Player()
        player.set_name("emi")
        self.assertEqual(player.get_name(),"emi") 
    def test_show_tiles(self):
        player=Player()
        player.tiles=["A","B"]
        self.assertEqual(player.show_tiles(),["A","B"])  
if __name__ == '__main__':
    unittest.main()