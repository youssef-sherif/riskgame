from Color import Color
from HumanAgent import HumanAgent
from PassiveAgent import PassiveAgent
from AggressiveAgent import AggressiveAgent
from MiniMaxAgent import MiniMaxAgent

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
