
from Color import Color


class Territory:

    def __init__(self, id, x, y):
        self.color = Color.Grey
        self.troops = 0
        self.neighbours = list()
        self.id = id
        self.x = x
        self.y = y

    def set_neighbours(self,territory):
        self.neighbours.extend(territory)

    def to_json(self):
        return {
            'id': self.id,
            'color': Color.to_str(self.color),
            'troops': self.troops,
            'x': self.x,
            'y': self.y
        }
