from Agent import Agent
from Color import Color


class PassiveAgent(Agent):

    def turn(self, game):
        self.receive_armies(game.board)
        territory_number = game.board.find_territory_with_fewest_armies(self.color)
        territory_armies = {territory_number: int(self.available_armies_count)}
        self.place_territories(game.board, territory_armies)

        game.alternate_turn()

    def place_territories(self, board, territory_armies: {}):
        for item in territory_armies:
            if board.map[item].color == Color.Grey or board.map[item].color == self.get_opponent_color():
                raise Exception('PassiveAgent can only place armies on own territories and cannot claim neutral territories')
        board.update(territory_armies, self.color)

