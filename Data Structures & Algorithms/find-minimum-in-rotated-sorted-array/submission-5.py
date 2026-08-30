class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            if nums[l] < res:         # This checks if the current search range is already
                res = nums[l]         # sorted if yes then we dont have to search anymore
                break                 # as the min value is the left most one
            
            m = (l + r) // 2
            res = min(res, nums[m])

            if nums[m] >= nums[l]:   # If the above check fails that means the range is not
                l = m + 1            # yet sorted which means we have to search more for the
            else:                    # min value, here we assume that the middle is the
                r = m - 1            # smallest one if the nums[m] >= nums[l] this indicates
                                     # know that as the array is rotated the min value must be
                                     # in the right side so we search in the right side of the
                                     # array
                                     # in the else case it indicates that the array have not 
                                     # rotated enough so that the nums[m] is still less than 
                                     # the left most value so we have to search for the min 
                                     # value in the left side of the array

        return res