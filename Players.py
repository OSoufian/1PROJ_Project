"""import pygame

players = {}

class players():"""


class Player:
    def __init__(self, players, coordinates):
        self._players = players
        self.coordinates = coordinates

    @property
    def players(self):
        return self._players

    @players.setter
    def players(self, name, value=None):
        if value is None:
            return
        self._players[name]=value

