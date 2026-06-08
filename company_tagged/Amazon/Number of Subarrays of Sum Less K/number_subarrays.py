class Solution:
    def solve(self, nums, k) -> int:
        
        n = len(nums)
        l = 0

        min_queue = deque() #tracks smallest in window
        max_queue = deque() #tracks bigger in window
        n_subarrays = 0

        for r in range(n): #for every end

            #update min_queue
            while min_queue and nums[min_queue[-1]] >= nums[r]:
                min_queue.pop()
            
            #update max_queue
            while max_queue and nums[max_queue[-1]] <= nums[r]:
                max_queue.pop()

            min_queue.append(r)
            max_queue.append(r)

            #max_queue[0] will have the biggest elemnt in window and min_queue the minimum
            #if the window has a difference too BIG --> the only way to reduce it is to shrink from left (hoping a bigger smaller element comes)
            #i will do this until the condition is met (will always be at least the same element in both queues --> difference is 0 and k is always >= 0)
            while nums[max_queue[0]] - nums[min_queue[0]] > k: #while it is NOT valid
                l += 1 #shrink window

                if max_queue[0] < l: #if now smallest is outside --> pop
                    max_queue.popleft()
                
                if min_queue[0] < l: #same for maximum
                    min_queue.popleft()

            n_subarrays += (r - l + 1) #if [l, r] is valid, then all inner subarrays ending on r are --> r - l + 1

        return n_subarrays