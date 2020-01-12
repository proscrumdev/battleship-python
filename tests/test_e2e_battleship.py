import subprocess
import unittest

class TestBattleship(unittest.TestCase):

    def test_play_game_shot_hits(self):
        process = subprocess.Popen(["python", "-m", "torpydo"], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                   stderr=subprocess.DEVNULL)
        positions = ["a1", "a2", "a3", "a4", "a5", "b1", "b2", "b3", "b4", "c1", "c2", "c3", "d1", "d2", "d3", "e1",
                     "e2", "b4"]

        self.write_positions(positions, process)

        result = process.communicate()
        process.stdin.close()
        self.assertIn("Welcome to Battleship", result[0].decode("utf8"))
        self.assertIn("Yeah ! Nice hit !", result[0].decode("utf8"))

    def test_play_game_shot_misses(self):
        process = subprocess.Popen(["python", "-m", "torpydo"], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                   stderr=subprocess.DEVNULL)
        positions = ["a1", "a2", "a3", "a4", "a5", "b1", "b2", "b3", "b4", "c1", "c2", "c3", "d1", "d2", "d3", "e1",
                     "e2", "e4"]

        self.write_positions(positions, process)

        result = process.communicate()
        process.stdin.close()
        self.assertIn("Welcome to Battleship", result[0].decode("utf8"))
        self.assertIn("Miss", result[0].decode("utf8"))

    @staticmethod
    def write_positions(positions, process):
        for position in positions:
            process.stdin.write(position.encode())
            process.stdin.write(b"\n")


if '__main__' == __name__:
    unittest.main()
