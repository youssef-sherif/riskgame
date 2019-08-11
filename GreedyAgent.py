from Agent import Agent
from Color import Color
from State import State


class GreedyAgent(Agent):

    def make_decision(self, board):
        self.receive_armies(board)
        state = State(board, self.available_armies_count, 1)
        children = self.get_children_states(state)
        min_heuristic = 999999
        for child in children:
            new_heuristic = self.evaluate_heuristic(board)
            if new_heuristic < min_heuristic:
                min_heuristic = new_heuristic
                board.bulk_update(child.parent.board)
