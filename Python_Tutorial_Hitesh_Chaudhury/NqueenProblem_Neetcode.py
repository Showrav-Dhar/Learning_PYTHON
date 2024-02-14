def solveNQueen(n):
    col = set()
    posDiag = set()  # r+c
    negDiag = set()  # r-c

    res = []
    board = [['.'] * n for i in range(n)]  # N x N chess board
    # board = N number of strings which length is also N

    def backTrack(r):
        if r == n:  # recursion stop condition -> if r == n then all the queens are placed safely
            # output is each row is joined together
            copy = [".".join(row) for row in board]
            res.append(copy)
            return

        for c in range(n):  # c = column
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                # checking if c is already used or c is in positive diagonal or in negative diagonal
                continue
            else:
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = 'Q'
                backTrack(r + 1)
                # clean up
                # backtracking to the initial conditions
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = '.'

    backTrack(0)
    return res


if __name__ == '__main__':

    n = 4
    result = solveNQueen(n)
    print(f"For {n} Queens , solutions are ")
    for i in range(len(result)):
        print(f"Solution {i+1} - ")
        for j in range(len(result[i])):
            print(result[i][j], end='')
            print()