class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if target <= i[-1]:
                return self.bs(i, target)
        else:
            return False
    
    def bs(self, nums: List[int], target: int):

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return True
            elif nums[mid] < target: 
                l = mid + 1
            else:
                r = mid - 1
        return False

