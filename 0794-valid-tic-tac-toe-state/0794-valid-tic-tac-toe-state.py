class Solution:
    def has_won(self, board, player):
        # Check rows
        for row in board:
            if row[0] == player and row[1] == player and row[2] == player:
                return True

        # Check columns
        for col in range(3):
            if board[0][col] == player and board[1][col] == player and board[2][col] == player:
                return True

        # Check diagonals
        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            return True
        if board[0][2] == player and board[1][1] == player and board[2][0] == player:
            return True

        return False
    def validTicTacToe(self, board):
        x_count = 0
        o_count = 0
        for row in board:
            for c in row:
                if c == 'X':
                    x_count += 1
                elif c == 'O':
                    o_count += 1

        # Check if the number of Xs and Os is valid
        if x_count < o_count or x_count > o_count + 1:
            return False

        # Check if X has won
        if x_count - o_count == 0 and self.has_won(board, 'X'):
            return False

        # Check if O has won
        if x_count - o_count == 1 and self.has_won(board, 'O'):
            return False

        return True