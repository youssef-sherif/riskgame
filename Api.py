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
        self.app.add_url_rule('/game', 'start_playing_game', self.start_playing_game)
        self.app.add_url_rule('/simulation', 'start_simulation_game', self.start_simulation_game)
        self.CORS = CORS(self.app, resources={r"/*": {"origins": "*"}})
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


api = Api()
if __name__ == '__main__':
    api.app.run(debug=True)
