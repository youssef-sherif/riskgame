class Board:

    def __init__(self, country_name: str, territory_count: int):
        self.country_name = country_name
        self.territory_count = territory_count

    @classmethod
    def init_egypt(cls):
        cls.territory_count = 27
        return cls('Egypt', cls.territory_count)

    @classmethod
    def init_usa(cls):
        cls.territory_count = 50
        return cls('USA', cls.territory_count)
