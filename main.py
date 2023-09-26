from game.cell import *
from game.board import *
from game.tiles import *
from game.scrabble import *
from game.player import *



def main():
    while True:
        try: 
            player = int(input("Indique la cantidad de jugadores: "))
            if player <= 1 or player > 4:
                raise ValueError
            break
        except ValueError:
            print("Valor invalido")
    scrabble_game = ScrabbleGame(player)
    for i in range(player):
        nombre = str(input(f"nombre del jugador {i+1}: " ))
        scrabble_game.players[i].name = nombre
main()        