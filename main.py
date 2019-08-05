from Game import Game
from Player import Player
from Agent import Agent
from Board import Board
from Territory import Territory
# import tkinter as tk

# player = Player('blue')
# agent_1 = Agent('blue')
# agent_2 = Agent('red')
#
# game = Game.start_simulation_mode(agent_1, agent_2, 'Egypt')
# # game = Game.start_playing_mode(player, agent_2, 'USA')
#
# player.turn({
#     1: 1,
#     2: 2,
#     3: 1
# })
#
# print(game.board.country_name)
#
#
board = Board.init_usa()
print(board.map)
# print(board.map[1])
# x = open("egypt.txt", "r")
# s = x.read()
# print(s[0])
# root = tk.Tk()
#
#
# def hello_call_back():
#     print('hello')
#
#
# w = tk.Button(root, text='click me', command=hello_call_back)
# w.pack()
# tk.mainloop()