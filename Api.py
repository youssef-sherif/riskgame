from flask import Flask, request
from flask_cors import CORS, cross_origin
from Game import Game
from AgentFactory import AgentFactory
from Color import Color
import json


def json_response(payload, status=200):
    return json.dumps(payload), status, {'content-type': 'application/json'}


class Api:

    def __init__(self):
        self.app = Flask(__name__)
        self.app.add_url_rule('/territories/<territory>/place', 'place_armies', self.place_armies, methods=["POST"])
        self.app.add_url_rule('/territories/<attacked_territory>/attack', 'attack', self.attack, methods=["POST"])
        self.app.add_url_rule('/game', 'start_playing_game', self.start_playing_game, methods=["GET"])
        self.app.add_url_rule('/simulation', 'start_simulation_game', self.start_simulation_game, methods=["GET"])
        self.app.add_url_rule('/neighbours_to_blue', 'get_neighbours_to_blue', self.get_neighbours_to_blue, methods=["GET"])
        self.app.add_url_rule('/neighbours_to_red', 'get_neighbours_to_red', self.get_neighbours_to_red, methods=["GET"])
        self.app.add_url_rule('/blue-armies', 'receive_blue_armies', self.receive_blue_armies, methods=["GET"])
        self.app.add_url_rule('/red-armies', 'receive_red_armies', self.receive_red_armies, methods=["GET"])
        self.game = None

    @cross_origin(origin='http://localhost:3000')
    def start_playing_game(self):
        opponent_type = request.args.get('opponent_type')
        country = request.args.get('country')

        human_agent = AgentFactory.create_agent('human', Color.Blue)
        opponent_agent = AgentFactory.create_agent(opponent_type, Color.Red)

        self.game = Game.start_playing_mode(human_agent, opponent_agent, country)

        return json_response(self.game.board.to_json())

    @cross_origin(origin='http://localhost:3000')
    def start_simulation_game(self):
        agent1_type = request.args.get('agent1_type')
        agent2_type = request.args.get('agent2_type')
        country = request.args.get('country')

        agent1 = AgentFactory.create_agent(agent1_type, Color.Blue)
        agent2 = AgentFactory.create_agent(agent2_type, Color.Red)

        self.game = Game.start_simulation_mode(agent1, agent2, country)

        return json_response(self.game.board.to_json())

    @cross_origin(origin='http://localhost:3000')
    def get_neighbours_to_blue(self):
        blue_territories = self.game.board.find_territories_with_color(Color.Blue)
        neighbours_to_blue = list()
        for blue_territory in blue_territories.values():
            for neighbour in blue_territory.neighbours:
                if self.game.board.map[int(neighbour)].color is Color.Grey:
                    continue
                neighbours_to_blue.append(neighbour)

        return json_response(neighbours_to_blue)

    @cross_origin(origin='http://localhost:3000')
    def get_neighbours_to_red(self):
        red_territories = self.game.board.find_territories_with_color(Color.Red)
        neighbours_to_red = list()
        for red_territory in red_territories.values():
            for neighbour in red_territory.neighbours:
                if self.game.board.map[int(neighbour)].color is Color.Grey:
                    continue
                neighbours_to_red.append(neighbour)

        return json_response(neighbours_to_red)

    @cross_origin(origin='http://localhost:3000')
    def place_armies(self, territory):
        armies_count = int(request.get_json()['armies_count'])
        self.game.player.place_territories(self.game.board, int(territory), armies_count)
        json = {
            'available_armies': self.game.player.available_armies_count,
            'map': self.game.board.to_json()
        }
        return json_response(json)

    @cross_origin(origin='http://localhost:3000')
    def attack(self, attacked_territory):
        armies_count = int(request.get_json()['armies_count'])
        attacking_territory = int(request.get_json()['attacking_territory'])
        success = self.game.player.attack(self.game.board, int(attacking_territory), int(attacked_territory), armies_count)
        json = {
            'map': self.game.board.to_json(),
            'attack_successful': success
        }
        return json_response(json)

    @cross_origin(origin='http://localhost:3000')
    def receive_blue_armies(self):
        self.game.player.receive_armies(self.game.board)

        return json_response(self.game.player.available_armies_count)

    @cross_origin(origin='http://localhost:3000')
    def receive_red_armies(self):
        self.game.opponent_agent.receive_armies(self.game.board)

        return json_response(self.game.player.available_armies_count)


api = Api()
cors = CORS(api.app, resources={r"/*": {"origins": "*"}})
if __name__ == '__main__':
    api.app.run(debug=True)
