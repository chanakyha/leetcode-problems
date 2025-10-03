from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        frequency = (Counter(nums)).values()
        return (max(frequency) * list(frequency).count(max(frequency)))
        
        