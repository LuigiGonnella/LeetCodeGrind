
#!O(N) time and O(1) space
#KADANE'S ALGORITHM
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1, 1

        for num in nums:
            tmp_max = num * curMax
            tmp_min = num * curMin

            curMax = max(tmp_max, tmp_min, num)
            curMin = min(tmp_max, tmp_min, num)

            res = max(res, curMax)
        
        return res




#!O(N^2)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        maxProd = max(nums)
        for i in range(1, n):
            currProd = nums[i]
            for j in range(i - 1, -1, -1):
                currProd *= nums[j]
                maxProd = max(maxProd, currProd)
               
        
        return maxProd


#!O(N) time and O(1) space
#PREFIX, SUFFIX
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        prefix = suffix = 0

        res = float("-inf")
        for i in range(n):
            prefix = nums[i] * (prefix or 1) #if prefix is 0 take 1
            suffix = nums[n - i - 1] * (suffix or 1)
            res = max(res, prefix, suffix)

        
        return res


#!O(N) time and space
#SLIDING WINDOW
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        A = [] #contains segments (each segment is divided by a ZERO with adjacent segments)
        cur = [] #tracks current segment
        res = float('-inf') #tracks maximum element in array to initialize res

        for num in nums:
            res = max(res, num) #tracks maximum
            if num == 0: #segment finished
                if cur:
                    A.append(cur)
                cur = []
            else: #segment ongoing
                cur.append(num)

        if cur: #last segment if it was ongoing
            A.append(cur)

        for sub in A: #for each segment
            negs = sum(1 for i in sub if i < 0) #count how many negative numbers
            prod = 1
            need = negs if negs % 2 == 0 else negs - 1 #NEED must be EVEN
            negs = 0 #keep track of current negatives in order to match need
            j = 0 #sliding window LEFT pointer

            for i in range(len(sub)): #sliding window RIGHT pointer
                prod *= sub[i] #track running product
                if sub[i] < 0: #negative number encountered
                    negs += 1
                    while negs > need: #if we exceeded NEED
                        prod //= sub[j] #since we ALREADY CONSIDERED the LEFTMOST NEGATIVE (in previous iterations), we now SEARCH for IT and EXCLUDE IT
                        #we also EXCLUDE EVERY OTHER NUMBER from the product (even non negative) since we wantr COINTIGOUS SEGMENT EXCLUDING first negative
                        if sub[j] < 0: #found
                            negs -= 1 #exclude
                        j += 1

                if j <= i: #every time window is valid, update res
                    res = max(res, prod)

        return res

        