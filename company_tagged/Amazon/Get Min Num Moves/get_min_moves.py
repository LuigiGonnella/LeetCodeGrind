
#!O(N) time and O(1) space
class Solution:
    def solve(self, blocks):
        n = len(blocks)

        minIdx = blocks.index(min(blocks))
        maxIdx = blocks.index(max(blocks))
        

        dist = (n - 1 - maxIdx) + (minIdx - 0)

        # Adjust by 1 if the elements have to cross paths
        return dist if maxIdx > minIdx else dist - 1


