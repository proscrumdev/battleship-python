import random

import colorama
from colorama import Fore, Back, Style

from torpydo.ship import Color, Letter, Position, Ship
from torpydo.game_controller import GameController

my_fleet = []
enemy_fleet = []

def main():
    colorama.init()
    print(Fore.YELLOW + r"""
                                    |__
                                    |\/
                                    ---
                                    / | [
                             !      | |||
                           _/|     _/|-++'
                       +  +--|    |--|--|_ |-
                     { /|__|  |/\__|  |--- |||__/
                    +---------------___[}-_===_.'____                 /\
                ____`-' ||___-{]_| _[}-  |     |_[___\==--            \/   _
 __..._____--==/___]_|__|_____________________________[___\==--____,------' .7
|                        Welcome to Battleship                         BB-61/
 \_________________________________________________________________________|""" + Style.RESET_ALL)

    initialize_game()

    start_game()

def start_game():
    global my_fleet, enemy_fleet

    print(r'''
                  __
                 /  \
           .-.  |    |
   *    _.-'  \  \__/
    \.-'       \
   /          _/
   |      _  /
   |     /_\
    \    \_/
     """"""""''')

    while True:
        print()
        print("Player, it's your turn")
        position = parse_position(input("Enter coordinates for your shot :"))
        is_hit = GameController.check_is_hit(enemy_fleet, position)
        if is_hit:
            print(r'''
                \          .  ./
              \   .:"";'.:..""   /
                 (M^^.^~~:.'"").
            -   (/  .    . . \ \)  -
               ((| :. ~ ^  :. .|))
            -   (\- |  \ /  |  /)  -
                 -\  \     /  /-
                   \  \   /  /''')

        print("Yeah ! Nice hit !" if is_hit else "Miss")

        position = get_random_position()
        is_hit = GameController.check_is_hit(my_fleet, position)
        print()
        print(f"Computer shoot in {position.column.name}{position.row} and {'hit your ship!' if is_hit else 'miss'}")
        if is_hit:
            print(r'''
                \          .  ./
              \   .:"";'.:..""   /
                 (M^^.^~~:.'"").
            -   (/  .    . . \ \)  -
               ((| :. ~ ^  :. .|))
            -   (\- |  \ /  |  /)  -
                 -\  \     /  /-
                   \  \   /  /''')

def parse_position(input: str):
    letter = Letter[input.upper()[:1]]
    number = int(input[1:])

    return Position(letter, number)

def get_random_position():
    rows = 8
    lines = 8

    letter = Letter(random.randint(1, lines))
    number = random.randint(1, rows)

    return Position(letter, number)

def initialize_game():
    initialize_my_fleet()

    initialize_enemy_fleet()

def initialize_my_fleet():
    global my_fleet

    my_fleet = GameController.initialize_ships()

    print("Please position your fleet (Game board has size from A to H and 1 to 8) :")

    for ship in my_fleet:
        print()
        print(f"Please enter the positions for the {ship.name} (size: {ship.size})")

        for i in range(ship.size):
            position_input = input(f"Enter position {i} of {ship.size} (i.e A3):")

            ship.add_position(position_input)

def initialize_enemy_fleet():
    global enemy_fleet

    enemy_fleet = GameController.initialize_ships()

    enemy_fleet[0].positions.append(Position(Letter.B, 4))
    enemy_fleet[0].positions.append(Position(Letter.B, 5))
    enemy_fleet[0].positions.append(Position(Letter.B, 6))
    enemy_fleet[0].positions.append(Position(Letter.B, 7))
    enemy_fleet[0].positions.append(Position(Letter.B, 8))

    enemy_fleet[1].positions.append(Position(Letter.E, 6))
    enemy_fleet[1].positions.append(Position(Letter.E, 7))
    enemy_fleet[1].positions.append(Position(Letter.E, 8))
    enemy_fleet[1].positions.append(Position(Letter.E, 9))

    enemy_fleet[2].positions.append(Position(Letter.A, 3))
    enemy_fleet[2].positions.append(Position(Letter.B, 3))
    enemy_fleet[2].positions.append(Position(Letter.C, 3))

    enemy_fleet[3].positions.append(Position(Letter.F, 8))
    enemy_fleet[3].positions.append(Position(Letter.G, 8))
    enemy_fleet[3].positions.append(Position(Letter.H, 8))

    enemy_fleet[4].positions.append(Position(Letter.C, 5))
    enemy_fleet[4].positions.append(Position(Letter.C, 6))

if __name__ == '__main__':
    main()
