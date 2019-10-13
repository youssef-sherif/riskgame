from Agent import Agent
from Color import Color
from State import State


class GreedyAgent(Agent):

    def make_decision(self, board):
        self.receive_armies(board)

        state = State(board, self.available_armies_count, 1)
        place_armies_result = None

        place_armies_children = self.get_place_armies_children(state)
        min_heuristic = 999999
        for child in place_armies_children:
            new_heuristic = self.evaluate_heuristic(board)
            if new_heuristic < min_heuristic:
                min_heuristic = new_heuristic
                place_armies_result = child

        attacking_children_states = self.get_attacking_children(place_armies_result.parent)
        attacking_result = None

        min_heuristic = 999999
        for child in attacking_children_states:
            new_heuristic = self.evaluate_heuristic(board)
            if new_heuristic < min_heuristic:
                min_heuristic = new_heuristic
                attacking_result = child

        if attacking_result is not None:
            board.bulk_update(attacking_result.parent.board)
