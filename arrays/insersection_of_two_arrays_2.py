https://leetcode.com/problems/intersection-of-two-arrays-ii/

#sol1
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1.sort()
        nums2.sort()
        intersect = list()
        m = len(nums1)
        n = len(nums2)
        diff = len(nums1) - len(nums2)
        # if nums1 has more elements, use nums2 as limiting array
        if diff > 0:
            count = 0
            m_idx, n_idx = 0,0
            while count < n:
                # if any of the index has exhausted, we are done
                if m_idx == m or n_idx == n:
                    break
                if nums1[m_idx] == nums2[n_idx] :
                    intersect.append(nums1[m_idx])
                    m_idx += 1
                    n_idx += 1
                    count += 1
                elif nums1[m_idx] < nums2[n_idx]:
                    m_idx += 1
                else:
                    n_idx += 1
                    count += 1
        # if nums2 has more elements, use nums1 as limiting array
        else:
            count = 0
            m_idx, n_idx = 0,0
            while count < m:
                # if any of the index has exhausted, we are done
                if m_idx == m or n_idx == n:
                    break
                if nums1[m_idx] == nums2[n_idx] :
                    intersect.append(nums1[m_idx])
                    m_idx += 1
                    n_idx += 1
                    count += 1
                elif nums1[m_idx] < nums2[n_idx]:
                    m_idx += 1
                    count += 1
                else:
                    n_idx += 1
        return intersect

#sol2

class Solution):
        nums1.sort(), nums2.sort()  # O(max(m, n) * log(max(m, n)))

        res = []

        it1, it2 = 0, 0
        while it1 < len(nums1) and it2 < len(nums2):
            if nums1[it1] < nums2[it2]:
                it1 += 1
            elif nums1[it1] > nums2[it2]:
                it2 += 1
            else:
                res += nums1[it1],
                it1 += 1
                it2 += 1

        return res