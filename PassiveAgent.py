from Agent import Agent
from Color import Color


class PassiveAgent(Agent):

    def place_territories(self, board, territory, armies_count):
        if board.map[territory].color == Color.Grey or board.map[territory].color == self.get_opponent_color():
            raise Exception('PassiveAgent can only place armies on own territories and cannot claim neutral territories')
        self.available_armies_count -= armies_count
        board.update(territory, armies_count, self.color)

