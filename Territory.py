
from Color import Color


class Territory:

    def __init__(self):
        self.color = Color.Grey
        self.troops = 0
        self.neighbours = list()
        return

    def set_neighbours(self,territory):
        self.neighbours.extend(territory)
