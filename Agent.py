from Color import Color
from Board import Board
from Node import Node
from copy import deepcopy
from State import State

#
#  This is the parent class that contains methods available to all agents
#


class Agent:

    def __init__(self, color):
        self.available_armies_count = 20
        self.color = color

    def receive_armies(self, board):
        territories_count = board.find_territories_with_color(self.color)
        armies_to_receive = sum(territories_count) / 3
        if armies_to_receive < 3:
            self.available_armies_count = 3
        else:
            self.available_armies_count = int(armies_to_receive)

    def make_decision(self, board):
        return

    def attack(self, attacking_territory, attacked_territory, armies_count):
        attacked_territory.troops -= armies_count
        attacking_territory.troops -= armies_count

        if attacked_territory.troops <= 0:
            attacked_territory.troops = 1
            attacked_territory.color = attacking_territory.color

            return True

        return False

    def get_opponent_color(self):
        if self.color == Color.Blue:
            return Color.Red
        elif self.color == Color.Red:
            return Color.Blue
        else:
            return Color.Grey

    def evaluate_heuristic(self, board):
        opponent_territories_count = board.count_territories_with_color(self.get_opponent_color())
        my_territories_count = board.count_territories_with_color(self.color)
        return opponent_territories_count - my_territories_count

    def get_children_states(self, state):
        place_armies_states = list()
        i = 1
        for territory in state.board.map.values():
            if territory.color == self.color:  # We can place armies on this territory
                copied_state = deepcopy(state)
                copied_state.board.map[i].troops += state.armies
                child_state = State(copied_state.board, copied_state.board.map[i].troops, copied_state.depth-1)
                place_armies_states.append(child_state)
            i += 1

        attacking_states = list()  # states generated after attack
        i = 1
        for territory in state.board.map.values():
            if territory.color == self.color:
                j = 0
                for neighbour in territory.neighbour_territories:     # Can only attack neighbours
                    if neighbour.color == self.get_opponent_color():  # We can attack this territory
                        if neighbour.troops < territory.troops:       # Attack only if success is guaranteed
                            copied_state = deepcopy(state)
                            copied_state.board.map[i].neighbour_territories[j].troops = copied_state.board.map[i].troops - 1
                            copied_state.board.map[i].troops = 1
                            copied_state.board.map[i].neighbour_territories[j].color = self.color

                            child_state = State(copied_state.board, copied_state.board.map[i].troops, 0)
                            node = Node(child_state, state)

                            attacking_states.append(node)
                    j += 1
            i += 1

        return attacking_states

