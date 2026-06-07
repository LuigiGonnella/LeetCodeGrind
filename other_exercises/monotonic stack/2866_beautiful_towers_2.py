class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        
        n = len(maxHeights)
        
        left = [0] * n
        stack = [-1] #stack will never be empty --> if i pop -1 will correctly count A[j] to delete from the running sum (pop 0 and remains -1)
        curr = 0 #running sum treating each eleemnt as the peak, then if we increase window and another new minimum gets in, we must delete
        #the old sum of the last stint (previous minimum - previous previous minimum) and add this one (new minimum - previous previous minimum that now is the previous minimum)

        #we compute the running sum for each element assuming it is the peak (real peak will have final sum as the biggest)
        for idx in range(n):

            while len(stack) > 1 and maxHeights[stack[-1]] > maxHeights[idx]:
                j = stack.pop()
                curr -= (j - stack[-1]) * maxHeights[j] #DELETE sum from j to previous minimum, since therre will be a new minimum after the while (substitute this one)
            
            #now the new minimum is in i and the previous is in stack[-1], we want to ADD this new sum
            curr += (idx - stack[-1]) * maxHeights[idx]
            stack.append(idx)
            left[idx] = curr
        
        #do the same from right --> at the end the final sum will be maximum for the peak
        stack = [n] #stack will never be empty --> if i pop n will correctly count A[j] to delete from the running sum (pop n - 1 and remains n, then put negative)
        curr = 0 #running sum treating each eleemnt as the peak, then if we increase window and another new minimum gets in, we must delete
        #the old sum of the last stint (previous minimum - previous previous minimum) and add this one (new minimum - previous previous minimum that now is the previous minimum)

        res = float("-inf")
        #we compute the running sum for each element assuming it is the peak (real peak will have final sum as the biggest)
        for idx in range(n - 1, -1, -1):

            while len(stack) > 1 and maxHeights[stack[-1]] > maxHeights[idx]:
                j = stack.pop()
                curr -= -(j - stack[-1]) * maxHeights[j] #DELETE sum from j to previous minimum, since therre will be a new minimum after the while (substitute this one)
            
            #now the new minimum is in i and the previous is in stack[-1], we want to ADD this new sum
            curr += -(idx - stack[-1]) * maxHeights[idx] #- since we are going right
            stack.append(idx)
            res = max(res, left[idx] + curr - maxHeights[idx]) #counted 2 times maxHeights[idx], so delete one
        
        return res

     
            
        