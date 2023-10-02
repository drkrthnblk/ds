https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1 = list(s)
        str2 = list(t)
        str1.sort()
        str2.sort()
        
        return "".join(str1) == "".join(str2)