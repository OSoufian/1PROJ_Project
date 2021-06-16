from typing import Counter


class Player:
    __player = {}

    def __init__(self, color, name, marbles = []):
        self.name = name
        self.color = color
        self.points = 0

    @property
    def marbles(self) -> list:
        return self.__player["marbles"] if "marbles" in self.__player else []

    @marbles.setter
    def marbles(self, marbles, remove=False):
        if isinstance(marbles, list):
                self.__player["marbles"] = marbles

        elif "marbles" not in self.__player:
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
