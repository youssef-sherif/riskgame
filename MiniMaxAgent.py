from Agent import Agent
from Color import Color
from State import State


class MiniMaxAgent(Agent):

    def make_decision(self, board):
        self.receive_armies(board)
        state = State(board, self.available_armies_count, 1)

        place_armies_result, _ = self.maximize_place_armies(state, -999999, 999999)

        attack_result, _ = self.maximize_attack(place_armies_result.parent, -999999, 999999)

        if attack_result is not None:
            board.bulk_update(attack_result.parent.board)

    def maximize_place_armies(self, state, alpha, beta):
        max_child, max_heuristic = (None, -999999)

        if state.is_terminal(self.get_opponent_color()):
            return max_child, self.evaluate_heuristic(state.board)

        for child_node in self.get_place_armies_children(state):
            self.receive_armies(child_node.state.board)
            _, new_heuristic = self.minimize_place_armies(child_node.state, alpha, beta)

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

    def minimize_place_armies(self, state, alpha, beta):
        min_child, min_heuristic = (None, 999999)

        if state.is_terminal(self.get_opponent_color()):
            return min_child, self.evaluate_heuristic(state.board)

        for child_node in self.get_place_armies_children(state):
            self.receive_armies(child_node.state.board)
            _, new_heuristic = self.maximize_place_armies(child_node.state, alpha, beta)

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

    def maximize_attack(self, state, alpha, beta):
        max_child, max_heuristic = (None, -999999)

        if state.is_terminal(self.get_opponent_color()):
            return max_child, self.evaluate_heuristic(state.board)

        for child_node in self.get_attacking_children(state):
            self.receive_armies(child_node.state.board)
            _, new_heuristic = self.minimize_attack(child_node.state, alpha, beta)

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

    def minimize_attack(self, state, alpha, beta):
        min_child, min_heuristic = (None, 999999)

        if state.is_terminal(self.get_opponent_color()):
            return min_child, self.evaluate_heuristic(state.board)

        for child_node in self.get_attacking_children(state):
            self.receive_armies(child_node.state.board)
            _, new_heuristic = self.maximize_attack(child_node.state, alpha, beta)

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
