from enum import Enum

class Color(Enum):
    CADET_BLUE = 1
    CHARTREUSE = 2
    ORANGE = 3
    RED = 4
    YELLOW = 5

class Letter(Enum):
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    F = 6
    G = 7
    H = 8

class Position(object):
    def __init__(self, column: Letter, row: int):
        self.column = column
        self.row = row
        self.is_shot = False

    def __eq__(self, other):
        return self.column == other.column and self.row == other.row

    def __hash__(self):
        return hash(f"{self.column}_{self.row}")

    def __str__(self):
        return f"{self.column.name}{self.row}"

    __repr__ = __str__

class Ship(object):
    def __init__(self, name: str, size: int, color: Color):
        self.name = name
        self.size = size
        self.color = color
        self.positions = []
        self.is_sunk = False

    def add_position(self, input: str):
        letter = Letter[input.upper()[:1]]
        number = int(input[1:])

        self.positions.append(Position(letter, number))

    def check_sunk(self):
        self.is_sunk = all(position.is_shot for position in self.positions)

    def __str__(self):
        return f"{self.color.name} {self.name} ({self.size}): {self.positions}"

    __repr__ = __str__
