
#! O(NlogN) time and O(1) space
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()
        n = len(people)
        l, r = 0, n - 1

        boats = 0
        while l < r:

            if people[l] + people[r] <= limit:
                l += 1
            
            r -= 1
            boats += 1
        
        
        return boats + 1 if l == r else boats

            



#! O(N) time and O(M) space, same idea but with counting sort
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        m = max(people)
        count = [0] * (m + 1)

        for p in people:
            count[p] += 1

        idx = 0
        n = len(people)

        for i in range(m + 1):
            if idx >= n:
                break

            if not count[i]:
                continue

            while count[i] and idx < n:
                people[idx] = i
                count[i] -= 1
                idx += 1


        l, r = 0, n - 1

        boats = 0
        while l < r:

            if people[l] + people[r] <= limit:
                l += 1
            
            r -= 1
            boats += 1
        
        
        return boats + 1 if l == r else boats

        