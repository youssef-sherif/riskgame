from HumanAgent import HumanAgent
from Agent import Agent
from Board import Board
from Territory import Territory
from Color import Color
import numpy as np


class Game:

    # mode = 0 -> simulation, mode = 1 -> playing
    mode = 0

    def __init__(self):
        self.turn = Color.Blue
        self.board.set_starting_armies(Color.Blue)
        self.board.set_starting_armies(Color.Red)
        self.status = 'blue playing'
        self.winner = None

    @classmethod
    def start_simulation_mode(cls, agent_1: Agent, agent_2: Agent, country_name: str):
        cls.agent_1 = agent_1
        cls.agent_2 = agent_2

        if country_name == 'Egypt':
            cls.board = Board.init_egypt()
        elif country_name == 'USA':
            cls.board = Board.init_usa()

        else:
            print('not supported yet')

        cls.mode = 0

        return cls()

    @classmethod
    def start_playing_mode(cls, player: HumanAgent, opponent_agent: Agent, country_name: str):
        cls.player = player
        cls.opponent_agent = opponent_agent

        if country_name == 'Egypt':
            cls.board = Board.init_egypt()
        elif country_name == 'USA':
            cls.board = Board.init_usa()
        else:
            print('not supported yet')

        cls.mode = 1

        return cls()

    def alternate_turn(self):
        if self.turn is Color.Blue:
            self.turn = Color.Red
            self.status = 'red playing'
        else:
            self.turn = Color.Blue
            self.status = 'blue playing'

    def check_win_condition(self):
        blue_territories = self.board.find_territories_with_color(Color.Blue)
        red_territories = self.board.find_territories_with_color(Color.Red)
        if not blue_territories:
            self.winner = Color.to_str(Color.Red)
            raise Exception(Color.to_str(Color.Red) + ' won')
        if not red_territories:
            self.winner = Color.to_str(Color.Blue)
            raise Exception(Color.to_str(Color.Blue) + ' won')

