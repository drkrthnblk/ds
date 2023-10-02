https://leetcode.com/problems/daily-temperatures/description/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        
        stack.append(len(temperatures)-1) 
        
        for idx in range(len(temperatures)-2, -1, -1):
            # if we get inc seq then we will remove the existing ele in stack
            # as it won't be higher than the curr ele
            while stack and temperatures[idx] >= temperatures[stack[-1]]:
                stack.pop()
            # compare the curr ele and add the curr ele in stack to compare with new values
            if stack:
                res[idx] = stack[-1] - idx
            stack.append(idx)
            
        return res