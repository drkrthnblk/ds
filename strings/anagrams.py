https://leetcode.com/problems/valid-anagram/

#sol1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1 = list(s)
        str2 = list(t)
        str1.sort()
        str2.sort()
        
        return "".join(str1) == "".join(str2)


# sol2

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1, d2 = {}, {}
        for i in s:
            d1[i] = d1.get(i,0) + 1
        for j in t:
            d2[j] = d2.get(j,0) + 1
        return d1 == d2