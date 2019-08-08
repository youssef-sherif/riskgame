from Agent import Agent
from Color import Color


class PassiveAgent(Agent):

    def place_territories(self, board):
        territory = board.find_territory_with_fewest_armies(self.color)
        if board.map[territory].color == Color.Grey or board.map[territory].color == self.get_opponent_color():
            raise Exception('PassiveAgent can only place armies on own territories and cannot claim neutral territories')
        board.update(territory, self.available_armies_count, self.color)

