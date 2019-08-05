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
game.board.display()

player.first_play(game, {1: 19, 2: 1})
game.board.display()

agent_2.first_play(game, {3: 1, 4: 19})
game.board.display()

player.turn(game, {5: 15, 6: 5})
game.board.display()

agent_2.turn(game, {7: 10, 8: 10})
game.board.display()
