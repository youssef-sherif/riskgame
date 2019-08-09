from Agent import Agent
from Color import Color


class PassiveAgent(Agent):

    def make_decision(self, board):
        self.receive_armies(board)
        self.place_territories(board)

    def place_territories(self, board):
        territory = self.find_territory_with_fewest_armies(board)
        board.update(territory, self.available_armies_count, self.color)

    def find_territory_with_fewest_armies(self, board) -> int:
        territory_number = 1
        for i in range(1, board.territory_count + 1):
            if board.map[i].color == self.color:
                if board.map[i].troops <= board.map[territory_number].troops:
                    territory_number = i

        return territory_number
