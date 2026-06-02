#O(N) time and O(1) space
def minMoves(arr):
    # Write your code here
    
    def get_moves_left(val: int) -> int:
        target_idx = 0
        tot_moves = 0
        
        for i, el in enumerate(arr):
            if el == val:
                tot_moves += (i - target_idx)
            
                target_idx += 1
        
        return tot_moves
    
    #SCENARIO A --> move zeros to left O(N)
    zero_left = get_moves_left(0)
    
    #SCENARIO B --> move ones to left O(N)
    one_left = get_moves_left(1)
    
    return min(zero_left, one_left)

# STDIN     Function
# -----     -----
# 8      →  arr[i] size n = 8 
# 1      →  arr = [1, 1, 1, 1, 0, 1, 0, 1]
# 1                              
# 1                               
# 1                              
# 0                                              
# 1                               
# 0                                          
# 1   

# -->     OUTPUT: 3