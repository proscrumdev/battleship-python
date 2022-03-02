from unittest import mock
from torpydo.battleship import is_hit_sound

def test_call_right_sound_fire():
    with mock.patch("torpydo.battleship.playsound") as mf:
        is_hit_sound(True)
        mf.assert_called_once_with('sound/explosion.mp3')

def test_call_right_sound_water():
    with mock.patch("torpydo.battleship.playsound") as mf:
        is_hit_sound(False)
        mf.assert_called_once_with('sound/splash.mp3')