from Color import Color
from HumanAgent import HumanAgent
from PassiveAgent import PassiveAgent
from AggressiveAgent import AggressiveAgent
from MiniMaxAgent import MiniMaxAgent
from NearlyPacifistAgent import NearlyPacifistAgent
from GreedyAgent import GreedyAgent
from AStarAgent import AStarAgent


class AgentFactory:

    @classmethod
    def create_agent(cls, agent_name, color):
        if agent_name == 'human':
            return HumanAgent(color)
        elif agent_name == 'passive':
            return PassiveAgent(color)
        elif agent_name == 'aggressive':
            return AggressiveAgent(color)
        elif agent_name == 'minimax':
            return MiniMaxAgent(color)
        elif agent_name == 'nearlypascifist':
            return NearlyPacifistAgent(color)
        elif agent_name == 'greedy':
            return GreedyAgent(color)
        elif agent_name == 'astar':
            return AStarAgent(color)
