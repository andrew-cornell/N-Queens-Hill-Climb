import random

def generate_board(n):
    board = [0] * n
    for col in range(n):
        row = random.randint(0, n - 1)
        board[col] = row
    return board

#counts num of attacks in current state
def compute_attacks(board):
    n = len(board)
    attacks = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                attacks += 1
    return attacks

#
def hill_climb(n):
    board = generate_board(n)
    #list of moves towards solution
    steps = [list(board)]
    while True:
        current_attacks = compute_attacks(board)
        if current_attacks == 0:
            return board, steps
        best_moves = []
        #loop through possible moves
        for col in range(n):
            for row in range(n):
                if board[col] != row:
                    board_copy = list(board)
                    board_copy[col] = row
                    new_attacks = compute_attacks(board_copy)
                    #add state to best moves if there are equal or less attacks
                    if new_attacks < current_attacks:
                        best_moves = [(col, row)]
                        current_attacks = new_attacks
                    elif new_attacks == current_attacks:
                        best_moves.append((col, row))
        #return none if there are no better moves
        if len(best_moves) == 0:
            return None, steps
        #randomly choose next move from list of best moves
        col, row = random.choice(best_moves)
        board[col] = row
        steps.append(list(board))

n = 8 # num of queens
solution = hill_climb(n)
if solution is not None:
    print("Solution found:")
    for row in solution[0]:
        print(" ".join(["Q" if col == row else "." for col in range(n)]))
    print(f"\nSteps taken: {len(solution[1])}")
    for i, step in enumerate(solution[1]):
        print(f"\nStep {i}:")
        for row in step:
            print(" ".join(["Q" if col == row else "." for col in range(n)]))
else:
    print("No solution found.")

