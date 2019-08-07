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
        self.app.add_url_rule('/game', 'start_playing_game', self.start_playing_game, methods=["GET"])
        self.app.add_url_rule('/simulation', 'start_simulation_game', self.start_simulation_game, methods=["GET"])
        self.app.add_url_rule('/<id>/blue-neighbours', 'get_blue_neighbours_for_id', self.get_blue_neighbours_for_id, methods=["GET"])
        self.app.add_url_rule('/<id>/red-neighbours', 'get_red_neighbours_for_id', self.get_red_neighbours_for_id, methods=["GET"])
        self.app.add_url_rule('/neighbours_to_blue', 'get_neighbours_to_blue', self.get_neighbours_to_blue, methods=["GET"])
        self.app.add_url_rule('/neighbours_to_red', 'get_neighbours_to_red', self.get_neighbours_to_red, methods=["GET"])
        self.app.add_url_rule('/armies', 'place_armies', self.place_armies, methods=["POST"])
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
    def get_blue_neighbours_for_id(self, id):
        territories = self.game.board.find_territories_with_color(Color.Blue)
        territory_locations = list()
        print(self.game.board.map[int(id)].neighbours)
        for i in territories.keys():
            if str(i) in self.game.board.map[int(id)].neighbours:
                territory_locations.append(i)

        return json_response(territory_locations)

    @cross_origin(origin='http://localhost:3000')
    def get_red_neighbours_for_id(self, id):
        territories = self.game.board.find_territories_with_color(Color.Red)
        territory_locations = list()
        print(self.game.board.map[int(id)].neighbours)
        for i in territories.keys():
            if str(i) in self.game.board.map[int(id)].neighbours:
                territory_locations.append(i)

        return json_response(territory_locations)

    @cross_origin(origin='http://localhost:3000')
    def get_neighbours_to_blue(self):
        blue_territories = self.game.board.find_territories_with_color(Color.Blue)
        neighbours_to_blue = list()
        for blue_territory in blue_territories.values():
            for neighbour in blue_territory.neighbours:
                neighbours_to_blue  .append(neighbour)

        return json_response(neighbours_to_blue)

    @cross_origin(origin='http://localhost:3000')
    def get_neighbours_to_red(self):
        red_territories = self.game.board.find_territories_with_color(Color.Red)
        neighbours_to_red = list()
        for red_territory in red_territories.values():
            for neighbour in red_territory.neighbours:
                neighbours_to_red.append(neighbour)

        return json_response(neighbours_to_red)

    @cross_origin(origin='http://localhost:3000')
    def place_armies(self):
        return json_response()


api = Api()
cors = CORS(api.app, resources={r"/*": {"origins": "*"}})
if __name__ == '__main__':
    api.app.run(debug=True)
