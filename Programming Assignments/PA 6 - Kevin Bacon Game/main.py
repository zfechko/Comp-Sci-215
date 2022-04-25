import game as g
from os import system, name

def clear():
    """
    helper function that clears the terminal
    """
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def main():
    """
    main wrapper function that carries out game flow
    """
    game = g.Game()
    ended = False
    game.print_rules()
    while not ended:
        choice = game.search()
        if choice == "return":
            print("thanks for playing! See you later!")
            ended = True 
        elif choice != "":
            clear()
            game.print_results(choice)
            game.graph_results(choice)

if __name__ == "__main__":
    main()