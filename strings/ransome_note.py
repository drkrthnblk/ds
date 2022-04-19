https://leetcode.com/problems/ransom-note/

#sol1
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = dict()
        for letter in magazine:
            freq[letter] = freq.get(letter, 0) + 1
        
        for letter in ransomNote:
            if letter not in freq.keys():
                return False
            elif freq.get(letter) == 0:
                return False
            else:
                freq[letter] = freq.get(letter) -1
        return True

#sol2

class Solution:
    def canConstruct(self, r: str, m: str) -> bool:
        a=[0]*26
        for i in m:
            c=(ord(i)-97)
            a[c]+=1
        for j in r:
            d=(ord(j)-97)
            if a[d]==0:
                return False
            a[d]-=1
        return True
