def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]  # Check rows
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]  # Check columns

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]  # Check diagonal (top-left to bottom-right)
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]  # Check diagonal (top-right to bottom-left)

    return None  # No winner yet

def is_board_full(board):
    # Check if the board is full (no empty spaces left)
    return all(all(cell != ' ' for cell in row) for row in board)

def play_tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")
    player1 = input("Enter name for Player 1 (X): ")
    player2 = input("Enter name for Player 2 (O): ")

    current_player = player1
    symbol = 'X'

    # Initialize the empty board
    board = [[' ' for _ in range(3)] for _ in range(3)]

    while True:
        print_board(board)

        # Get the player's move
        try:
            row = int(input(f"{current_player}, enter the row (0, 1, or 2): "))
            col = int(input(f"{current_player}, enter the column (0, 1, or 2): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # Check if the chosen cell is empty
        if board[row][col] == ' ':
            board[row][col] = symbol
            winner = check_winner(board)

            if winner:
                print_board(board)
                print(f"Congratulations, {current_player}! You win!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a tie! The board is full.")
                break

            # Switch to the other player for the next turn
            current_player = player2 if current_player == player1 else player1
            symbol = 'O' if symbol == 'X' else 'X'
        else:
            print("That cell is already taken. Try again.")

if __name__ == "__main__":
    play_tic_tac_toe()
