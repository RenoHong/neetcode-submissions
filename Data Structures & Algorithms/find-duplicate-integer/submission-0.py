class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        left = nums[0] 
        for i in range(1, len(nums)):
            if left == nums[i]:
                return left 
            left = nums[i]
        