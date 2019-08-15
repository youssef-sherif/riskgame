from Agent import Agent
from State import State
import heapq


class AStarAgent(Agent):

    def make_decision(self, board):
        self.receive_armies(board)
        state = State(board, self.available_armies_count, 1)

        place_armies_result = self.a_star_place_armies(state)

        if place_armies_result is not None and place_armies_result.parent is not None:
            board.bulk_update(place_armies_result.parent.board)

        attack_result = self.a_star_attack(place_armies_result.parent)

        if attack_result is not None:
            board.bulk_update(attack_result.parent.board)

    def a_star_place_armies(self, state):
        heap_list = []
        heapq.heapify(heap_list)
        explored = list()
        cost = 0

        for child in self.get_place_armies_children(state):
            heuristic = self.evaluate_heuristic(state.board)
            child.state.distance = heuristic
            heap_list.insert(0, child)
            heapq.heapify(heap_list)

        while heap_list.__len__() is not 0:
            node = heap_list.pop()

            explored.append(node)

            if node.state.is_terminal(self.color):

                return node

            for child in self.get_place_armies_children(node.state):
                if child is not None:

                    if child in heap_list:
                        if child.state.distance < node.state.distance:
                            heap_list.remove(neighbour)
                            heapq.heapify(heap_list)

                    if child in explored:
                        if node.state.distance < child.distance:
                            explored.remove(child)

                    if child not in heap_list and child not in explored:
                        cost += 1
                        heuristic = self.evaluate_heuristic(child.state.board)
                        child.parent.distance = cost + heuristic
                        heap_list.insert(0, child)
                        heapq.heapify(heap_list)
                        child.parent = state

        return None

    def a_star_attack(self, state):
        heap_list = []
        heapq.heapify(heap_list)
        explored = list()
        cost = 0

        for child in self.get_attacking_children(state):
            heuristic = self.evaluate_heuristic(state.board)
            child.state.distance = heuristic
            heap_list.insert(0, child)
            heapq.heapify(heap_list)

        while heap_list.__len__() is not 0:
            node = heap_list.pop()

            explored.append(node)

            if node.state.is_terminal(self.color):
                return node

            for child in self.get_attacking_children(node.state):
                if child is not None:

                    if child in heap_list:
                        if child.state.distance < node.state.distance:
                            heap_list.remove(neighbour)
                            heapq.heapify(heap_list)

                    if child in explored:
                        if node.state.distance < child.distance:
                            explored.remove(child)

                    if child not in heap_list and child not in explored:
                        cost += 1
                        heuristic = self.evaluate_heuristic(child.state.board)
                        child.parent.distance = cost + heuristic
                        heap_list.insert(0, child)
                        heapq.heapify(heap_list)
                        child.parent = state

        return None
