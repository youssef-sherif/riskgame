
from Color import Color


class Territory:

    def __init__(self):
        self.color = Color(3)
        self.troops = 0
        self.neighbours = list()
        return

    def set_neighbours(self,territory):
        self.neighbours.extend(territory)


    # def in_egypt(cls):
    #     return
    #
    # @classmethod
    # def in_usa(cls):
    #     return
