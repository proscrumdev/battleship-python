from torpydo.battleship import overlaps, set_direction, set_forward_rear
from torpydo.ship import Letter, Position, Ship, Color

def test_not_overlaps():
    ship = Ship("test",5,Color.RED)
    ship.add_position("B1")
    assert overlaps(
        [
            Position(Letter.A,1),
            Position(Letter.A,2)
        ],
        fleet=[
            ship
        ]
    ) == False

def test_overlaps():
    ship = Ship("test",5, Color.RED)
    ship.add_position("A2")
    assert overlaps(
        [
            Position(Letter.A,1),
            Position(Letter.A,2)
        ],
        fleet=[
            ship
        ]
    ) == True

def test_set_forward_read():
    assert set_forward_rear(5,3,6) == 0
    assert set_forward_rear(5,1,7) == 1
    assert set_forward_rear(2,3,8) == 1
    assert set_forward_rear(3,5,7) == 1
    assert set_forward_rear(3,5,6) == -1
    
def test_set_direction():
    axis, st_value = set_direction(Position(Letter.A,1))
    assert axis == "horizontal"
    assert st_value == 1
    axis, st_value = set_direction(Position(Letter.A,2))
    assert axis == "vertical"
    assert st_value == 2
    