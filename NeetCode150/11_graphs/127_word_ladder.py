#BRUTE FORCE SOLUTION
#!O(N*N*M) with M = length of th words and N = number of words


#!O(N*M*M) --> N*M for BFS and M for slicing pattern
#BFS
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        graph = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:] #returns "" instead of throwing error
                graph[pattern].append(word)
                
        visited = set()
        q = deque([beginWord])
        visited.add(beginWord)

        steps = 1
        while q:
            for _ in range(len(q)):
                currWord = q.popleft()                

                if currWord == endWord:
                    return steps
                
                for i in range(len(currWord)): 
                    pattern = currWord[:i] + "*" + currWord[i+1:] #O(M) complexity
                    for neigh in graph[pattern]:
                        if neigh not in visited:
                            visited.add(neigh)
                            q.append(neigh)

            steps += 1 
        
        return 0




       
