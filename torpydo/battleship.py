import random
import os
import colorama
import platform

from typing import List, Tuple
from colorama import Fore, Style
from torpydo.ship import Color, Letter, Position, Ship
from torpydo.game_controller import GameController
from torpydo.telemetryclient import TelemetryClient

import time

myFleet = []
enemyFleet = []
board = []
BAD_POSITION_INPUT_MSG = "The position is invalid. Please try enter a letter and a number like: 'A1'"
NUMBER_ROWS = 8
NUMBER_COL = 8

print("Starting")

def main():
    TelemetryClient.init()
    TelemetryClient.trackEvent('ApplicationStarted', {'custom_dimensions': {'Technology': 'Python'}})
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

def right_colour(is_hit:bool):
    if is_hit:
        colour = Fore.RED
    else:
        colour = Fore.BLUE
    return colour

def start_colouring(colour):
    print(colour)

def end_colouring():
    print(Style.RESET_ALL)

def start_game():
    global myFleet, enemyFleet
    # clear the screen
    if(platform.system().lower()=="windows"):
        cmd='cls'
    else:
        cmd='clear'
    os.system(cmd)
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

        # Player
        start_colouring(Fore.GREEN)
        print("Player, it's your turn")
        print("Coordinates should be written in the following format 'LetterNumber' as in C1, F4")
        try:
            position = parse_position(check_position_input("Enter coordinates (A-H, 1-8) for your shot :"))
        except Exception:
            print(BAD_POSITION_INPUT_MSG)
            continue
        end_colouring()

        is_hit = GameController.check_is_hit(enemyFleet, position)
        add_position_to_board(board, position, True)

        start_colouring(right_colour(is_hit))
        print("Yeah ! Nice hit !" if is_hit else "Miss")
        TelemetryClient.trackEvent('Player_ShootPosition', {'custom_dimensions': {'Position': str(position), 'IsHit': is_hit}})

        print( r'''
            \          .  ./
          \   .:"";'.:..""   /
             (M^^.^~~:.'"").
        -   (/  .    . . \ \)  -
           ((| :. ~ ^  :. .|))
        -   (\- |  \ /  |  /)  -
             -\  \     /  /-
               \  \   /  /''')

        end_colouring()
        if is_fleet_down(enemyFleet):
            start_colouring(Fore.MAGENTA)
            print("Congratulations! You are the winner \o/")
            end_colouring()
            break

        print("\n\nComputer is thinking...")
        time.sleep(3)
        # Computer
        position = get_random_position()
        is_hit = GameController.check_is_hit(myFleet, position)
        add_position_to_board(board, position, True)
        start_colouring(right_colour(is_hit))

        print()
        print(f"Computer shoot in {str(position)} and {'hit your ship!' if is_hit else 'miss'}")
        TelemetryClient.trackEvent('Computer_ShootPosition', {'custom_dimensions': {'Position': str(position), 'IsHit': is_hit}})
        print(r'''
            \          .  ./
          \   .:"";'.:..""   /
             (M^^.^~~:.'"").
        -   (/  .    . . \ \)  -
           ((| :. ~ ^  :. .|))
        -   (\- |  \ /  |  /)  -
             -\  \     /  /-
               \  \   /  /''')
        end_colouring()
        if is_fleet_down(myFleet):
            start_colouring(Fore.LIGHTRED_EX)
            print("Sorry, you lost...")
            end_colouring()
            break

    print("Thank you for playing!")

def is_fleet_down(fleet):
    return all(ship.is_sunk for ship in fleet)

def parse_position(input: str):
    letter = Letter[input.upper()[:1]]
    number = int(input[1:])

    return Position(letter, number)

def add_position_to_board(board: list, position: Position, is_shot = None):
    if is_shot is True:
        position.is_shot = True

    if position not in board:
        board.append(position)

def get_random_position(board: list):
    rows = NUMBER_ROWS
    lines = NUMBER_COL

    while True:
        letter = Letter(random.randint(1, lines))
        number = random.randint(1, rows)
        position = Position(letter, number)
        for pos in board:
            if position == pos:
                position = pos
                break

        add_position_to_board(board, position)
        if not position.is_shot:
            position.is_shot = True
            return position

