
#!O(NlogN) time and O(N) space --> sorting
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        n = len(hand)

        if n % groupSize != 0:
            return False
        
        occ = Counter(hand) #el: occurrencies
        hand.sort() #start from smallest to create group

        for el in hand: 
            if occ[el]:  
                for neigh in range(el, el + groupSize):
                    if not occ[neigh]:
                        return False
                    occ[neigh] -= 1
        
        return True

        
        
#!O(NlogN) time and O(N) space --> heap
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        n = len(hand)

        if n % groupSize != 0:
            return False
        
        occ = {}
        for n in hand:
            occ[n] = 1 + occ.get(n, 0)

        minH = list(occ.keys())
        heapq.heapify(minH) #i need heap to contain NON REPEATED elements

        while minH:
            curr_min = minH[0] #take smallest
            for neigh in range(curr_min, curr_min + groupSize): #check next elements in group
                if neigh not in occ: #if not present --> False
                    return False
                occ[neigh] -= 1
                if not occ[neigh]: #if now there are no more occurrencies --> pop from heap so it is not evaluated again
                    heapq.heappop(minH)

        
        return True   



#!O(N^2) worst case (if all numbers are incresing by 1 and sorted in decreasing order we would consider, for each number, each other lower number as possible start) time and O(N) space --> hashmap
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand) #--> counter is like defaultdict, we can access occ[el] and if el does not exist it returns 0 (faster than check if el not in occ)
        for num in hand:
            start = num
            while count[start - 1]:
                start -= 1
            while start <= num:
                while count[start]:
                    for i in range(start, start + groupSize):
                        if not count[i]:
                            return False
                        count[i] -= 1
                start += 1
        return True

        



