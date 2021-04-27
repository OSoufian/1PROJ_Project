class Players:
    __players = []

    def new_player(self):
        self.__players = Player(self.__players)

    @classmethod
    def getPlayers(cls) -> list:
        return cls.__players


class Player(object):
    __player = {}

    def __new__(cls, players=None, **kwargs):
        players = [] if players is None else players

        player = super(Player, cls).__new__(cls)

        players_data = ["circles", "colorn" "points", "nom"]
        for k in kwargs.keys():
            if k not in players_data:
                del kwargs[k]

        cls.__player = kwargs

        cls.__player["id"] = len(players)

        players.append(player)

        return players

    @property
    def player_id(self) -> int:
        return self.__player["id"]

    @property
    def circles(self) -> list:

        return self.__player["circles"] if "circles" in self.__player else None

    @circles.setter
    def circles(self, circles, remove=False):
        if "circles" not in self.__player:
            self.__player["circles"] = []
            remove = False
        if remove:
            self.__player["circles"].remove(circles)
        self.__player["circles"].append(circles)

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
        return self.__player["name"] if "name" in self.__player else None

    @name.setter
    def name(self, name):
        self.__player["name"] = name