from Color import Color
from Board import Board

#
#  This is the parent class that contains methods available to all agents
#


class Agent:

    def __init__(self, color):
        self.armies_count = 20
        self.color = color

    def receive_armies(self, board):
        territories = board.get_territories_with_color(self.color)
        armies_to_receive = sum(territories) / 3
        if armies_to_receive < 3:
            self.armies_count = 3
        else:
            self.armies_count = armies_to_receive

    def first_play(self,  game, territory_armies: {}):
        self.place_territories(game.board, territory_armies)

        game.alternate_turn()

    def turn(self, game, territory_armies: {}):
        self.receive_armies(game.board)
        self.place_territories(game.board, territory_armies)

        game.alternate_turn()

    def place_territories(self, board, territory_armies: {}):
        for item in territory_armies:
            if board.map[item].color is not Color.Grey:
                raise Exception('You can only place armies on neutral territories')
        board.update(territory_armies, self.color)

