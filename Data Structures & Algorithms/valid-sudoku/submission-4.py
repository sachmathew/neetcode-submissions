class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for r in range(9)]
        cols = [{} for c in range(9)]
        squares = [[{} for c in range(3)] for r in range(3)]
        for r in range(9):
            for c in range(9):
                b = board[r][c]
                if b != ".":
                    rows[r][b] = rows[r].get(b, 0)+1
                    cols[c][b] = cols[c].get(b, 0)+1
                    squares[r//3][c//3][b] = squares[r//3][c//3].get(b, 0)+1
                    if rows[r][b] > 1 or cols[c][b] > 1 or squares[r//3][c//3][b] > 1:
                        return False
        return True