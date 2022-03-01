import unittest

from torpydo.ship import Color, Letter, Position, Ship
from torpydo.game_controller import GameController

class TestBattleship(unittest.TestCase):
    def setUp(self):
        self.ships = []
        self.ships.append(init_ship(Ship("Test", 2, Color.RED), [Position(Letter.A, 1), Position(Letter.A, 2)]))

    def test_check_sunk(self):
        self.assertFalse(self.ships[0].is_sunk)
        GameController.check_is_hit(self.ships, Position(Letter.A, 1))
        self.assertFalse(self.ships[0].is_sunk)
        GameController.check_is_hit(self.ships, Position(Letter.A, 2))
        self.assertTrue(self.ships[0].is_sunk)

def init_ship(ship: Ship, positions: list):
    ship.positions = positions

    return ship
if '__main__' == __name__:
    unittest.main()
