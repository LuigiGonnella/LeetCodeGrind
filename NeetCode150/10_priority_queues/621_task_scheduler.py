
#BRUTE FORCE --> PERMUTATIONS + CHECK --> O(N*N!)

#HASMAP WITH VALUE = LIST OF INDEXES AND LOOP OVER THE KEYS N TIMES UNTIL NO MORE KEY --> O(K*N) so O(N^2)


#!MAX HEAP --> O(N)
#pick first the task with MOST occurrencies

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        occ = Counter(tasks)
        max_heap = [-freq for freq in occ.values()] #occurrency heap

        heapq.heapify(max_heap)

        queue = deque() #cooldown queue

        cycles = 0
        while max_heap or queue:
            cycles += 1 #every iteration id a CPU cycle

            if not max_heap:
                cycles = queue[0][1] #go directly to first task in cooldown queue if no more available tasks
            else:
                cnt = - heapq.heappop(max_heap) - 1 #decrease count
                if cnt:
                    queue.append([cnt, cycles + n]) #insert in cooldown queue
                
            
            if queue and cycles == queue[0][1]: #cooldown ended
                cnt = queue.popleft()[0] 
                heapq.heappush(max_heap, - cnt) #re-insert in available tasks
            
        
        return cycles


#!GREEDY --> O(N)
#the most frequent task is the bottleneck. The total number of idles is assured to be (maxF - 1) * n --> n gaps between each most frequent element
#each different task, CAN ONLY be placed in a DIFFERENT gap of n idles (otherwise diff < n)
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        occ = 26 * [0]

        for task in tasks:
            occ[ord('A') - ord(task)] += 1
        
        occ.sort(reverse=True) 
        maxF = occ[0]
        idles = (maxF - 1) * n #the most frequent task is the bottleneck. The total number of idles is assured to be (maxF - 1) * n --> n gaps between each most frequent element

        for i in range(1, len(occ)):
            freq = occ[i]
            if idles > 0 and freq:
                idles -= min(freq, maxF - 1) #each different task, CAN ONLY be placed in a DIFFERENT gap of n idles (otherwise diff < n)
            elif idles <= 0:
                return len(tasks)
            
        return len(tasks) + idles




            


        