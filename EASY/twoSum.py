#link: https://leetcode.com/problems/two-sum/
"""
class Solution(object):
    def twoSum(self, nums, target):
    
       # :type nums: List[int]
       # :type target: int
       # :rtype: List[int]
    
        for index, currentNum in enumerate(nums):
            goalNum = target - currentNum
            if goalNum in nums:
                return [nums.index(currentNum), nums.index(goalNum)]
                
        else:
            return None
"""

class Solution(object):
    def twoSum(self, nums, target):
        visited = set() #empty set

        for current in nums:
            goalNum = target - current
            if goalNum in visited:
                return [nums.index(current), nums.index(goalNum)]
            else:
                visited.add(current)

sol = Solution()
retList = sol.twoSum([2,7,15, 3], 10)
print(retList)