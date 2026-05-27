


def verify(matr, sol, m):
    are_on = [0] * m

    for c in range(m):
        for r in sol:
            are_on[c] += matr[r][c]
        if are_on[c] %2 == 0:
            return False        
    
    return True

def powerset(pos, sol, n, k, start, matr, m): #n = rows = interruttori,  #m = cols = lampadine
    if pos >= k:
        if verify(matr, sol, m):
            return sol.copy()

        return None
    
    for i in range(start, n):
        sol[pos] = i
        res = powerset(pos + 1, sol, n, k, i + 1, matr, m)
        if res is not None:
            return res
    
    return None



