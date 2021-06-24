class Team:

    def __init__(self, players=[]):
        self.players = players.copy()
        self.points = 0
        self.marbles = [(c, d) for player in self.players for c, d in player.marbles]

    def add_players(self, player):
        self.players.append(player)
        self.players = self.players.copy()
        player.team = self
    
    def __repr__(self):
        return f"Team object ({', '.join(str(player) for player in self.players)})"
    
    def update(self):
        self.marbles = [(c, d) for player in self.players for c, d in player.marbles]
