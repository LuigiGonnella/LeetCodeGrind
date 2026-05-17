
#!O(N^2)
#only lenght
class Solution: 
    def LIS(self, nums):
        if not nums:
            return 0
        
        
        dp = [1] * len(nums) #tracks current max len for the LIS where the element i is contained
        res = 1

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i] and dp[i] < dp[j] + 1: #only if i can be added to the LIS terminating with j and if this new LIS would be longer than the current
                    dp[i] = dp[j] + 1
            
            res = max(res, dp[i])
        
        return res #return number of elements in LIS


#!O(N^2)
#reconstruction of LIS
class Solution: 
    def LIS(self, nums):
        if not nums:
            return 0
        
        
        dp = [1] * len(nums) #tracks current max len for the LIS where the element i is contained
        pred = [-1] * len(nums) #tracks pred for the current LIS
        res = 1
        last = -1

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i] and dp[i] < dp[j] + 1: #only if i can be added to the LIS terminating with j and if this new LIS would be longer than the current
                    dp[i] = dp[j] + 1
                    pred[i] = j
            
            if dp[i] > res:
                res = dp[i]
                last = i #tracks last elemnt in global LIS
        
        lis = []
        def recosntruct(pred, last):

            while last != -1:
                lis.append(nums[last])
                last = pred[last]
        
        recosntruct(pred, last)
        lis.reverse()

        
        return res, lis

#!O(NlogN)
#length of LIS
class Solution: 
    def LIS(self, nums):
        if not nums:
            return 0
        
        
        sub = [] #!will NOT contain LIS but will have same length, we store values

        for num in nums:

            if not sub or num > sub[-1]:
                sub.append(num)
            else:
                idx = bisect.bisect_left(sub, num) #find first element in sub that is >= than num
                #replace it --> we maintain LOWEST POSSIBLE ending number for the LIS of length idx + 1
                sub[idx] = num
        
        return len(sub)

#!O(NlogN)
#reconstruction of LIS
class Solution: 
    def LIS(self, nums):
        if not nums:
            return 0
        
        pred = [-1] * len(nums)
        sub = [] #!will NOT contain LIS but will have same length, now we store indexes

        for i in range(len(nums)):
            left, right = 0, len(sub) - 1
            pos = len(sub) # Default to appending at the end
            
            while left <= right:
                m = left + (right - left) // 2

                if nums[i] > nums[sub[m]]:
                    left = m + 1
                else:
                    right = m - 1
                    pos = m 
            
            # If it's not the first element in the subsequence, record its predecessor
            if pos > 0:
                pred[i] = sub[pos - 1]
            
            # Overwrite or append the index to the sub array
            if pos == len(sub):
                sub.append(i)
            else:
                sub[pos] = i 

        #RECOSNTURCT
        lis = []
        def recosntruct(pred, last):

            while last != -1:
                lis.append(nums[last])
                last = pred[last]
        
        recosntruct(pred, sub[-1])
        lis.reverse()

            
        
        return len(sub), lis

        
