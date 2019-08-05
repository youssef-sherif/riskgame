from Player import Player
from Agent import Agent
from Board import Board
from Territory import Territory


class Game:

    # mode = 0 -> simulation, mode = 1 -> playing
    mode = 0

    def __init__(self, mode: int):
        self.mode = mode
        self.turn = 'blue'
        return

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

        return cls(int(0))

    @classmethod
    def start_playing_mode(cls, player: Player, opponent_agent: Agent, country_name: str):
        cls.player = player
        cls.opponent_agent = opponent_agent

        if country_name == 'Egypt':
            cls.board = Board.init_egypt()
        elif country_name == 'USA':
            cls.board = Board.init_usa()
        else:
            print('not supported yet')

        return cls(int(1))