##Task Description

Given some Chess moves in SAN (Standard Algebraic Notation), update the chess board state.

##Thought Template

```python
import chess

def find_checkmate_move(moves_san):
    # Initialize a new chess board
    board = chess.Board()

    # Apply the moves to the board
    for move_san in moves_san:
        # Remove move numbers and periods (e.g., "1." or "2.")
        if len(move_san.split('. ')) > 1:
            move_san = move_san.split('. ')[1]

        # Skip empty strings resulting from the removal
        if move_san:
            # Apply each move in SAN format to the board
            move = board.parse_san(move_san)
            board.push(move)

    # Generate all possible legal moves from the current position
    for move in board.legal_moves:
        # Make the move on a copy of the board to test the result
        board_copy = board.copy()
        board_copy.push(move)

        # Check if the move results in a checkmate
        if board_copy.is_checkmate():
            # Return the move that results in checkmate in SAN format
            return board.san(move)

    # Return "No solution found" message if no checkmate move exists
    return None

# Example usage:
# Input: Provide moves in SAN format
moves_san = [
    # Add your moves here
]
# Find the checkmate move
checkmate_move = find_checkmate_move(moves_san)
print(checkmate_move)
```