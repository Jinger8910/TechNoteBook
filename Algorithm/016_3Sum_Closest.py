"""
Given an array nums of n integers and an integer target, 
find three integers in nums such that the sum is closest to target. 
Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

class Solution:
    
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        Note: Similar to 3sum. Still use 3 pointer.
            Instead of looking for target, compare the absolute delta with target.
        """
        if len(nums) < 3:
            return None
        
        result = nums[0] + nums[1] + nums[2]
        nums.sort()

        for i in range(0, len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == target: # If lucky, we have sum that equals target
                    return sum
                
                if abs(target - sum) < abs(target - result):
                    result = sum
                
                if sum < target:
                    left += 1
                else:
                    right -= 1
        
        return result

s = Solution()
result = s.threeSumClosest([-1, 2, 1, -4], 1)
print(result)
input("Press Enter")