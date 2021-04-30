class Players:
    __players = []

    def new_player(self):
        self.__players = Player()

    @classmethod
    def getPlayers(cls) -> list:
        return cls.__players


class Player(object):
    __player = {}

    def __init__(self, **kwargs):
        players_data = ["circles", "color", "points", "name", "marbles"]
        for k in kwargs.keys():
            if k not in players_data:
                del kwargs[k]

        self.__player = kwargs

    @property
    def circles(self) -> list:
        return self.__player["circles"] if "circles" in self.__player else []

    @circles.setter
    def circles(self, circles, remove=False):
        if "circles" not in self.__player:
            self.__player["circles"] = []
            remove = False
        if remove:
            self.__player["circles"].remove(circles)
        if circles != []:
            self.__player["circles"].append(circles)

    @property
    def marbles(self) -> list:
        return self.__player["marbles"] if "marbles" in self.__player else []

    @marbles.setter
    def marbles(self, marbles, remove=False):
        if "marbles" not in self.__player:
            self.__player["marbles"] = []
            remove = False
        if remove:
            self.__player["marbles"].remove(marbles)
        if marbles != []:
            self.__player["marbles"].append(marbles)

    @property
    def color(self) -> str:
        return self.__player["color"] if "color" in self.__player else "red"

    @color.setter
    def color(self, color):
        self.__player["color"] = color

    @property
    def points(self) -> int:
        return self.__player["points"] if "points" in self.__player else 0

    @points.setter
    def points(self, points):
        if "points" not in self.__player:
            self.__player["points"] = points
        else:
            self.__player["points"] += points

    @property
    def name(self) -> str:
        return self.__player["name"] if "name" in self.__player else ""

    @name.setter
    def name(self, name):
        self.__player["name"] = name
