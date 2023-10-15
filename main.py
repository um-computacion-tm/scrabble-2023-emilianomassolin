from game.cell import *
from game.board import *
from game.tiles import *
from game.scrabble import *
from game.player import *
def main():
    print("Bienvenido!")
    while True:
        try: 
            players_count = int(input("Ingrese cantidad de jugadores: "))
            if players_count <= 1 or players_count > 4:
                raise ValueError
            break
        except ValueError:
            print("Valor invalido")
    scrabble_game = ScrabbleGame(players_count=players_count)
    for i in range(players_count):
        nombre = str(input(f"Indique nombre de jugador {i+1}: " ))
        scrabble_game.players[i].name = nombre
   # while True:
   #     try:
   #         scrabble_game.next_turn()
   #         scrabble_game.end_game()
   #         scrabble_game.show_current_player()
   #         scrabble_game.actual_turn()
   #     except   end_game:
   #         print("END GAME")
   #         break     
main()        