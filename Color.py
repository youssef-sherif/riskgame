from enum import Enum


class Color(Enum):
    Blue = 'blue'
    Red = 'red'
    Grey = 'grey'

    @classmethod
    def to_str(cls, color):
        if color == cls.Blue:
            return 'blue'
        elif color == cls.Red:
            return 'red'
        else:
            return 'grey'
