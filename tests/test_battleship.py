import unittest

from torpydo.battleship import parse_position

class TestBattleship(unittest.TestCase):
    def test_parse_position_true(self):
        self.assertTrue(parse_position("A1"))

if '__main__' == __name__:
    unittest.main()
