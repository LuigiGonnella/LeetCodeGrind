
#!O(M ^ 2 * N ^ 2)
class Solution:
    def solve(self, n, m, k, paint):


        squares = (m - k + 1) * (n - k + 1) #number of squares k * k in grid

        occ = [0] * squares #frequenxy map of blacks in each square

        for minute, (r, c) in enumerate(paint): #O(M*N) for every cell
            r -= 1
            c -= 1
            for s in range(squares): #O(M * N) for every square
                start_r = s // (m - k + 1)
                end_r = start_r + k - 1

                start_c = s % (m - k + 1)
                end_c = start_c + k - 1

                if r  >= start_r and r <= end_r and c >= start_c and c <= end_c: #if the cell belongs to this square
                    occ[s] += 1 #add the black count
                    if occ[s] == k * k: #if all square is black
                        return minute + 1
        return -1
                    


#!O(M * N * K²)
class Solution:
    def solve(self, n, m, k, paint):
        squares_per_row = m - k + 1
        occ = [0] * ((n - k + 1) * (m - k + 1))

        for minute, (r, c) in enumerate(paint):
            r -= 1
            c -= 1

            min_start_r = max(0, r - k + 1) #all squares containing this cell
            max_start_r = min(r, n - k)

            min_start_c = max(0, c - k + 1)
            max_start_c = min(c, m - k)

            for sr in range(min_start_r, max_start_r + 1):
                for sc in range(min_start_c, max_start_c + 1):
                    square_id = sr * squares_per_row + sc #Y * width + X
                    occ[square_id] += 1

                    if occ[square_id] == k * k:
                        return minute + 1

        return -1

#!2D SLIDING WINDOW APPROACH
#O(N * M)
class Solution:
    def solve(self, n, m, k, paint):
        
        time = [[0] * m for _ in range(n)] #stores UNLOCK minute for each pixel

        for minute, (r, c) in enumerate(paint):
            time[r - 1][c - 1] = minute
        

        ########### PHASE 1 ##############
        #Now we want to find the MAXIMUM TIME for EVERY KxK grid
        #since the maximum one is the time when ALL the square will be black

        #We first compress each row into m - k + 1 values (#squares) --> max per segment
        #MAX HORIZONTAL SEGMENTS
        row_max = [[0] * (m - k + 1) for _ in range(n)]

        for r in range(n):
            q = deque() #MONOTONIC DECREASING DEQUE TO STORE THE MAX --> contains [c]

            for c in range(m):

                #delete elements out of window
                while q and q[0] <= c - k:
                    q.popleft()
                
                #maintain decreasing status
                while q and time[r][q[-1]] <= time[r][c]:
                    q.pop()
                
                q.append(c)
                
                if c >= k - 1: #for each window, pop maximum
                    row_max[c - k + 1] = time[r][q[0]]
        
        #Then we must compute the maximum in each vertical segment basing on the horizontal segments
        #MAX VERTICAL SEGMENTS --> this will compute the maximum for each KxK square, the we just pick the minimum

        min_time = float("+inf")

        for c in range(m - k + 1):
            q = deque() #contains [r]

            for r in range(n):

                #delete indexes out of range
                while q and q[0] <= r - k:
                    q.popleft()
                
                #maintain decreasing property
                while q and row_max[q[-1]][c] <= row_max[r][c]:
                    q.pop()
                
                q.append(r)

                ########### PHASE 2 ##############
                #Once did so we must find the SMALLEST across these values --> FIRST SQUARE to be beautiful
                if r >= k  - 1: #for each window, get max, update min
                    min_time = min(min_time, row_max[q[-1]][c])


        return min_time