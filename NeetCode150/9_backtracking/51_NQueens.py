
#!PERMUTAZIONI di N colonne in N righe --> ogni colonna in una riga diversa --> N!
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def is_valid(board):
            #CHECK DIAGONALS
            diag = set()
            antidiag = set()

            for r in range(n):
                for c in range(n):
                    if board[r][c] == 'Q':
                        d = r - c
                        if d in diag:
                            return False
                        diag.add(d)

                        a = r + c
                        if a in antidiag:
                            return False
                        antidiag.add(a)
            
            return True

        board = [['.'] * n for _ in range(n)]

        

        res = []
        used = [False] * n
        def dfs(r: int):
            if r == n:
                if is_valid(board):
                    sol = []
                    for row in board:
                        sol.append("".join(row))
                    res.append(sol)

                return

            for i in range(n):
                if not used[i]:
                    used[i] = True
                    board[r][i] = 'Q'
                    dfs(r + 1)
                    board[r][i] = '.'
                    used[i] = False


        dfs(0)
        return res

        


#!PERMUTAZIONI with PRUNING di N colonne in N righe --> ogni colonna in una riga diversa 
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        board = [['.'] * n for _ in range(n)]
        

        res = []
        used = [False] * n
        antidiag = set()
        diag = set()

        def dfs(r: int):
            if r == n:
                sol = []
                for row in board:
                    sol.append("".join(row))
                res.append(sol)
                return

            
            for i in range(n):
                d = r - i
                a = r + i
                if not used[i] and a not in antidiag and d not in diag:
                    diag.add(d)
                    antidiag.add(a)
                    used[i] = True
                    board[r][i] = 'Q'

                    dfs(r + 1)

                    board[r][i] = '.'
                    used[i] = False
                    diag.remove(d)
                    antidiag.remove(a)


        dfs(0)
        return res

        


        