from Agent import Agent
from Color import Color


class AggressiveAgent(Agent):

    def make_decision(self, board):
        self.receive_armies(board)
        self.place_territories(board)
        self.attack(board)

    def place_territories(self, board):
        territory = self.find_owned_territory_with_most_armies(board)
        board.update(territory, self.available_armies_count, self.color)

    def attack(self, board):
        try:
            attacking_territory = self.find_owned_territory_with_most_armies(board)
            attacked_territory = self.find_weakest_opposite_color_neighbour_to(board, attacking_territory)
            armies_count = board.map[attacking_territory].troops - 1

            board.map[attacked_territory].troops -= armies_count
            board.map[attacking_territory].troops -= armies_count

            if board.map[attacked_territory].troops <= 0:
                board.map[attacked_territory].troops = armies_count
                board.map[attacked_territory].color = board.map[attacking_territory].color

                return True
        except Exception as e:
            print(e)
            return False

    def find_weakest_opposite_color_neighbour_to(self, board, attacking_territory):

        can_attack = False
        opposite_color_neighbours = {}

        for neighbour_territory in board.map[attacking_territory].neighbour_territories:
            if neighbour_territory.color == self.get_opponent_color() \
                    and board.map[attacking_territory].has_neighbour(neighbour_territory):
                can_attack = True
                opposite_color_neighbours[neighbour_territory.id] = neighbour_territory

        if not can_attack:
            raise Exception("cannot attack")

        print(opposite_color_neighbours)

        return min(opposite_color_neighbours, key=lambda k: opposite_color_neighbours[k])

    def find_owned_territory_with_most_armies(self, board) -> int:
        territories = board.find_territories_with_color(self.color)

        return max(territories, key=lambda k: territories[k])


