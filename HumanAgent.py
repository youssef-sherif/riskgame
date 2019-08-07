from Agent import Agent
from Color import Color


class HumanAgent(Agent):

    def turn(self, game, territory_armies: {}):
        self.receive_armies(game.board)
        self.place_territories(game.board, territory_armies)
        self.attack(game.board)

        game.alternate_turn()

    def place_territories(self, board, territory_armies: {}):
        for item in territory_armies:
            if board.map[item].color == Color.Blue or board.map[item].color == Color.Red:
                raise Exception('You can only place armies on neutral territories')
        board.update(territory_armies, self.color)

    def attack(self, board):
        return
