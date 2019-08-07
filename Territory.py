
from Color import Color


class Territory:

    def __init__(self, id):
        self.color = Color.Grey
        self.troops = 0
        self.neighbours = list()
        self.id = id
        return

    def set_neighbours(self,territory):
        self.neighbours.extend(territory)

    def to_json(self):
        return {
            'id': self.id,
            'color': str(self.color),
            'troops': self.troops
        }
