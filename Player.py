class Player:

    def __init__(self, color: str):
        self.armies_count = 20
        self.color = color

    def turn(self, territory_armies: {}):
        return