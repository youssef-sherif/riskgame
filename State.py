class State():
    def __init__(self, board, armies, depth):
        self.board = board
        self.armies = armies
        self.depth = depth

    def is_terminal(self, opponent_color):
        if self.depth == 0:
            return True
        for territory in self.board.map.values():
            if territory.color == opponent_color:
                return False
        return True
