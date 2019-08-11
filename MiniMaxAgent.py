from Agent import Agent
from Color import Color
from State import State


class MiniMaxAgent(Agent):

    def make_decision(self, board):
        self.receive_armies(board)
        state = State(board, self.available_armies_count, 1)

        result, _ = self.maximize(state, -999999, 999999)
        if result is not None:
            board.bulk_update(result.parent.board)

    def maximize(self, state, alpha, beta):
        max_child, max_heuristic = (None, -999999)

        if state.is_terminal(self.get_opponent_color()):
            return max_child, self.evaluate_heuristic(state.board)

        for child_node in self.get_children_states(state):
            self.receive_armies(child_node.state.board)
            _, new_heuristic = self.minimize(child_node.state, alpha, beta)

            # Update heuristic
            if new_heuristic > max_heuristic:
                max_child, max_heuristic = child_node, new_heuristic

            # Update alpha
            if new_heuristic > alpha:
                alpha = new_heuristic

            # Break from loop to prune if no chance for better results
            if alpha >= beta:
                break

        return max_child, max_heuristic #return max child

    def minimize(self, state, alpha, beta):
        min_child, min_heuristic = (None, 999999)

        if state.is_terminal(self.get_opponent_color()):
            return min_child, self.evaluate_heuristic(state.board)

        for child_node in self.get_children_states(state):
            self.receive_armies(child_node.state.board)
            _, new_heuristic = self.maximize(child_node.state, alpha, beta)

            # Update heuristic
            if new_heuristic < min_heuristic:
                min_child, min_heuristic = child_node, new_heuristic

            # Update alpha
            if new_heuristic < beta:
                beta = new_heuristic

            # Break from loop to prune if no chance for better results
            if alpha >= beta:
                break

        return min_child, min_heuristic
