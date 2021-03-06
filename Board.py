from Territory import Territory
from Color import Color
import random


class Board:

    def __init__(self, country_name: str, territory_count: int):
        self.country_name = country_name
        self.territory_count = territory_count

    @classmethod
    def init_egypt(cls):
        cls.territory_count = 27
        cls.map = dict()

        file = open("maps/egypt/Egypt.txt")
        coordinates_file = open("maps/egypt/Egypt_Coordinates.txt")
        text = file.read().split("\n")
        coordinates_text = coordinates_file.read().split("\n")
        for i in range(1, 28):
            x = coordinates_text[i-1].split()[0]
            y = coordinates_text[i - 1].split()[1]
            cls.map[i] = Territory(i, x, y)
            current_line = text[i-1].split()
            cls.map[i].set_neighbours(current_line[1:])

        for i in range(1, 28):
            for neighbour in cls.map[i].neighbours:
                cls.map[i].add_neighbour_territory(cls.map[int(neighbour)])

        return cls('Egypt', cls.territory_count)

    @classmethod
    def init_usa(cls):
        cls.territory_count = 50
        cls.map = dict()

        file = open("maps/usa/USA.txt")
        coordinates_file = open("maps/usa/USA_Coordinates.txt")
        text = file.read().split("\n")
        coordinates_text = coordinates_file.read().split("\n")
        for i in range(1, 51):
            x = coordinates_text[i-1].split()[0]
            y = coordinates_text[i - 1].split()[1]
            cls.map[i] = Territory(i, x, y)
            current_line = text[i-1].split()
            cls.map[i].set_neighbours(current_line[1:])

        for i in range(1, 51):
            for neighbour in cls.map[i].neighbours:
                cls.map[i].add_neighbour_territory(cls.map[int(neighbour)])

        return cls('USA', cls.territory_count)

    def update(self, territory, armies_count, color):
        self.map[territory].color = color
        self.map[territory].troops += armies_count

    def bulk_update(self, new):
        i = 1
        for territory in self.map.values():
            territory.troops = new.map[i].troops
            territory.color = new.map[i].color
            i += 1

    def set_starting_armies(self, color):
        army_size = 20
        while army_size > 0:
            i = random.randint(1, self.territory_count+1)
            if self.map[i].color is Color.Grey:
                x = random.randint(1, army_size+1)
                self.map[i].color = color
                self.map[i].troops = x
                army_size -= x

    def find_territories_with_color(self, color) -> {}:
        j = 1
        territories = {}
        for i in range(1, self.territory_count+1):
            if self.map[i].color == color:
                territories[j] = self.map[i]
            j += 1

        return territories

    def count_territories_with_color(self, color) -> int:
        count = 0
        for i in range(1, self.territory_count+1):
            if self.map[i].color == color:
                count += 1

        return count

    def to_json(self):
        arr = [{} for i in range(self.territory_count)]
        for i in range(0, self.territory_count):
            arr[i] = (self.map[i+1].to_json())

        return arr

    def display(self):

        for i in range(1, self.territory_count+1):
            print(str(i) + " " + str(self.map[i].troops) + " " + str(self.map[i].color))

        print('\n')


