from collections import defaultdict

class Solution:
    def twoSum(nums):
        indices = defaultdict(list)
        
        for i, num in enumerate(nums):
            indices[num].append(i)
        return indices

s = Solution.twoSum([5,9,5,5,7,9])

