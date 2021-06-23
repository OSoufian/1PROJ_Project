class Player:

    def __init__(self, color):
        self.name = ""
        self.name_rect = None
        self.color = color
        self.marbles = []
        self.points = 0
    
    def __str__(self) -> str:
        return f"player with color = {self.color} - name = {self.name} - point = {self.points}"