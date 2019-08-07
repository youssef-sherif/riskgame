from HumanAgent import HumanAgent
from Game import Game
from PassiveAgent import PassiveAgent
from Board import Board
from Territory import Territory
from Color import Color

player = HumanAgent(Color.Blue)
agent_1 = PassiveAgent(Color.Blue)
agent_2 = PassiveAgent(Color.Red)

# game = Game.start_simulation_mode(agent_1, agent_2, 'Egypt')
game = Game.start_playing_mode(player, agent_2, 'Egypt')

player.turn(game, {1: 1})
game.board.display()

print(agent_2.color)
agent_2.turn(game)

game.board.display()
