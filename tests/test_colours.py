from torpydo.battleship import right_colour
from colorama import Fore

def test_right_colour_hit():
    assert right_colour(True) == Fore.RED

def test_right_colour_water():
    assert right_colour(False) == Fore.BLUE
