from Color import Color
from HumanAgent import HumanAgent
from PassiveAgent import PassiveAgent


class AgentFactory:

    @classmethod
    def create_agent(cls, agent_name, color):
        if agent_name == 'human':
            return HumanAgent(color)
        elif agent_name == 'passive':
            return PassiveAgent(color)
