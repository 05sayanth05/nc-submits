class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # select the row and do a binary search on the row
        # we can even do binary serach vertically on the first element
        vrow = [row[0] for row in matrix]
        found, pos = self.binary_search(vrow, target)

        print(vrow, pos)

        if not found:
            return self.binary_search(matrix[pos], target)[0]
        
        return True


    
    def binary_search(self, nums: list[int], target: int) -> tuple[bool, int]:
        start, end = 0, len(nums) - 1
        mid = int((end - start) / 2)

        while start <= end:
            if nums[mid] == target:
                return True, 0
            
            if target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
            
            mid = start + int((end - start) / 2)
        
        return False, end
