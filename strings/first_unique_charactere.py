https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        visited = dict()
        for i in range(len(s)):
            if s[i] in visited:
                visited[s[i]] = (-1, 0)
            else:
                visited[s[i]] = (1, i)
        
        for k,v in visited.items():
            if v[0] == 1:
                return v[1]
        return -1