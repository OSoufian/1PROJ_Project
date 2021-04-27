class Player(object):
    __player = {}

    def __new__(cls, **kwargs):

        return super(Player, cls).__new__()

    def __init__(self, **kwargs):
        players_data = ["circles", "colorn" "points", "nom"]
        for k in kwargs.keys():
            if k not in players_data:
                del kwargs[k]

        self.__player = kwargs

        self .get_id()

    @classmethod
    def get_id(cls):
        cls.__player["id"] = len(cls.__player.keys())-1
        
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
        return self.__player["color"] if "color" in self.__player else None

    @color.setter
    def color(self, color):
        self.__player["color"] = color

    @property
    def points(self) -> int:
        return self.__player["points"] if "points" in self.__player else None

    @points.setter
    def points(self, points, remove=False):
        if "points" not in self.__player:
            self.__player["points"] = points

        elif remove:
            self.__player["points"] += points
        else:
            self.__player["points"] -= points

    @property
    def getName(self) -> str:
        return self.__player["name"] if "name" in self.__player else None

    @getName.setter
    def getName(self, name):
        self.__player["name"] = name


