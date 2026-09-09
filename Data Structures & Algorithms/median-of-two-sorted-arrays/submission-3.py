class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0

        t = len(nums1) + len(nums2)

        m1 = None
        m2 = None

        for k in range((t // 2) + 1):
            m2 = m1
            if i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    m1 = nums1[i]
                    i += 1
                else:
                    m1 = nums2[j]
                    j += 1
            elif i < len(nums1):
                m1 = nums1[i]
                i += 1
            else:
                m1 = nums2[j]
                j += 1
        
        print(m1, m2)

        if t % 2 == 0:
            return (m1 + m2) / 2
        
        return m1