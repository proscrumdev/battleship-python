import unittest

from torpydo.game_controller import GameController
from torpydo.ship import Color, Letter, Position, Ship

class TestShip(unittest.TestCase):
    def setUp(self):
        self.ships = []
        self.ships.append(init_ship(Ship("Test", 2, Color.RED), [Position(Letter.A, 1), Position(Letter.A, 2)]))

    def test_check_is_hit_true(self):
        self.assertTrue(GameController.check_is_hit(self.ships, Position(Letter.A, 1)))

    def test_check_is_hit_false(self):
        self.assertFalse(GameController.check_is_hit(self.ships, Position(Letter.B, 1)))

    def test_check_is_hit_position_none(self):
        with self.assertRaises(ValueError):
            self.assertRaises(GameController.check_is_hit(self.ships, None))

    def test_check_is_hit_ship_none(self):
        with self.assertRaises(ValueError):
            self.assertRaises(GameController.check_is_hit(None, Position(Letter.A, 1)))

    def test_is_ship_valid_false(self):
        self.assertFalse(GameController.is_ship_valid(Ship("Not Valid", 3, Color.RED)))

    def test_is_ship_valid_true(self):
        self.assertTrue(GameController.is_ship_valid(self.ships[0]))

def init_ship(ship: Ship, positions: list):
    ship.positions = positions

    return ship

if '__main__' == __name__:
    unittest.main()
