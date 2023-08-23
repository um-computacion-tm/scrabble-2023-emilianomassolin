class Board:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]

    def display(self):
        for row in self.board:
            print(' '.join(row))

# Crear un tablero de juego de Scrabble de 15x15
scrabble_board = Board(15, 15)

# Mostrar el tablero
scrabble_board.display()
