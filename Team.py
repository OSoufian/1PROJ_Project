class Team:

    def __init__(self, players: tuple):
        self.players = players
        self.points = 0
        self.marbles = [(c, d) for player in self.players for c, d in player.marbles]
