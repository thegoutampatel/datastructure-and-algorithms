
# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

# https://leetcode.com/problems/3sum-closest/description/
###################################################################################

def threeSumClosest(nums, target):
    nums.sort()
    answer = nums[0] + nums[1] + nums[2]

    for i in range(len(nums)-2):
        
        j = i + 1
        k = len(nums) - 1
        while j < k:
            sum = nums[i] + nums[j] + nums[k]

            if abs(sum-target) < abs(answer - target):
                answer = sum

            if sum < target:
                j = j+1
            elif sum > target:
                k = k-1
            else:
                return target
    return answer

#Driver Code        
nums = [-1,2,1,-4]
target = 1
result = threeSumClosest(nums,target)
print(result)