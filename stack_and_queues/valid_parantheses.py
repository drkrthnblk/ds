https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        brackets = {"(": ")","[":"]","{":"}"}
        
        for i in s:
            if i in brackets.keys():
                stack.append(brackets.get(i))
            else:
                if stack and stack[-1] == i:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True