def initialize_game():

    initialize_enemyFleet()
    initialize_myFleet()

    

def initialize_myFleet():
    global myFleet

    myFleet = GameController.initialize_ships()

    quick_and_dirty = False
    if quick_and_dirty:
        myFleet[0].positions.append(Position(Letter.B, 4))
        myFleet[0].positions.append(Position(Letter.B, 5))
        myFleet[0].positions.append(Position(Letter.B, 6))
        myFleet[0].positions.append(Position(Letter.B, 7))
        myFleet[0].positions.append(Position(Letter.B, 8))

        myFleet[1].positions.append(Position(Letter.E, 6))
        myFleet[1].positions.append(Position(Letter.E, 7))
        myFleet[1].positions.append(Position(Letter.E, 8))
        myFleet[1].positions.append(Position(Letter.E, 9))

        myFleet[2].positions.append(Position(Letter.A, 3))
        myFleet[2].positions.append(Position(Letter.B, 3))
        myFleet[2].positions.append(Position(Letter.C, 3))

        myFleet[3].positions.append(Position(Letter.F, 8))
        myFleet[3].positions.append(Position(Letter.G, 8))
        myFleet[3].positions.append(Position(Letter.H, 8))

        myFleet[4].positions.append(Position(Letter.C, 5))
        myFleet[4].positions.append(Position(Letter.C, 6))

    else:
        print("Please position your fleet (Game board has size from A to H and 1 to 8) :")

        for ship in myFleet:
            print()
            print(f"Please enter the positions for the {ship.name} (size: {ship.size})")

            i = 0
            while i < ship.size:
                try:
                    position_input = check_position_input(f"Enter position {i+1} of {ship.size} (i.e A3):")
                except Exception:
                    print(BAD_POSITION_INPUT_MSG)
                    continue
                else:
                    ship.add_position(position_input)
                    i += 1
                    TelemetryClient.trackEvent('Player_PlaceShipPosition', {'custom_dimensions': {'Position': position_input, 'Ship': ship.name, 'PositionInShip': i}})


def overlaps(positions, fleet:List[Ship]):
    for ship in fleet:
        for ship_pos in ship.positions:
            if ship_pos in positions:
                return True
    return False

def set_forward_rear(ship_size, init_value, max_size) -> int:
    if init_value + ship_size - 1 > max_size:
        if init_value - ship_size + 1 > 0:
            return -1
        else:
            return 0
    else:
        return 1


def set_direction(random_position:Position) -> Tuple[str,int]:
    if random_position.row % 2:
        axis = "horizontal"
        st_value = random_position.column.value
    else:
        axis = "vertical"
        st_value = random_position.row
    return axis, st_value

def place_this_ship(ship:Ship, st_point:Position, enemyFleet:List[Ship]):
    # Take a direction: either vertical or horizontal:
    positions = []
    positions.append(st_point)

    axis, st_value = set_direction(st_point)
    factor = set_forward_rear(ship.size, st_value, 8)

    if factor:
        for i in range(1,ship.size):
            if axis == "horizontal":
                column = Letter(st_point.column.value + (i * factor))
                row = st_point.row
            else:
                column = st_point.column
                row = st_point.row + (i * factor)
            positions.append(Position(row=row,column=column))
    else:
        return False

    if not overlaps(positions,enemyFleet):
        # insert positions into the ship
        for p in positions:
            ship.positions.append(p)
        return True
    else:
        return False

def get_random_position_2():
    rows = 8
    lines = 8

    letter = Letter(random.randint(1, lines))
    number = random.randint(1, rows)
    position = Position(letter, number)

    return position

def initialize_enemyFleet():
    global enemyFleet

    enemyFleet = GameController.initialize_ships()

    for ship in enemyFleet:
        ship_strating_point = get_random_position_2()
        while not place_this_ship(ship,ship_strating_point, enemyFleet):
            ship_strating_point = get_random_position_2()


    #print(enemyFleet)

def check_position_input(msg: str):
    string = input(msg)
    assert len(string) == 2 and string[0].isalpha() and string[1:].isnumeric()
    return string


if __name__ == '__main__':
    main()
