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
        attacked_territory = self.find_weakest_neighbour_to(board, attacking_territory)

        armies_count = board.map[attacking_territory].troops - 1

        board.map[attacked_territory].troops -= armies_count
        board.map[attacking_territory].troops -= armies_count

        if board.map[attacked_territory].troops <= 0:
            board.map[attacked_territory].troops = armies_count
            board.map[attacked_territory].color = board.map[attacking_territory].color

            return True

        return False

    def find_weakest_neighbour_to(self, board, attacking_territory) -> int:
        print(board.map[attacking_territory].neighbours[0])
        territory_number = int(board.map[attacking_territory].neighbours[0])
        for i in board.map[attacking_territory].neighbours:
            if board.map[int(i)].color == self.get_opponent_color():
                if board.map[int(i)].troops < board.map[territory_number].troops:
                    territory_number = int(i)

        return territory_number

    def find_territory_with_most_armies(self, board) -> int:
        territory_number = 1
        for i in range(1, board.territory_count + 1):
            if board.map[i].color == self.color:
                if board.map[i].troops >= board.map[territory_number].troops:
                    territory_number = i

        return territory_number



