import unittest

from torpydo.battleship import parse_position, is_fleet_down, get_random_position
from torpydo.ship import Color, Letter, Position, Ship
from unittest.mock import patch

class TestBattleship(unittest.TestCase):
    def setUp(self):
        self.ships = []
        self.ships.append(init_ship(Ship("Test", 2, Color.RED), [Position(Letter.A, 1), Position(Letter.A, 2)]))

    def test_parse_position_true(self):
        self.assertTrue(parse_position("A1"))

    def test_is_fleet_down(self):
        self.assertFalse(is_fleet_down(self.ships))
        self.ships[0].is_sunk = True
        self.assertTrue(is_fleet_down(self.ships))

    @patch("torpydo.battleship.NUMBER_ROWS", 2)
    @patch("torpydo.battleship.NUMBER_COL", 2)
    def test_random_duplicate_position(self):
        for i in range(10):
            board = []
            x = [
                get_random_position(board),
                get_random_position(board),
                get_random_position(board),
                get_random_position(board),
            ]
            y = list(set(x))
            self.assertTrue(len(y) == 4)

def init_ship(ship: Ship, positions: list):
    ship.positions = positions

    return ship

if '__main__' == __name__:
    unittest.main()
