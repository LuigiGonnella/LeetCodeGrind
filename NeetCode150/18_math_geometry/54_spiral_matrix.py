
#!O(N*M) time and O(1) extra space
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # visit in 4 directions every time, reducing top, right, bottom, left

        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])
        res = []
        while left < right and top < bottom:
            
            #scan top from left to right
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            #scan right from top to bottom
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom): #remaining rectangle is invalid (would generate duplicates)
                break

            #scan bottom from right to left
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            #scan left from bottom to top
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        
        return res
