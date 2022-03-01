import unittest
from unittest.mock import patch, call

from torpydo.utils import print_with_color
from colorama import Fore, Style

class TestBattleship(unittest.TestCase):

    @patch('builtins.print')
    def test_print_with_colors(self, mocked_print):
        print_with_color("test", color=Fore.BLUE)
        assert Fore.BLUE in mocked_print.mock_calls[0].args[0]
        assert Style.RESET_ALL in mocked_print.mock_calls[0].args[0]

if '__main__' == __name__:
    unittest.main()
