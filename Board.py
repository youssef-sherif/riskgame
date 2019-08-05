from Territory import Territory
class Board:

    def __init__(self, country_name: str, territory_count: int):
        self.country_name = country_name
        self.territory_count = territory_count

    @classmethod
    def init_egypt(cls):
        cls.territory_count = 27
        cls.map = dict()
        file = open("EGYPT.txt")
        text = file.read().split("\n")
        for i in range(1,28):
            cls.map[i] = Territory()
            currentLine = text[i-1].split()
            cls.map[i].set_neighbours(currentLine[1:])
            print(cls.map[i].neighbours)

        print(cls.map)
        return cls('Egypt', cls.territory_count)

    @classmethod
    def init_usa(cls):
        cls.territory_count = 50
        cls.map = dict()
        file = open("USA.txt")
        text = file.read().split("\n")
        for i in range(1, 51):
            cls.map[i] = Territory()
            currentLine = text[i - 1].split()
            cls.map[i].set_neighbours(currentLine[1:])
            print(cls.map[i].neighbours)
        return cls('USA', cls.territory_count)
