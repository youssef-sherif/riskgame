from Territory import Territory
from Color import Color


class Board:

    def __init__(self, country_name: str, territory_count: int):
        self.country_name = country_name
        self.territory_count = territory_count

    @classmethod
    def init_egypt(cls):
        cls.territory_count = 27
        cls.map = dict()

        file = open("Egypt.txt")
        text = file.read().split("\n")
        for i in range(1,28):
            cls.map[i] = Territory()
            current_line = text[i-1].split()
            cls.map[i].set_neighbours(current_line[1:])

        return cls('Egypt', cls.territory_count)

    @classmethod
    def init_usa(cls):
        cls.territory_count = 50
        cls.map = dict()

        file = open("USA.txt")
        text = file.read().split("\n")
        for i in range(1, 51):
            cls.map[i] = Territory()
            current_line = text[i - 1].split()
            cls.map[i].set_neighbours(current_line[1:])

        return cls('USA', cls.territory_count)

    def update(self, territory_armies: {}, color):
        for item in territory_armies:
            self.map[item].color = color
            self.map[item].troops = territory_armies[item]

    def get_territories_with_color(self, color):
        j = 1
        territories = {}
        for i in range(1, self.territory_count):
            if self.map[i].color is color:
                territories[j] = self.map[i]
            j += 1

        return territories

    def display(self):

        for i in range(1, self.territory_count):
            print(self.map[i].color)
            print(self.map[i].troops)

        print('\n')


