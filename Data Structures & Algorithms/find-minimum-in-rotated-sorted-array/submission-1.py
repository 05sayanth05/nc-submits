class Solution:
    def findMin(self, nums: List[int]) -> int:
        m = nums[0]

        for n in nums:
            if m > n:
                return n
        
        return m