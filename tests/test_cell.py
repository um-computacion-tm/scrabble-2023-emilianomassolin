import unittest
from game.cell import Cell
from game.tiles import Tile


class TestCell(unittest.TestCase):
    def test_init(self):
        cell = Cell(None,True,multiplier=2, multiplier_type='letter')

        self.assertEqual(
            cell.multiplier,
            2,
        )
        self.assertEqual(
            cell.multiplier_type,
            'letter',
        )
        self.assertIsNone(cell.letter)
        self.assertEqual(
            cell.calculate_value(),
            0,
        )

    def test_add_letter(self):
        cell = Cell(None,True,multiplier=1, multiplier_type='')
        letter = Tile(letter='p', value=3)

        cell.add_letter(letter=letter)

        self.assertEqual(cell.letter, letter)
    def test_cell_value(self):
        cell = Cell(None,True,multiplier=2, multiplier_type='letter')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)

        self.assertEqual(
            cell.calculate_value(),
            6,
        )

    def test_cell_multiplier_word(self):
        cell = Cell(None,True,multiplier=2, multiplier_type='word')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)

        self.assertEqual(
            cell.calculate_value(),
            3,
        )
    def test_repr_with_letter(self):
        cell = Cell("A", "active", 1, "word")
        self.assertEqual(repr(cell),"'A'")

    def test_repr_with_word_multiplier(self):
        cell = Cell(None, "inactive", 3, "word")
        self.assertEqual(repr(cell), 'Wx3')

    def test_repr_with_letter_multiplier(self):
        cell = Cell(None, "active", 2, "letter")
        self.assertEqual(repr(cell), 'Lx2')

    def test_repr_with_default(self):
        cell = Cell(None, "inactive", 1, "word")
        self.assertEqual(repr(cell), '   ')

if __name__ == '__main__':
    unittest.main()