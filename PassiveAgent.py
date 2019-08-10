from Agent import Agent
from Color import Color


class PassiveAgent(Agent):

    def make_decision(self, board):
        self.receive_armies(board)
        self.place_territories(board)

    def place_territories(self, board):
        territory = self.find_owned_territory_with_fewest_armies(board)
        board.update(territory, self.available_armies_count, self.color)

    def find_owned_territory_with_fewest_armies(self, board) -> int:
        territories = board.find_territories_with_color(self.color)

        return min(territories, key=lambda k: territories[k])
