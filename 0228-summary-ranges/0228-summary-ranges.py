class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        if nums == []: return []

        if len(nums) == 1: return [f"{nums[0]}"]


        l = 0
        result = []
        for i in range(1,len(nums)):
            if (nums[i] - nums[i-1] == 1):
                pass
            else:
                result.append(f"{nums[l]}" if nums[l] == nums[i-1] else f"{nums[l]}->{nums[i-1]}")
                l = i

        if nums != []:
            result.append(f"{nums[l]}" if nums[l] == nums[i] else f"{nums[l]}->{nums[i]}")
        
        return result