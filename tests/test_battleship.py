import unittest

from torpydo.battleship import parse_position, is_fleet_down
from torpydo.ship import Color, Letter, Position, Ship

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

def init_ship(ship: Ship, positions: list):
    ship.positions = positions

    return ship

if '__main__' == __name__:
    unittest.main()
