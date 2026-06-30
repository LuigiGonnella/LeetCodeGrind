
#!O(N) time and space
class Solution:
    def calPoints(self, operations: List[str]) -> int:

        tot = 0
        stack = []

        for op in operations:
            
            if op == "+":
                op2 = stack[-1]
                op1 = stack[-2]
                tot += (op1 + op2)
                stack.append(op1 + op2)
            elif op == "C":
                el = stack.pop()
                tot -= el
            elif op == "D":
                el = stack[-1]
                tot += (2 * el)
                stack.append(2 * el)
            else:
                tot += int(op)
                stack.append(int(op))
        
        return tot


        