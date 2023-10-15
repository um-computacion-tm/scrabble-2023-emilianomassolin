import unittest
from game.dictionary import Dictionary,NoDictoniaryException
class TestDictionary(unittest.TestCase):
    def test_dictionary(self):
        dictionary = Dictionary('dictionaries/dictionary.txt')
        self.assertTrue(dictionary.has_word('auto'))
    def test_word_false(self):
        dictionary = Dictionary('dictionaries/dictionary.txt')
        with self.assertRaises (NoDictoniaryException):
            dictionary.has_word('ard')
if __name__ == '__main__':
    unittest.main()