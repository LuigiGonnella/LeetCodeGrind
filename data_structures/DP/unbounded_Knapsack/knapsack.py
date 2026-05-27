
#!O(N*CAP)
def unbounded_knapsack_memo(weights: list[int], values: list[int], cap: int) -> int:
    # Initialize the cache array with -1 (Translates: int *maxKnown)
    max_known = [-1] * (cap + 1)
    
    def dp(current_cap: int) -> int: #CAP runs
        # Base Case / Cache Hit: If we already calculated this capacity, return it!
        if max_known[current_cap] != -1:
            return max_known[current_cap]
            
        max_val = 0
        
        # Try every single item for the current capacity
        for i in range(len(weights)): #N other runs
            space = current_cap - weights[i]
            
            # If the item fits, recursively find the max for the remaining space
            if space >= 0:
                t = dp(space) + values[i]
                if t > max_val:
                    max_val = t
                    
        # Save the result in the cache before returning
        max_known[current_cap] = max_val
        return max_val

    return dp(cap)