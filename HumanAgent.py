from Agent import Agent
from Color import Color


class HumanAgent(Agent):

    def place_territories(self, board, territory, armies_count):
        if board.map[territory].color == Color.Red:
            raise Exception('You can only place armies on owned or neutral territories')
        self.available_armies_count -= armies_count
        board.update(territory, armies_count, self.color)

    def attack(self, board, attacking_territory, attacked_territory, armies_count):
        board.map[attacked_territory].troops -= armies_count
        board.map[attacking_territory].troops -= armies_count

        if board.map[attacked_territory].troops <= 0:
            board.map[attacked_territory].troops = 1
            board.map[attacked_territory].color = board.map[attacking_territory].color

            return True

        return False
