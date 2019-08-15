class Node:

    def __init__(self, state, parent):
        self.state = state
        self.parent = parent

    def __lt__(self, node):
        return self.state.distance < node.state.distance
