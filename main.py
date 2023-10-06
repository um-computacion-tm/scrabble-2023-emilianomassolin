from game.cell import *
from game.board import *
from game.tiles import *
from game.scrabble import *
from game.player import *




def main():
    print("Bienvenido!")
    board=Board()
    board.print_board()
    while True:
        try: 
            players_count = int(input("Ingrese cantidad de jugadores: "))
            if players_count <= 1 or players_count > 4:
                raise ValueError
            break
        except ValueError:
            print("Valor invalido")
    scrabble_game = ScrabbleGame(players_count=players_count)
    print("Cantidad de jugadores: ",len(scrabble_game.players))
    scrabble_game.next_turn()
   # #TODO while playing: loop por turno de jugador hasta que termine el juego
   # print(f"Turno del jugador {scrabble_game.current_player.id}")
   # word = input("Ingrese palabra: ")
   # location_x = input("Ingrese posicion X: ")
   # location_y = input("Ingrese posicion Y: ")
   # location = (location_x, location_y)
   # orientation = input("Ingrese orientacion (V/H)")
   # scrabble_game.validate_word(word, location, orientation)
main()        