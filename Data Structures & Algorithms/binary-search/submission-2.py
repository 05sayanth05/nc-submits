class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        mid = int((end - start) / 2)
        # print(mid)
        
        while start <= end:
            # print(start, end, mid)
            if nums[mid] == target:
                return mid
            
            if target > nums[mid]:
                start = mid + 1
            elif target < nums[mid]:
                end = mid - 1
            
            mid = start + int((end - start) / 2)
            # print(start, end, mid)
        
        return -1

