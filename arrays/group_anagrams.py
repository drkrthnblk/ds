https://leetcode.com/problems/group-anagrams/description/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mappings = dict()
        for word in strs:
            ana_word = list(word)
            ana_word.sort()
            ana_word = "".join(ana_word)
            if ana_word not in mappings:
                mappings[ana_word] = [word]
            else:
                word_list = mappings.get(ana_word)
                word_list.append(word)
                mappings[ana_word] = word_list
                
        return list(mappings.values())