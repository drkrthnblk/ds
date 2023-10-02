https://leetcode.com/problems/top-k-frequent-elements/description/

class Solution:
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        for ele in nums:
            freq[ele] = freq.get(ele, 0) + 1
        res = sorted(freq.items(), key=lambda item: item[1])
        return [ele[0] for ele in res[-1:-(k+1):-1]]