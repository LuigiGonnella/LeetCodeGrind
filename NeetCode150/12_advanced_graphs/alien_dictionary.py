#DFS with 3 state
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {c: [] for word in words for c in word} #O(TOTAL LENGTH)

        for i in range(len(words) - 1):
            len1 = len(words[i])
            len2 = len(words[i + 1])
            min_len = min(len1, len2)

            if len2 < len1 and words[i][:len2] == words[i + 1][:len2]: #invalid prefix edge case
                return ""

            for j in range(min_len):
                if words[i][j] != words[i + 1][j]:
                    graph[words[i][j]].append(words[i + 1][j])
                    break
        
        
        state = defaultdict(int)
        res = []
        def dfs(node): #once we construct the graph it MUST be a DAG (acyclic)
            if state[node] == 1:
                return False

            if state[node] == 2:
                return True

            state[node] = 1

            for neigh in graph[node]:
                if not dfs(neigh):
                    return False

            res.append(node)
            state[node] = 2
            return True
        
        #!O(V + E) = O(total length)
        for node in graph:
            if not dfs(node):
                return ""

        
        return "".join(res[::-1])

#!O(TOTAL LENGTH)
#KAHN'S algorithm
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {}
        in_degree = {}
        for word in words:
            for c in word:
                if c not in graph:
                    graph[c] = list()
                if c not in in_degree:
                    in_degree[c] = 0

        for i in range(len(words) - 1):
            len1 = len(words[i])
            len2 = len(words[i + 1])
            min_len = min(len1, len2)

            if len2 < len1 and words[i][:len2] == words[i + 1][:len2]: #invalid prefix edge case
                return ""

            for j in range(min_len):
                if words[i][j] != words[i + 1][j]:
                    graph[words[i][j]].append(words[i + 1][j])
                    in_degree[words[i + 1][j]] += 1
                    break
        
        
        q = deque([c for c in in_degree if in_degree[c] == 0])
        res = []
        while q:
            curr = q.popleft()
            res.append(curr)
            for neigh in graph[curr]:
                in_degree[neigh] -= 1 #if there is a cycle this will go negative so we don't append anymore the char and we don't visit the others
                if in_degree[neigh] == 0:
                    q.append(neigh)

        if len(res) != len(in_degree): #cycle detected --> queue emptied before visiting all nodes
            return ""
        
        return "".join(res)

