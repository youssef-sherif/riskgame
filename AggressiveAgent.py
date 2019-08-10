from Agent import Agent
from Color import Color


class AggressiveAgent(Agent):

    def make_decision(self, board):
        self.receive_armies(board)
        self.place_territories(board)
        self.attack(board)

    def place_territories(self, board):
        territory = self.find_territory_with_most_armies(board)
        board.update(territory, self.available_armies_count, self.color)

    def attack(self, board):
        attacking_territory = self.find_territory_with_most_armies(board)
        try:
            attacked_territory = self.find_weakest_opposite_color_neighbour_to(board, attacking_territory)
        except Exception as e:
            print(e)
            return False

        armies_count = board.map[attacking_territory].troops - 1

        board.map[attacked_territory].troops -= armies_count
        board.map[attacking_territory].troops -= armies_count

        if board.map[attacked_territory].troops <= 0:
            board.map[attacked_territory].troops = armies_count
            board.map[attacked_territory].color = board.map[attacking_territory].color

            return True

        return False

    def find_weakest_opposite_color_neighbour_to(self, board, attacking_territory) -> int:
        territory_number = int(board.map[attacking_territory].neighbours[0])
        has_opposite_color_neighbour = False
        for i in board.map[attacking_territory].neighbours:
            if board.map[int(i)].color == self.get_opponent_color():
                has_opposite_color_neighbour = True
                if board.map[int(i)].troops < board.map[territory_number].troops:
                    territory_number = int(i)

        if not has_opposite_color_neighbour:
            raise Exception("cannot attack as no opposite color neighbours found")
        return territory_number

    def find_territory_with_most_armies(self, board) -> int:
        territories = board.find_territories_with_color(self.color)

        return max(territories, key=lambda k: territories[k])



