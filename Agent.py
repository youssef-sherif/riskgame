from Color import Color
from Board import Board

#
#  This is the parent class that contains methods available to all agents
#


class Agent:

    def __init__(self, color):
        self.available_armies_count = 20
        self.color = color

    def receive_armies(self, board):
        territories_count = board.find_territories_with_color(self.color)
        armies_to_receive = sum(territories_count) / 3
        if armies_to_receive < 3:
            self.available_armies_count = 3
        else:
            self.available_armies_count = int(armies_to_receive)

    def make_decision(self, board):
        return

    def get_opponent_color(self):
        if self.color == Color.Blue:
            return Color.Red
        elif self.color == Color.Red:
            return Color.Blue
        else:
            return Color.Grey
