
#!#O(M + N)
class Solution:
    def solve(self, arr, state, m) -> List[int]:

        avail = defaultdict(list)

        step = float("+inf")
        #O(N)
        for i, el in enumerate(state):
            if el == "1":
                step = 0
                avail[step].append(i)
            else:
                step += 1
                avail[step].append(i)

        
        max_el = float("-inf")
        res = []

        #O(M + N)
        for step in range(m): #for eevery step WE DON'T LOOK to EACH element
            #Instead, we look to ALL elements SUMMING all steps
            #add all available elements to heap
            if avail[step]:
                max_unlocked = max(arr[idx] for idx in avail[step])
                max_el = max(max_el, max_unlocked)

            if max_el != float("-inf"):
                res.append(max_el)

        
        return res
