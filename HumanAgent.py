from Agent import Agent
from Color import Color


class HumanAgent(Agent):

    def place_territories(self, board, territory, armies_count):
        if board.map[territory].color == Color.Red:
            raise Exception('You can only place armies on owned or neutral territories')
        self.available_armies_count -= armies_count
        board.update(territory, armies_count, self.color)
