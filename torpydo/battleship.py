import random
import os
import colorama
import platform

from colorama import Fore, Back, Style
from torpydo.ship import Color, Letter, Position, Ship
from torpydo.game_controller import GameController
from torpydo.telemetryclient import TelemetryClient

import time
print("Starting")

myFleet = []
enemyFleet = []
BAD_POSITION_INPUT_MSG = "The position is invalid. Please try enter a letter and a number like: 'A1'"


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

        start_colouring(right_colour(is_hit))
        print("Yeah ! Nice hit !" if is_hit else "Miss")
        TelemetryClient.trackEvent('Player_ShootPosition', {'custom_dimensions': {'Position': str(position), 'IsHit': is_hit}})
        if is_fleet_down(enemyFleet):
            print("Congratulations! You are the winner \o/")
            break

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

        print("\n\nComputer is thinking...")
        time.sleep(3)
        # Computer
        position = get_random_position()
        is_hit = GameController.check_is_hit(myFleet, position)
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
            print("Sorry, you lost...")
            break

    print("Thank you for playing!")

def is_fleet_down(fleet):
    return all(ship.is_sunk for ship in fleet)

def parse_position(input: str):
    letter = Letter[input.upper()[:1]]
    number = int(input[1:])

    return Position(letter, number)

def get_random_position():
    rows = 8
    lines = 8

    letter = Letter(random.randint(1, lines))
    number = random.randint(1, rows)
    position = Position(letter, number)

    return position

def initialize_game():
    initialize_myFleet()

    initialize_enemyFleet()

def initialize_myFleet():
    global myFleet

    myFleet = GameController.initialize_ships()

    quick_and_dirty = True
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

def initialize_enemyFleet():
    global enemyFleet

    enemyFleet = GameController.initialize_ships()

    enemyFleet[0].positions.append(Position(Letter.B, 4))
    enemyFleet[0].positions.append(Position(Letter.B, 5))
    enemyFleet[0].positions.append(Position(Letter.B, 6))
    enemyFleet[0].positions.append(Position(Letter.B, 7))
    enemyFleet[0].positions.append(Position(Letter.B, 8))

    enemyFleet[1].positions.append(Position(Letter.E, 6))
    enemyFleet[1].positions.append(Position(Letter.E, 7))
    enemyFleet[1].positions.append(Position(Letter.E, 8))
    enemyFleet[1].positions.append(Position(Letter.E, 9))

    enemyFleet[2].positions.append(Position(Letter.A, 3))
    enemyFleet[2].positions.append(Position(Letter.B, 3))
    enemyFleet[2].positions.append(Position(Letter.C, 3))

    enemyFleet[3].positions.append(Position(Letter.F, 8))
    enemyFleet[3].positions.append(Position(Letter.G, 8))
    enemyFleet[3].positions.append(Position(Letter.H, 8))

    enemyFleet[4].positions.append(Position(Letter.C, 5))
    enemyFleet[4].positions.append(Position(Letter.C, 6))

def check_position_input(msg: str):
    string = input(msg)
    assert len(string) == 2 and string[0].isalpha() and string[1:].isnumeric()
    return string


if __name__ == '__main__':
    main()
