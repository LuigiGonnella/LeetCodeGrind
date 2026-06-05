

#TWO POINTERS
#!O(M * N) with M = maxCost and N = len(itemCost) and O(1) space
class Solution:

    def solve(self, itemCost):


        itemCost.sort()
        max_item = itemCost[-1]
        n = len(itemCost)

        max_packages = -1

        for target in range(1, (2 * max_item) + 1): #max target is maximum pair sum

            curr_packages = 0
            l, r = 0,  n - 1

            while l <= r:

                if itemCost[r] == target: #CASE 1 --> RIGHT IS BIGGER
                    curr_packages += 1
                    r -= 1
                
                elif itemCost[r] + itemCost[l] > target:  #CASE 2 --> SUM IS BIGGER
                    r -= 1
                
                elif l < r and itemCost[r] + itemCost[l] == target:  #CASE 3 --> SUM IS EQUAL
                    curr_packages += 1
                    l += 1
                    r -= 1
                else: #CASE 4 --> SUM IS SMALLER
                    l += 1
            
            max_packages = max(max_packages, curr_packages)

            
            
        
        return max_packages

                        
