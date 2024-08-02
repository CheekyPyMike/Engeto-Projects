def print_greeting():
    """
    Pozdraví hráče a vypíše krátká pravidla hry.
    """
    print("Vítejte ve hře Tic-Tac-Toe (Piškvorky)!")
    print("Hráči se střídají v zadávání pozic pro umístění svého hracího kamene (X nebo O).")
    print("Cílem je získat tři kameny v řadě - horizontálně, vertikálně nebo diagonálně.")
    print("Užijte si hru!")
    print()

def print_board(board):
    """
    Vypíše aktuální stav hrací plochy.
    """
    print("  0 1 2")
    for idx, row in enumerate(board):
        print(idx, " ".join(row))
        if idx < 2:
            print("  -----")

def check_winner(board, player):
    """
    Kontroluje, zda hráč vyhrál.
    Prohledává řádky, sloupce a diagonály.
    """
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    """
    Kontroluje, zda je hrací plocha plná (remíza).
    """
    return all([cell != " " for row in board for cell in row])

def get_player_input(player):
    """
    Vyzývá hráče k zadání pozice.
    Kontroluje platnost vstupu (číselný a v rozsahu 0-2).
    """
    while True:
        try:
            row = int(input(f"Hráč {player}, zadej řádek (0, 1, 2): "))
            col = int(input(f"Hráč {player}, zadej sloupec (0, 1, 2): "))
            if row not in range(3) or col not in range(3):
                print("Neplatný vstup. Zadejte číslo mezi 0 a 2.")
            else:
                return row, col
        except ValueError:
            print("Neplatný vstup. Zadejte číselnou hodnotu.")

def main():
    """
    Hlavní funkce, která řídí průběh hry.
    """
    print_greeting()
    
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    while True:
        print_board(board)
        row, col = get_player_input(players[current_player])
        
        if board[row][col] != " ":
            print("Toto místo je již obsazeno. Zkuste to znovu.")
            continue
        
        board[row][col] = players[current_player]
        
        if check_winner(board, players[current_player]):
            print_board(board)
            print(f"Hráč {players[current_player]} vyhrál!")
            break
        if is_full(board):
            print_board(board)
            print("Remíza!")
            break
        
        current_player = 1 - current_player

if __name__ == "__main__":
    main()
