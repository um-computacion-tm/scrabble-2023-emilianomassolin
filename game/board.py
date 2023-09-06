from game.cell import Cell

class Board:
    def __init__(self):
        self.grid = [
            [ Cell(None,None,1, '') for _ in range(15) ]
            for _ in range(15)
        ]
