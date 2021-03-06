from Agent import Agent
from Color import Color


class NearlyPacifistAgent(Agent):

    def make_decision(self, board):
        self.receive_armies(board)
        self.place_territories(board)
        try:
            attacking_territory = self.find_owned_territory_with_most_armies(board)
            attacked_territory = self.find_weakest_opposite_color_neighbour_to(board, attacking_territory)
            if board.map[attacking_territory].troops > board.map[attacked_territory].troops:
                armies_count = board.map[attacked_territory].troops
                self.attack(board.map[attacking_territory], board.map[attacked_territory], armies_count)
        except Exception as e:
            print(e)

    def place_territories(self, board):
        territory = self.find_owned_territory_with_fewest_armies(board)
        board.update(territory, self.available_armies_count, self.color)
