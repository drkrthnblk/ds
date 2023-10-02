https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'{': '}', '[': ']', '(':')'}
        stack = list()
        for ele in s:
            if ele in brackets.keys():
                stack.append(brackets.get(ele))
            else:
                if stack and stack[-1] == ele:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        return False